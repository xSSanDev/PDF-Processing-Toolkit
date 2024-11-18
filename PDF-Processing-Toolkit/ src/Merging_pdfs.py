import PyPDF2

def merge_pdfs(pdf_list, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page (pdf_reader.pages[page_num])
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved as {output_pdf}")

#let's use the function
merge_pdfs(['pdf1.pdf', 'pdf2.pdf'], 'merged.pdf')