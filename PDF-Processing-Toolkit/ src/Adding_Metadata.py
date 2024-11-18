#Adding metadata to a PDF file
import PyPDF2

def add_metadata(input_pdf, output_pdf, title, author):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Set the metadata directly using add_metadata
    metadata = {
        '/Title': title,
        '/Author': author,
        '/Producer': ''
    }
    pdf_writer.add_metadata(metadata)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"PDF with added metadata saved as {output_pdf}")
#let's use the function
add_metadata('merged.pdf', 'metadata_added1.pdf', 'Immunolodie Resourses', 'Anass Zeroul')