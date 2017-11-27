from __future__ import print_function
from transition_table import table
from simple_url_lexer import SimpleUrlLexer
from re import sub


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
        self.alphas = [
            "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
            "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S",
            "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"
        ]
        self.digits = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        ]
        self.error_position = []

    def parse(self):
        stack = ["$"]
        if self.output_lexer[0].value in table["url"]:
            rule = table["url"][self.output_lexer[0].value].split(' ')

            for i in rule[::-1]:
                stack.append(i)
        else:
            self.error_position.append(self.output_lexer[0])
            return 0

        index = 0
        while True:
            last_stack = stack.pop()

            # non-terminal
            if last_stack in self.non_terminals:
                if self.output_lexer[index].value in self.alphas:
                    token_value = "A-Z a-z"
                    if token_value in table[last_stack]:
                        rule = table[last_stack][token_value]

                        if rule == "A | .. | Z | a | .. | z":
                            stack.append(self.output_lexer[index].value)
                        else:
                            rule = rule.split(' ')
                            # print("rule", rule)

                            if "epsilon" not in rule:
                                for i in rule[::-1]:
                                    stack.append(i)
                    else:
                        self.error_position.append(self.output_lexer[index])
                        index = index + 1
                        stack.append(last_stack)

                elif self.output_lexer[index].value in self.digits:
                    token_value = "0 .. 9"
                    if token_value in table[last_stack]:
                        rule = table[last_stack][token_value]

                        if rule == "0 | .. | 9":
                            stack.append(self.output_lexer[index].value)
                        else:
                            rule = rule.split(' ')
                            # print("rule", rule)

                            if "epsilon" not in rule:
                                for i in rule[::-1]:
                                    stack.append(i)
                    else:
                        self.error_position.append(self.output_lexer[index])
                        index = index + 1
                        stack.append(last_stack)

                elif self.output_lexer[index].value in table[last_stack]:
                    rule = table[last_stack][self.output_lexer[index].value].split(' ')
                    # print("rule", rule)

                    if "epsilon" not in rule:
                        for i in rule[::-1]:
                            stack.append(i)
                else:
                    self.error_position.append(self.output_lexer[index])
                    index = index + 1
                    stack.append(last_stack)

            # terminal
            else:
                if self.output_lexer[index].value == last_stack:
                    if self.output_lexer[index].value != "$":
                        index = index + 1
                    else:
                        if last_stack == "$":
                            return 1
                        else:
                            self.error_position.append(self.output_lexer[index])
                            index = index + 1
                            stack.append(last_stack)
                else:
                    self.error_position.append(self.output_lexer[index])
                    index = index + 1
                    stack.append(last_stack)

            # for i in self.output_lexer[index:]:
            #     print(i.value, end='')
            # print ("\nstack", stack)
            # print(self.error_position)

if __name__ == '__main__':
    lexer = SimpleUrlLexer()
    lexer.build()

    file = open('/home/pukes/Projects/SJ/SJ-Assignment/subor', 'r')
    lexer.lexical_analysis(file)

    parser = SimpleUrlParser(lexer.output)
    parser.parse()
