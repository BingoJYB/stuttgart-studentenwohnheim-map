from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('index.html', name='John')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
