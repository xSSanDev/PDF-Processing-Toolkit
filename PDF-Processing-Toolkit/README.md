# PDF Processing Toolkit

This project includes scripts to merge PDFs, add metadata, read metadata, extract images, rearrange pages, rotate pages, and optimize PDFs.

## Features

- Merge PDFs
- Add metadata to PDFs
- Read metadata from PDFs
- Extract images from PDFs
- Rearrange pages in PDFs
- Rotate pages in PDFs
- Optimize PDFs

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/AnassZr23/PDF-Processing-Toolkit.git
   cd PDF-Processing-Toolkit
2. Create a virtual environment:
   ```sh
   python -m venv venv
3. Activate the virtual environment:
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
5. Run the tests to ensure everything is set up correctly:
   ```sh
   pytest
  6. (Optional) Install additional development dependencies:
   ```sh
   pip install -r dev-requirements.txt