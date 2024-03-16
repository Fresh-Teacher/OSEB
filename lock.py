import PyPDF2

def encrypt_pdf(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                           use_128bit=True)
        
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_file = "OSEB CHARGES.pdf"
    output_pdf_file = "OSEB CHARGES_locked.pdf"
    password = "12345"
    
    encrypt_pdf(input_pdf_file, output_pdf_file, password)
    print(f"PDF locked and saved as: {output_pdf_file}")
