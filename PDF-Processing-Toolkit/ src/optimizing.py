import fitz # PyMuPDF

def optimize_pdf(input_pdf, output_pdf):
    pdf_document = fitz.open(input_pdf)
    pdf_document.save(output_pdf, garbage=3, deflate=True)
    print(f"Optimized PDF saved as {output_pdf}")

# let's use the function
optimize_pdf('merged.pdf', 'optimize.pdf')