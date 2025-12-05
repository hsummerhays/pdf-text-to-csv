import os
import csv
import re
import pypdf
import multiprocessing
from functools import partial

def process_file(file_info):
    root_dir, file_path, filename = file_info
    
    # Extract Batch ID
    rel_path = os.path.relpath(os.path.dirname(file_path), root_dir)
    parts = rel_path.split(os.sep)
    batch_id = parts[0] if parts else "Unknown"
    
    # Extract Artist ID
    artist_id_match = re.search(r'\b(\d{3,4})\b', filename)
    artist_id = artist_id_match.group(1) if artist_id_match else "Unknown"
    
    # Extract Total
    total = "0.00"
    try:
        reader = pypdf.PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        # Pattern 1: Total Due: $xxx
        total_match = re.search(r'Total Due:\s*\$?([\d,]+\.\d{2})', text, re.IGNORECASE)
        if total_match:
            total = total_match.group(1)
        else:
            # Pattern 1b: $xxx Total Due
            total_match_b = re.search(r'\$?([\d,]+\.\d{2})\s*Total Due', text, re.IGNORECASE)
            if total_match_b:
                total = total_match_b.group(1)
            else:
                # Pattern 2: Amount: $xxx
                amount_match = re.search(r'Amount:\s*\$?([\d,]+\.\d{2})', text, re.IGNORECASE)
                if amount_match:
                    total = amount_match.group(1)
    except Exception as e:
        # print(f"Error reading {filename}: {e}")
        total = "Error"
        
    return [artist_id, batch_id, total, filename]

def get_files(root_dir):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                file_list.append((root_dir, os.path.join(dirpath, filename), filename))
    return file_list

def main():
    root_dir = "pdf_files_to_scan"
    output_file = "output.csv"
    
    print("Scanning files...")
    files = get_files(root_dir)
    print(f"Found {len(files)} files. Starting extraction with {multiprocessing.cpu_count()} processes...")
    
    with multiprocessing.Pool() as pool:
        results = pool.map(process_file, files)
        
    print("Writing results...")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Artist ID', 'Batch ID', 'Total', 'Filename'])
        writer.writerows(results)
    
    print(f"Extraction complete. Saved to {output_file}")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
