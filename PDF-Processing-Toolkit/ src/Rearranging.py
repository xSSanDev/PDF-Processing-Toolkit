import PyPDF2

def rearrange_pages(input_pdf, output_pdf, page_order):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, "wb") as out:
        pdf_writer.write(out)

    print(f"Pages rearranged and saved to {output_pdf}")

# let's use the function
rearrange_pages('pdf1.pdf', 'rearranged.pdf', [1, 0, 2, 3])