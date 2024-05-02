import pdfplumber
import csv

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_csv(text, csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        for line in text.split("\n"):
            csv_writer.writerow([line])

pdf_path = "/Volumes/ADATA/Documents/ATO/Tax22-23/BOQStatement.pdf"
csv_path = "/Volumes/ADATA/Documents/ATO/Tax22-23/BOQStatement.csv"

text = extract_text_from_pdf(pdf_path)
save_text_to_csv(text, csv_path)
