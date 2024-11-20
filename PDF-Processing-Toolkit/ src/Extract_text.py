import pdfplumber
#install pdfplumber using pip install pdfplumber
def extract_text(pfd_path, output_text_path):
    with pdfplumber.open(pfd_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'

    with open(output_text_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Extracted text is saved as {output_text_path}")

# let's use the function
# remove [] and add the required values
extract_text('[pdf path]', '[output text path]')