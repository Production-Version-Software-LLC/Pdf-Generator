from flask import Flask, request, render_template_string, send_file
from weasyprint import HTML
import io

app = Flask(__name__)


@app.route('/json-to-pdf', methods=['POST'])
def json_to_pdf():
    data = request.get_json()

    # JSON parametrelerini işlemek için dinamik HTML şablonu oluşturma
    html_template = """
    <html>
    <head>
        <title>Dynamic PDF Report</title>
        <style>
            table {
                width: 100%%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <h1>Report for {{ userName or 'Unknown User' }}</h1>
        <p><strong>Timestamp:</strong> {{ timestamp or 'Not provided' }}</p>
        <p><strong>Template Name:</strong> {{ pdfTemplateName or 'Default Template' }}</p>

        <h2>Parameters</h2>
        <p><strong>Label 1:</strong> {{ params.label1 }}</p>

        <h3>Table 1 Data:</h3>
        <table>
            <thead>
                <tr>
                    <th>Column 1</th>
                    <th>Column 2</th>
                </tr>
            </thead>
            <tbody>
            {% for row in params.table1 %}
                <tr>
                    <td>{{ row.col1 }}</td>
                    <td>{{ row.col2 }}</td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """

    # Şablonu JSON verisi ile dolduruyoruz
    rendered_html = render_template_string(html_template, **data)

    # HTML'yi PDF'ye dönüştürüyoruz
    pdf_file = HTML(string=rendered_html).write_pdf()

    # PDF dosyasını indirilmek üzere döndürüyoruz
    return send_file(io.BytesIO(pdf_file), attachment_filename='dynamic_report.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
