import os
from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/confirm')
def confirm():
    product = {
        "name": "NVIDIA フィジカルAI 戦略分析レポート（2026年5月版）",
        "price": "2,000",
        "id": "nv-001"
    }
    return render_template('confirm.html', product=product)

@app.route('/dummy_pay', methods=['POST'])
def dummy_pay():
    return render_template('success.html')

@app.route('/download')
def download_file():
    path = "files/sample_report.pdf"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
