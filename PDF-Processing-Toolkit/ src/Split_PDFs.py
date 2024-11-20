import PyPDF2
# install PyPDF2 using pip install PyPDF2
def split_pdf(pdf_path, output_dir):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_page = f"{output_dir}/page_{page_num + 1}.pdf"

        with open(output_page, 'wb') as out:
            pdf_writer.write(out)
        print(f"saved {output_page}")

#let's use the function
split_pdf('[pdf path]', '[output directory]')