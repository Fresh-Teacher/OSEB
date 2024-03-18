import os
import PyPDF2
from docx import Document

def text_to_hex(text):
    return ''.join(hex(ord(char))[2:].upper() for char in text)

def encrypt_pdf(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def lock_docx(input_docx, output_docx, password):
    doc = Document(input_docx)
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = None  # Remove any existing font color
            run.font.highlight_color = None  # Remove any existing highlight color
            run.font.bold = True  # Make the text bold
            run.font.size = run.font.size  # Preserve original font size
    doc.save(output_docx)

def lock_files_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            filename, file_extension = os.path.splitext(file)

            # Convert filename to hexadecimal
            hex_value = text_to_hex(filename)
            password = hex_value.upper()  # Convert to uppercase

            if file_extension.lower() == ".pdf":
                encrypt_pdf(file_path, file_path, password)
                print(f"Locked {file} with the password: {password}")

            elif file_extension.lower() == ".docx":
                lock_docx(file_path, file_path, password)
                print(f"Locked {file} with the password: {password}")

if __name__ == "__main__":
    folder_to_lock = "files"
    lock_files_in_folder(folder_to_lock)
    print("All files locked successfully.")
