# PDF Converter API

This Flask-based API allows you to convert various file formats (HTML, Word, Excel, PowerPoint, and JPG) to PDF. It supports both file upload and URL-based conversions, making it ideal for applications where on-the-fly PDF generation is needed.

## Features

- **HTML to PDF** (via file upload or URL)
- **Word (DOCX) to PDF**
- **Excel (XLSX) to PDF**
- **PowerPoint (PPTX) to PDF**
- **JPG to PDF**

## Requirements

- **Python 3.9+**
- **Docker (optional)** for containerization and deployment.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:5000`.

### Using Docker

1. **Build the Docker image**:
   ```bash
   docker build -t pdf_converter .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 pdf_converter
   ```

   The app will now be accessible on `http://localhost:5000`.

