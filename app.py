from flask import Flask, request, send_file, render_template, jsonify
from werkzeug.utils import secure_filename
from io import BytesIO

from conversions.docx_converter import doc_to_pdf
from conversions.excel_converter import excel_to_pdf
from conversions.ppt_converter import ppt_to_pdf
from conversions.jpg_converter import jpg_to_pdf
from conversions.html_converter import html_to_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/htmltopdf', methods=['POST'])
def convert_html_to_pdf():
    file = request.files.get('file')
    url = request.form.get('url')
    
    if file:
        filename = secure_filename(file.filename)
        file_bytes = file.read()
        pdf_bytes = html_to_pdf(file_bytes, is_url=False)
        return send_file(BytesIO(pdf_bytes), download_name=f"{filename}.pdf", as_attachment=True)
    elif url:
        pdf_bytes = html_to_pdf(url, is_url=True)
        return send_file(BytesIO(pdf_bytes), download_name="converted_from_url.pdf", as_attachment=True)
    else:
        return jsonify({"error": "No file or URL provided"}), 400

@app.route('/wordtopdf', methods=['POST'])
def convert_word_to_pdf():
    return handle_conversion(doc_to_pdf, 'docx')

@app.route('/exceltopdf', methods=['POST'])
def convert_excel_to_pdf():
    return handle_conversion(excel_to_pdf, 'xlsx')

@app.route('/ppttopdf', methods=['POST'])
def convert_ppt_to_pdf():
    return handle_conversion(ppt_to_pdf, 'pptx')

@app.route('/jpgtopdf', methods=['POST'])
def convert_jpg_to_pdf():
    return handle_conversion(jpg_to_pdf, 'jpg')

def handle_conversion(conversion_function, file_type):
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "Missing file"}), 400

    filename = secure_filename(file.filename)
    file_bytes = file.read()

    pdf_bytes = conversion_function(file_bytes)

    return send_file(BytesIO(pdf_bytes), download_name=f"{filename}.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
