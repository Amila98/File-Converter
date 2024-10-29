import subprocess
import os
import tempfile

def doc_to_pdf(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_input:
        temp_input.write(file_bytes)
        input_path = temp_input.name

    output_path = input_path.replace('.docx', '.pdf')
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', os.path.dirname(output_path), input_path], check=True)

    with open(output_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    os.remove(input_path)
    os.remove(output_path)

    return pdf_bytes
