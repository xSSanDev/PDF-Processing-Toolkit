import PyPDF2


def encrypt_pdf(input_pdf, output_pdf, password):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(password)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"Encrypted PDF saved as {output_pdf}")

# let's use the function
encrypt_pdf('merged.pdf', 'encrypted.pdf', 'xSSanDev')