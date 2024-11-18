import PyPDF2

def rotate_pages(input_pdf, output_pdf, rotation):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.rotate(rotation)
        pdf_writer.add_page(page)

    with open(output_pdf, "wb") as out:
        pdf_writer.write(out)

    print(f"Pages rotated and saved to {output_pdf}")

# let's use the function
rotate_pages('pdf1.pdf', 'rotated.pdf', 180)