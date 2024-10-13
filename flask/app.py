from flask import Flask, request, jsonify, render_template
from modules.generate_qr_code import generate_qr_code

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'status': 'succeed'})


@app.route('/get_qr_code')
def generate_qr():
    url = request.args.get('url', '')
    response_type = request.args.get('response_type', 'json')

    qr_code = generate_qr_code(url)

    if response_type == 'html':
        return render_template('qr_code.html', qr_code=qr_code)
    return jsonify({'qr_code': qr_code})


if __name__ == '__main__':
    app.run(debug=True, port=8001)
