# PDF Data Extractor

This tool scans a directory of PDF files, extracts specific financial information (Artist ID, Batch ID, and Total Due), and exports the data to a CSV file.

## Features

- **Batch Processing**: Recursively scans the `pdf_files_to_scan` directory for all PDF files.
- **Data Extraction**:
    - **Artist ID**: Extracted from the filename (looking for 3-4 digit numbers).
    - **Batch ID**: Extracted from the parent directory name.
    - **Total Due**: specific patterns like "Total Due: $xxx", "$xxx Total Due", or "Amount: $xxx".
- **Multiprocessing**: utilizes multiple CPU cores for faster processing of large numbers of files.
- **CSV Export**: Saves results to `output.csv`.

## Prerequisites

- Python 3.x
- `pypdf` library

## Installation

1.  Clone this repository or download the files.
2.  Install the required Python library:

    ```bash
    pip install pypdf
    ```

## Usage

1.  **Prepare Files**: Place your PDF files inside the `pdf_files_to_scan` directory.
    -   The script expects a structure where the parent directory of the PDF represents the "Batch ID".
    -   Example: `pdf_files_to_scan/Batch123/1001_Invoice.pdf`

2.  **Run the Script**:

    ```bash
    python extract_pdf_data.py
    ```

3.  **View Results**:
    -   The script will generate an `output.csv` file in the same directory.
    -   The CSV contains: `Artist ID`, `Batch ID`, `Total`, and `Filename`.

## Troubleshooting

If you need to check how the script is reading a specific PDF file, you can use the `debug_pdf.py` script.

1.  Open `debug_pdf.py` and update the `sample_pdf` variable with the path to the PDF you want to test.
2.  Run the debug script:

    ```bash
    python debug_pdf.py
    ```
    -   This will print the text content of each page to the console, helping you identify why a value might not be matching the extraction patterns.

## Project Structure

- `extract_pdf_data.py`: Main script for bulk processing.
- `debug_pdf.py`: Utility script for inspecting single PDF file text.
- `pdf_files_to_scan/`: Input directory for PDF files.
- `output.csv`: Output file containing extracted data.
