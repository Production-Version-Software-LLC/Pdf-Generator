import traceback

from flask import Flask, request, render_template_string, send_file, jsonify
from weasyprint import HTML
import io

app = Flask(__name__)
@app.route('/json-to-pdf', methods=['POST'])
def json_to_pdf():
    try:
        data = request.get_json()

        # html.html dosyasını oku
        with open('html_template.html', 'r', encoding='utf-8') as dosya:
            html_template1 = dosya.read()


        # JSON parametrelerini işlemek için dinamik HTML şablonu oluşturma


        # Şablonu JSON verisi ile dolduruyoruz
        rendered_html = render_template_string(html_template1, **data)

        # HTML'yi PDF'ye dönüştürüyoruz
        pdf_file = HTML(string=rendered_html).write_pdf()

        # PDF dosyasını indirilmek üzere döndürüyoruz
        return send_file(io.BytesIO(pdf_file), download_name='dynamic_report.pdf', as_attachment=True)
    except Exception as e:
        # Capture and log the stack trace
        stack_trace = traceback.format_exc()
        app.logger.error("request error %s",request,e,stack_trace)

        # Return a JSON response with the stack trace and error message
        return jsonify({
            "error": str(e),
            "stackTrace": stack_trace
        }), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
