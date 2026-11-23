# Scanned Document OCR Benchmark using Python and Tesseract

## 1. Project Overview

The **Scanned Document OCR Benchmark** is a Python-based Optical Character Recognition (OCR) project that extracts text from scanned business documents using the open-source Tesseract OCR engine.

The project processes 20 scanned documents, including invoices and purchase orders, using OpenCV for image preprocessing and Pytesseract for text extraction.

OCR performance is evaluated by comparing extracted text against manually prepared ground-truth transcripts using Character Error Rate (CER) and Word Error Rate (WER).

### Key Objectives

- Extract text from scanned business documents.
- Improve image quality through preprocessing techniques.
- Automate OCR using an open-source OCR engine.
- Evaluate extraction accuracy against labelled ground-truth data.
- Generate measurable evaluation reports.

## 2. Project Highlights

- Processed 20 scanned business documents.
- Implemented image preprocessing using OpenCV.
- Integrated Tesseract OCR with Python.
- Implemented Character Error Rate (CER) and Word Error Rate (WER).
- Generated document-level and aggregate evaluation reports.
- Created automated unit tests using Pytest.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tesseract OCR | Text recognition engine |
| Pytesseract | Python integration for OCR |
| OpenCV | Image preprocessing |
| NumPy | Image processing operations |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## 4. Dataset Description

The project uses a controlled dataset containing 20 scanned-style business documents.

| Document Type | Number of Documents |
|---|---:|
| Invoices | 10 |
| Purchase Orders | 10 |
| **Total** | **20** |

Each scanned image has a corresponding ground-truth text file used for evaluation.

Dataset directories:

- `data/scanned/` – Contains scanned document images.
- `data/ground_truth/` – Contains reference text files.

The dataset includes printed English text, minor image noise and small rotation variations.

## 5. System Architecture

The OCR pipeline follows these steps:

1. **Image Loading:** Load scanned document images using OpenCV.
2. **Grayscale Conversion:** Convert images into grayscale.
3. **Image Resizing:** Increase image resolution to improve text recognition.
4. **Noise Reduction:** Apply Gaussian blur to reduce image noise.
5. **Adaptive Thresholding:** Improve text and background contrast.
6. **Text Extraction:** Extract text using Tesseract OCR.
7. **Accuracy Evaluation:** Compare extracted text against ground-truth transcripts.
8. **Report Generation:** Generate evaluation results in CSV and JSON formats.

## 6. OCR Evaluation Results

The OCR pipeline was evaluated on all 20 scanned documents.

| Evaluation Metric | Result |
|---|---:|
| Documents Evaluated | 20 |
| Character Error Rate (CER) | 1.32% |
| Word Error Rate (WER) | 3.90% |
| Character Accuracy | 98.68% |
| Word Accuracy | 96.10% |

### Understanding the Metrics

**Character Error Rate (CER)**

Measures character-level differences between extracted text and reference text.

CER = Character Edit Distance / Total Reference Characters

**Word Error Rate (WER)**

Measures word-level differences between extracted text and reference text.

WER = Word Edit Distance / Total Reference Words

**Character Accuracy**

Character Accuracy = 1 - CER

**Word Accuracy**

Word Accuracy = 1 - WER

### Results Interpretation

The OCR pipeline achieved 98.68% character accuracy and 96.10% word accuracy on the controlled dataset.

These results demonstrate the effectiveness of the implemented preprocessing and OCR pipeline on the included document images. Performance may vary on real-world documents with handwriting, poor scan quality, complex layouts or different fonts.

## 7. Project Structure

```text
ocr_document_intelligence/
│
├── data/
│   ├── scanned/
│   │   ├── doc_01.png
│   │   ├── doc_02.png
│   │   └── ... doc_20.png
│   │
│   └── ground_truth/
│       ├── doc_01.txt
│       ├── doc_02.txt
│       └── ... doc_20.txt
│
├── src/
│   └── doc_ocr/
│       ├── __init__.py
│       ├── pipeline.py
│       └── cli.py
│
├── tests/
│   └── test_metrics.py
│
├── reports/
│   ├── evaluation.csv
│   └── metrics.json
│
├── README.md
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

## 8. Installation and Setup

### Prerequisites

- Python 3.9 or later
- Visual Studio Code
- Tesseract OCR
- Git

### Step 1: Install Tesseract OCR

Download and install Tesseract OCR for Windows:

https://github.com/UB-Mannheim/tesseract/wiki

Add the installation directory to Windows PATH:

```text
C:\Program Files\Tesseract-OCR
```

Verify installation:

```bash
tesseract --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/scanned-document-ocr-benchmark.git
```

Navigate to the project directory:

```bash
cd scanned-document-ocr-benchmark
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## 9. Execution

### Run OCR on a Single Document

```bash
python -m doc_ocr.cli ocr data/scanned/doc_01.png
```

This command extracts and displays the text from the selected scanned document.

### Evaluate All 20 Documents

```bash
python -m doc_ocr.cli evaluate
```

The evaluation generates:

- `reports/evaluation.csv` – Individual document OCR results and error rates.
- `reports/metrics.json` – Aggregate evaluation metrics.

### Run Automated Tests

```bash
pytest -q
```

The tests validate:

- Character Error Rate calculation.
- Word Error Rate calculation.
- Text normalisation.
- Edit distance calculation.

## 10. Output and Reports

The project generates structured evaluation reports.

**evaluation.csv**

Contains:
- Document filename.
- Character Error Rate.
- Word Error Rate.
- Reference character count.
- Reference word count.
- Extracted OCR text.

**metrics.json**

Contains:
- Total documents evaluated.
- Aggregate CER.
- Aggregate WER.
- Character accuracy.
- Word accuracy.

## 11. Limitations and Future Enhancements

Potential improvements include:

- Support for multi-page PDF documents.
- Automatic document orientation correction.
- Advanced image deskewing.
- Support for multilingual OCR.
- Structured information extraction from invoices.
- Comparison of Tesseract with EasyOCR or PaddleOCR.
- Evaluation on publicly available real-world scanned-document datasets.
- Integration with a database for storing extracted document information.

## 12. Skills Demonstrated

- Python Programming
- Optical Character Recognition (OCR)
- Computer Vision
- Image Preprocessing
- OpenCV
- Tesseract OCR
- Data Validation
- Model Evaluation
- Error Rate Analysis
- Unit Testing
- Git and GitHub



---

*This project was developed as a practical demonstration of OCR automation, computer vision and quantitative evaluation using open-source Python libraries.*
