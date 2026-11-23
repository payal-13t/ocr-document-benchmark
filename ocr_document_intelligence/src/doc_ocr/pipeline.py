"""OCR pipeline using the open-source Tesseract engine via pytesseract."""
from pathlib import Path
import re
import cv2
import pytesseract

def preprocess_image(image_path: str | Path):
    """Deskew-ready basic preprocessing: grayscale, upscale, denoise, adaptive threshold."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=1.35, fy=1.35, interpolation=cv2.INTER_CUBIC)
    denoised = cv2.GaussianBlur(gray, (3, 3), 0)
    processed = cv2.adaptiveThreshold(
        denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 11
    )
    return processed

def extract_text(image_path: str | Path, lang: str = "eng") -> str:
    """Extract text from a scanned image using Tesseract OCR."""
    processed = preprocess_image(image_path)
    return pytesseract.image_to_string(processed, lang=lang, config="--oem 3 --psm 6").strip()

def normalise(text: str) -> str:
    """Normalise whitespace for fair text comparison."""
    return re.sub(r"\s+", " ", text).strip()

def edit_distance(a: str, b: str) -> int:
    """Levenshtein distance with O(min(n, m)) memory."""
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]

def character_error_rate(reference: str, hypothesis: str) -> float:
    ref, hyp = normalise(reference), normalise(hypothesis)
    return edit_distance(ref, hyp) / max(1, len(ref))

def word_error_rate(reference: str, hypothesis: str) -> float:
    ref, hyp = normalise(reference).split(), normalise(hypothesis).split()
    return edit_distance(ref, hyp) / max(1, len(ref))

def evaluate_dataset(images_dir: str | Path, truth_dir: str | Path):
    """Evaluate all matching PNG/TXT pairs and return per-document and aggregate metrics."""
    images_dir, truth_dir = Path(images_dir), Path(truth_dir)
    rows = []
    for image_path in sorted(images_dir.glob("*.png")):
        truth_path = truth_dir / f"{image_path.stem}.txt"
        if not truth_path.exists():
            raise FileNotFoundError(f"Missing ground truth for {image_path.name}")
        reference = truth_path.read_text(encoding="utf-8")
        prediction = extract_text(image_path)
        rows.append({
            "document": image_path.name,
            "cer": character_error_rate(reference, prediction),
            "wer": word_error_rate(reference, prediction),
            "reference_chars": len(normalise(reference)),
            "reference_words": len(normalise(reference).split()),
            "ocr_text": prediction,
        })
    if not rows:
        raise ValueError(f"No PNG documents found in {images_dir}")
    total_chars = sum(r["reference_chars"] for r in rows)
    total_words = sum(r["reference_words"] for r in rows)
    # Corpus-level error rates are computed over concatenated aligned document text.
    refs, hyps = [], []
    for row in rows:
        refs.append(normalise((truth_dir / f"{Path(row['document']).stem}.txt").read_text(encoding="utf-8")))
        hyps.append(normalise(row["ocr_text"]))
    corpus_cer = edit_distance("\n".join(refs), "\n".join(hyps)) / max(1, total_chars + len(rows)-1)
    corpus_wer = edit_distance(" ".join(" ".join(x.split()) for x in refs).split(),
                               " ".join(" ".join(x.split()) for x in hyps).split()) / max(1, total_words)
    return rows, {"documents": len(rows), "cer": corpus_cer, "wer": corpus_wer,
                  "character_accuracy": max(0.0, 1.0-corpus_cer),
                  "word_accuracy": max(0.0, 1.0-corpus_wer)}
