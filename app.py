from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/parse", methods=['POST'])
def parse():
    q = request.form.get('q', default="", type=str)

    return render_template(
        'parse.html',
        q=q
    )