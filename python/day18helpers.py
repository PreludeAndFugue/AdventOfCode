#!python3

'''

https://ruslanspivak.com/lsbasi-part1/
https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python--part-1-

Google search: python simple interpreter

'''

from operator import __add__, __mul__

OPEN_PAREN = 'OPEN_PAREN'
CLOSE_PAREN = 'CLOSE_PAREN'
OPERATOR = 'OPERATOR'
INT = 'INT'
EOF = 'EOF'


class Token(object):
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value


    def __repr__(self):
        return f'Token({self.type}, {self.value})'


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.position = 0


    def get_tokens(self):
        tokens = []
        while True:
            token = self._get_next_token()
            tokens.append(token)
            if token.type == EOF:
                break
        return tokens


    def _get_next_token(self):
        if self._at_end:
            return Token(EOF, None)
        char = self.text[self.position]
        if char.isdigit():
            self.position += 1
            return Token(INT, int(char))
        elif char == '+':
            self.position += 1
            return Token(OPERATOR, __add__)
        elif char == '*':
            self.position += 1
            return Token(OPERATOR, __mul__)
        elif char == '(':
            self.position += 1
            return Token(OPEN_PAREN, None)
        elif char == ')':
            self.position += 1
            return Token(CLOSE_PAREN, None)
        elif char == ' ':
            self.position += 1
            return self._get_next_token()
        else:
            raise Exception(f'Invalid token: {repr(char)}')


    @property
    def _at_end(self):
        return self.position >= len(self.text)


class Interpreter(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = tokens[0]


    def expr(self):
        '''expr: factor (OPERATOR factor)*
        '''
        result = self.factor()
        while self.current_token.type == OPERATOR:
            token = self.current_token
            self.eat(OPERATOR)
            operator = token.value
            result = operator(result, self.factor())
        return result


    def factor(self):
        '''factor: INT | OPEN_PAREN expr CLOSE_PAREN
        '''
        token = self.current_token
        if token.type == INT:
            self.eat(INT)
            return token.value
        elif token.type == OPEN_PAREN:
            self.eat(OPEN_PAREN)
            result = self.expr()
            self.eat(CLOSE_PAREN)
            return result


    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self._get_next_token()
        else:
            raise Exception(f'Eat error: {self.current_token}, type: {token_type}')


    def _get_next_token(self):
        self.position += 1
        return self.tokens[self.position]


def main():
    l = Lexer('((3 + 2) * 4) + (3 + 1)')
    tokens = l.get_tokens()
    print(tokens)
    i = Interpreter(tokens)
    n = i.expr()
    print(n)


if __name__ == "__main__":
    main()
