from PIL import Image
from io import BytesIO

def jpg_to_pdf(file_bytes):
    """
    Converts a JPEG image to a PDF file.

    Args:
        file_bytes (bytes): The content of the JPEG file.

    Returns:
        bytes: The content of the PDF file as bytes.
    """
    image = Image.open(BytesIO(file_bytes))
    pdf_bytes = BytesIO()
    image.save(pdf_bytes, format='PDF')
    pdf_bytes.seek(0)
    return pdf_bytes.getvalue()
