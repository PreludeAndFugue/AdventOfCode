#!python3

'''

https://ruslanspivak.com/lsbasi-part1/
https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python--part-1-

Google search: python simple interpreter

'''

from operator import __add__, __mul__

OPEN_PAREN = 'OPEN_PAREN'
CLOSE_PAREN = 'CLOSE_PAREN'
MUL = 'MUL'
ADD = 'ADD'
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


    def get_next_token(self):
        if self._at_end:
            return Token(EOF, None)
        char = self.text[self.position]
        if char.isdigit():
            self.position += 1
            return Token(INT, int(char))
        elif char == '+':
            self.position += 1
            return Token(ADD, __add__)
        elif char == '*':
            self.position += 1
            return Token(MUL, __mul__)
        elif char == '(':
            self.position += 1
            return Token(OPEN_PAREN, None)
        elif char == ')':
            self.position += 1
            return Token(CLOSE_PAREN, None)
        elif char == ' ':
            self.position += 1
            return self.get_next_token()
        else:
            raise Exception(f'Invalid token: {repr(char)}')


    @property
    def _at_end(self):
        return self.position >= len(self.text)


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()


    def expr(self):
        '''
        expr: term (MUL term)*
        term: factor (ADD factor)*
        factor: INT | OPEN_PAREN expr CLOSE_PAREN
        '''
        result = self.term()
        while self.current_token.type == MUL:
            token = self.current_token
            self.eat(MUL)
            operator = token.value
            result = operator(result, self.term())
        return result


    def term(self):
        '''
        term: factor (ADD factor)*
        '''
        result = self.factor()
        while self.current_token.type == ADD:
            token = self.current_token
            self.eat(ADD)
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
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Eat error: {self.current_token}, type: {token_type}')



def test():
    l = Lexer('((3 + 2) * 4) + (3 + 1)')
    tokens = [l.get_next_token() for _ in range(10)]
    print(tokens)


def main():
    # test()

    l = Lexer('1 + 2 * 3')
    i = Interpreter(l)
    n = i.expr()
    print(n)


if __name__ == "__main__":
    main()
