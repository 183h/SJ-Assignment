class SimpleUrlParser(object):
    def __init__(self, output_lexer):
        self.output_lexer = output_lexer
        self.non_terminals = [
            "url", "httpaddress", "httpaddress1", "httpaddress2", "ftpaddress",
            "telnetaddress", "mailtoaddress", "login", "login1", "hostport",
            "hostport1", "hostname", "hostname1", "port", "path", "path1", "search",
            "search1", "user", "password", "segment", "xalphas", "xalphas1",
            "xalpha", "digits", "digits1", "alpha", "digit"
        ]