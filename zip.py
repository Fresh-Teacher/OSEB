import os
import zipfile
from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def zip_folder_with_password(folder_path, zip_path, password):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    encrypted_pdf_path = os.path.join(root, f"{os.path.splitext(file)[0]}_locked.pdf")
                    encrypt_pdf(file_path, encrypted_pdf_path, password)
                    zip_file.write(encrypted_pdf_path, arcname=os.path.basename(encrypted_pdf_path))

if __name__ == "__main__":
    folder_to_lock = "files"
    output_zip_file = "locked_pdfs.zip"
    password = "12345"
    
    zip_folder_with_password(folder_to_lock, output_zip_file, password)
    print(f"Locked PDFs zipped and saved as: {output_zip_file}")
