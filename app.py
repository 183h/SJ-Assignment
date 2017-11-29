from flask import Flask, render_template, request
from simple_url_parser import SimpleUrlParser
from simple_url_lexer import SimpleUrlLexer
from transition_table import table
from copy import copy

app = Flask(__name__)
lexer = SimpleUrlLexer()
lexer.build()


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/parse", methods=['POST'])
def parse():
    q = request.form.get('q', default="", type=str)

    lexer.simple_input_lexical_analysis(q)

    if lexer.errors:
        qe = copy(q)
        ec = list(set([e.value for e in lexer.errors]))
        for e in ec:
            qe = qe.replace(e, "<mark>" + e + "</mark>")

        return render_template(
            'parse.html',
            q=q,
            result=qe,
            error=[e.lexpos for e in lexer.errors]
        )

    parser = SimpleUrlParser(lexer.output)
    parser.parse(lexer.errors)

    return render_template(
        'parse.html',
        q=q,
        data=parser.output,
        result=parser.result,
        error=[e.lexpos for e in parser.error_position]
    )