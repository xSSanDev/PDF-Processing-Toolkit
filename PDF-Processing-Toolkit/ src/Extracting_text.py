import pdfplumber

def extract_text(pfd_path, output_text_path):
    with pdfplumber.open(pfd_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'

    with open(output_text_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Extracted text is saved as {output_text_path}")

# let's use the function
extract_text('../../pdf1.pdf', 'output1.txt')