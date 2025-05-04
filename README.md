# Hindi & Sanskrit PDF OCR

Extracts text from scanned Hindi/Sanskrit PDFs using Tesseract OCR.

## Features

- Converts PDF pages to images using `pdf2image`
- OCR support for Hindi + Sanskrit (`hin+san`)
- Works on macOS

## Requirements

- Python 3.x
- `pytesseract`, `pdf2image`
- Poppler (must be installed and in PATH)

## Install dependencies:
```bash
pip install pytesseract pdf2image

## Usage:
python hindi_sanskrit_ocr.py

## You'll be prompted to enter:
Input PDF filename
Output TXT filename

Written by Arush Kotta
