from flask import Flask, request, render_template_string, send_file
from weasyprint import HTML
import io

app = Flask(__name__)
@app.route('/json-to-pdf', methods=['POST'])
def json_to_pdf():
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


if __name__ == '__main__':
    app.run(debug=True)
