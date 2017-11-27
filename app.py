from flask import Flask, render_template, request
from transition_table import table
from simple_url_parser import SimpleUrlParser
from simple_url_lexer import SimpleUrlLexer

app = Flask(__name__)
lexer = SimpleUrlLexer()
lexer.build()


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/parse", methods=['POST'])
def parse():
    q = request.form.get('q', default="", type=str)

    lexer.lexical_analysis1(q)

    parser = SimpleUrlParser(lexer.output)
    parser.parse()

    return render_template(
        'parse.html',
        q=q,
        data=parser.output
    )