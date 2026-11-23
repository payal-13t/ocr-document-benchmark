import argparse
import csv
import json
from pathlib import Path
from .pipeline import extract_text, evaluate_dataset

def main():
    parser = argparse.ArgumentParser(description="OCR scanned documents with Tesseract.")
    sub = parser.add_subparsers(dest="command", required=True)
    one = sub.add_parser("ocr", help="OCR a single image")
    one.add_argument("image")
    ev = sub.add_parser("evaluate", help="Evaluate the bundled labelled dataset")
    ev.add_argument("--images", default="data/scanned")
    ev.add_argument("--truth", default="data/ground_truth")
    ev.add_argument("--output", default="reports/evaluation.csv")
    args = parser.parse_args()
    if args.command == "ocr":
        print(extract_text(args.image))
    else:
        rows, metrics = evaluate_dataset(args.images, args.truth)
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["document","cer","wer","reference_chars","reference_words","ocr_text"])
            writer.writeheader()
            writer.writerows(rows)
        Path("reports/metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        print(json.dumps(metrics, indent=2))
        print(f"Saved per-document results to {out}")
if __name__ == "__main__":
    main()
