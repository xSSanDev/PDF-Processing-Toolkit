import PyPDF2
#install PyPDF2
def read_metadata(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = pdf_reader.metadata
    print("Metadata of the PDF:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

# Usage
read_metadata('../../metadata_added.pdf')