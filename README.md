## Design

### Architecture

The PDF Processing Toolkit is designed with modular scripts, each responsible for a specific PDF manipulation task. The main components are:

- `merge_pdfs.py`: Merges multiple PDF files into one.
- `add_metadata.py`: Adds metadata to a PDF file.
- `read_metadata.py`: Reads metadata from a PDF file.
- `extract_images.py`: Extracts images from a PDF file.
- `rearrange_pages.py`: Rearranges pages in a PDF file.
- `rotate_pages.py`: Rotates pages in a PDF file.
- `optimize_pdf.py`: Optimizes a PDF file for size.

### Flow

1. **Input**: The user provides the necessary input files and parameters.
2. **Processing**: The respective script processes the input as per the user's request.
3. **Output**: The processed PDF file is saved to the specified output location.

### Diagrams

#### Component Diagram

![Component Diagram](path/to/component-diagram.png)

#### Flow Diagram

![Flow Diagram](path/to/flow-diagram.png)