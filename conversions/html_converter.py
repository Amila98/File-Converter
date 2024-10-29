import pdfkit
import requests
from io import BytesIO

def html_to_pdf(content, is_url=False):
    if is_url:
        # Fetch HTML content from URL
        response = requests.get(content)
        if response.status_code == 200:
            html_content = response.text
        else:
            raise ValueError("Unable to fetch HTML content from URL")
    else:
        html_content = content.decode('utf-8')

    pdf = pdfkit.from_string(html_content, False)
    return pdf
