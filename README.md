# AI-Based Fake Identity and Document Screening System

## Project Overview
This project is a web-based document screening prototype developed using Python and Flask. It uses Optical Character Recognition (OCR) to extract text from uploaded document images and applies rule-based validation to identify missing or incorrectly formatted information.

## Objectives
- Extract text from uploaded document images.
- Identify missing required fields.
- Validate date of birth format and calendar validity.
- Check the demo Document ID format.
- Check whether the name and country fields are empty.
- Display a screening result.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- Tesseract OCR
- Pytesseract
- Pillow

## Features
1. Image upload (PNG, JPG, JPEG).
2. OCR-based text extraction.
3. Required field detection.
4. Name field validation.
5. Date of birth validation.
6. Document ID format validation.
7. Country field validation.
8. Screening result display.

## Project Structure
```text
AI_Document_Screening/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

## How to Run the Project

1. Clone this repository.
2. Install Python.
3. Install Tesseract OCR.
4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

5. Configure the Tesseract OCR executable path in `app.py`.
6. Run the application:

```bash
python app.py
```

7. Open this address in your browser:

```text
http://127.0.0.1:5000
```

## Current Development Status
The initial Flask backend, OCR text extraction, and rule-based validation modules have been implemented and tested using fictional sample documents.

Further development will include database integration, improved interface design, and additional analysis features.

## Disclaimer
This is an academic prototype. Its screening results are indicators for review only and do not establish whether a real identity document is genuine or fraudulent.
