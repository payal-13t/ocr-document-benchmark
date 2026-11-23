# Scanned Document OCR Benchmark (20 Documents)

A small, reproducible document-intelligence project that extracts text from scanned invoices and purchase orders using **Tesseract OCR** (open-source OCR engine) through `pytesseract`. It evaluates OCR output against human-readable ground-truth transcripts and reports **Character Error Rate (CER)** and **Word Error Rate (WER)**.

## Why this project?

It demonstrates practical Python, image preprocessing, OCR integration, dataset/ground-truth management, evaluation metrics, CLI design, and automated tests. It is suitable as a portfolio project for Python, data engineering, automation, or applied AI roles.

## Dataset

- 20 generated scanned-style document images (`data/scanned/`): 10 invoices and 10 purchase orders.
- Matching reference transcripts (`data/ground_truth/`).
- The images contain printed English text, subtle scan noise, and small rotation variations.
- This is a controlled benchmark dataset, not a claim of performance on arbitrary real-world handwriting or poor-quality archival scans.

## OCR and evaluation

Pipeline steps:
1. Load each PNG with OpenCV.
2. Convert to greyscale and upscale by 1.35x.
3. Apply Gaussian denoising and adaptive thresholding.
4. Run Tesseract with English language data (`--oem 3 --psm 6`).
5. Compare prediction with the paired reference transcript.

Metrics:
- **CER** = character edit distance / number of reference characters.
- **WER** = word edit distance / number of reference words.
- **Character accuracy** = `1 - CER`.
- **Word accuracy** = `1 - WER`.

CER/WER are error rates, so lower is better. Accuracy figures are derived from these error rates and are not classification accuracy.

## Benchmark results

Results are populated from an actual run of the included OCR pipeline on all 20 bundled images. See the table below and `reports/` for per-document output.

<!-- RESULTS_START -->
| Metric | Result |
|---|---:|
| Documents evaluated | 20 |
| Corpus character error rate (CER) | 1.32% |
| Corpus word error rate (WER) | 3.90% |
| Character accuracy (1 - CER) | 98.68% |
| Word accuracy (1 - WER) | 96.10% |
| Mean per-document CER | 1.32% |
| Mean per-document WER | 3.88% |

**Interpretation:** On this controlled 20-image dataset, the pipeline achieved 98.68% character accuracy and 96.10% word accuracy. These figures describe only this generated dataset and this Tesseract/preprocessing configuration. They are not a guarantee for unrelated real-world scans.

<!-- RESULTS_END -->

## Setup

### 1. Install Tesseract

The Python package is only a wrapper. Install the Tesseract OCR engine and English language data separately:

- **Windows:** Install the Tesseract OCR Windows installer, then add its installation folder (commonly `C:\\Program Files\\Tesseract-OCR`) to your system `PATH`.
- **macOS:** `brew install tesseract`
- **Ubuntu/Debian:** `sudo apt-get update && sudo apt-get install -y tesseract-ocr tesseract-ocr-eng`

Check installation:

```bash
tesseract --version
```

### 2. Create an environment and install dependencies

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Then:
```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 3. Run OCR on one document

```bash
python -m doc_ocr.cli ocr data/scanned/doc_01.png
```

### 4. Evaluate all 20 documents

```bash
python -m doc_ocr.cli evaluate
```

This writes:
- `reports/evaluation.csv`: OCR text and CER/WER for each document.
- `reports/metrics.json`: aggregate benchmark metrics.

### 5. Run tests

```bash
pytest -q
```

## Project structure

```text
scanned-document-ocr/
├── data/
│   ├── scanned/          # 20 PNG scans
│   └── ground_truth/     # paired reference transcripts
├── reports/              # generated evaluation output
├── src/doc_ocr/
│   ├── pipeline.py       # preprocessing, OCR, CER/WER, evaluation
│   └── cli.py            # command-line interface
├── tests/                # unit tests
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Limitations and next improvements

- Dataset is synthetic and English-only. Benchmark results should not be generalised to all document types.
- Tesseract quality depends on scan resolution, language packs, fonts, skew, and layout.
- Useful next steps: test on a public scanned-document dataset, add deskew detection, compare preprocessing strategies, add PDF page ingestion, and extract structured fields into CSV/JSON.

## GitHub publishing

1. Create a new empty GitHub repository, for example `scanned-document-ocr-benchmark`.
2. Extract this ZIP and open the folder in VS Code.
3. In the terminal:

```bash
git init
git add .
git commit -m "Build 20-document Tesseract OCR benchmark"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/scanned-document-ocr-benchmark.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Resume bullet (use only after reviewing your measured result)

Built a Python OCR evaluation pipeline using OpenCV and Tesseract to process 20 scanned business documents, applying image preprocessing and benchmarking extraction quality with character and word error rates against labelled ground truth.
