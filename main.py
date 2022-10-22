import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main-page.html')

@app.route('/info-page')
def info_page():
    return render_template('info-page.html')

@app.route('/secret-page', methods=['post', 'get'])
def secret_page():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'qwerty':
            return render_template('contents-page.html')
    return render_template('secret-page.html')

@app.route('/contents-page')
def contents_page():
    return render_template('contents-page.html')

@app.route('/developer-page')
def developer_page():
    return render_template('developer-page.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

