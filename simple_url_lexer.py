import ply.lex as lex


class SimpleUrlLexer(object):
    keywords = (
        'http', 'ftp', 'telnet', 'mailto'
    )

    tokens = keywords + (
        'QUESTION', 'AT', 'DVOJBODKA', 'DOT', 'SLASH', 'PLUS', 'DIGIT', 'NAME'
    )

    # Tokens
    t_QUESTION = r'\?'
    t_AT = r'@'
    t_DVOJBODKA = r':'
    t_DOT = r'.'
    t_SLASH = r'/'
    t_PLUS = r'\+'
    t_DIGIT = r'[0-9][0-9]*'

    # Ignored characters
    t_ignore = ' \t\n'

    def t_NAME(self, t):
        r'[a-zA-Z][a-zA-Z]*'
        if t.value in self.keywords:  # is this a keyword?
            t.type = t.value
        return t

    def t_error(self, t):
        print ("Illegal character {0} at line {1}".format(t.value[0], t.lineno))
        t.lexer.skip(1)

    def build(self, **kwargs):
        self._lexer = lex.lex(module=self, **kwargs)

    def lexical_analysis(self, file):
        print ("Started lexical analysis...")

        for line in file:
            try:
                lex_input = line
            except EOFError:
                break

            self._lexer.input(lex_input)
            while True:
                token = self._lexer.token()
                if not token:
                    break
                print token

        print ("Ended lexical analysis...")

if __name__ == '__main__':
    lexer = SimpleUrlLexer()
    lexer.build()

    file = open('/home/pukes/Projects/SJ/SJ-Assignment/subor', 'r')
    lexer.lexical_analysis(file)
