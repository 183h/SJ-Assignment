import ply.lex as lex


class SimpleUrlLexer(object):
    tokens = (
        'QUESTION', 'AT', 'COLON', 'DOT', 'SLASH', 'PLUS', 'DIGIT', 'NAME', 'HTTP', 'TELNET', 'MAILTO', 'FTP', 'DOLLAR'
    )

    # Tokens
    t_QUESTION = r'\?'
    t_AT = r'@'
    t_COLON = r':'
    t_DOT = r'.'
    t_SLASH = r'/'
    t_PLUS = r'\+'
    t_DIGIT = r'[0-9]'
    t_DOLLAR = r'\$'

    # Ignored characters
    t_ignore = ' \t\n'

    def t_HTTP(self, t):
        r'http://'
        return t

    def t_TELNET(self, t):
        r'telnet://'
        return t

    def t_MAILTO(self, t):
        r'mailto::'
        return t

    def t_FTP(self, t):
        r'ftp://'
        return t

    def t_NAME(self, t):
        r'[a-zA-Z]'
        return t

    def t_error(self, t):
        print ("Illegal character {0} at line {1}".format(t.value[0], t.lineno))
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.output = []
        self._lexer = lex.lex(module=self, **kwargs)

    def lexical_analysis(self, file):
        for line in file:
            try:
                lex_input = line + "$"
            except EOFError:
                break

            self._lexer.input(lex_input)
            while True:
                token = self._lexer.token()
                if not token:
                    break
                self.output.append(token)

if __name__ == '__main__':
    lexer = SimpleUrlLexer()
    lexer.build()

    file = open('/home/pukes/Projects/SJ/SJ-Assignment/subor', 'r')
    lexer.lexical_analysis(file)
