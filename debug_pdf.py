import pypdf
import os

# Path to the second sample PDF
sample_pdf = r"1287/test.pdf"

try:
    reader = pypdf.PdfReader(sample_pdf)
    print(f"Number of pages: {len(reader.pages)}")
    for i, page in enumerate(reader.pages):
        print(f"--- Page {i+1} ---")
        print(page.extract_text())
except Exception as e:
    print(f"Error reading PDF: {e}")
