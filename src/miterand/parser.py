class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Lambda:
    def __init__(self, param, body):
        self.param = param
        self.body = body


class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Variable:
    def __init__(self, name):
        self.name = name


class Number:
    def __init__(self, value):
        self.value = int(value)


class Call:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def match(self, kind):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == kind:
            val = self.tokens[self.pos][1]
            self.pos += 1
            return val
        raise SyntaxError(f"Expected {kind}, got {self.tokens[self.pos]}")

    def peek(self):
        return self.tokens[self.pos][0] if self.pos < len(self.tokens) else None

    def parse(self):
        if self.peek() is None:
            return None

        if self.peek() == 'IDENT':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'ASSIGN':
                return self.assignment()
            else:
                return self.expr()
        else:
            return self.expr()

    def assignment(self):
        name = self.match('IDENT')
        self.match('ASSIGN')
        value = self.lambda_expr()
        return Assignment(name, value)

    def lambda_expr(self):
        self.match('LAMBDA')
        param = self.match('IDENT')
        self.match('DOT')
        body = None
        # Handle chained lambdas automatically
        if self.peek() == 'LAMBDA':
            body = self.lambda_expr()
        else:
            body = self.expr()
        return Lambda(param, body)

    def expr(self):
        return self.parse_addition()

    def parse_addition(self):
        expr = self.parse_application()
        while self.peek() == 'PLUS':
            self.match('PLUS')
            right = self.parse_application()
            expr = BinaryOp('+', expr, right)
        return expr

    def parse_application(self):
        expr = self.parse_atom()

        while self.peek() in ('IDENT', 'NUMBER', 'LPAREN'):
            arg = self.parse_atom()
            expr = Call(expr, arg)

        return expr

    def parse_atom(self):
        if self.peek() == 'LPAREN':
            self.match('LPAREN')
            expr = self.expr()
            self.match('RPAREN')
            return expr
        elif self.peek() == 'IDENT':
            return Variable(self.match('IDENT'))
        elif self.peek() == 'NUMBER':
            return Number(self.match('NUMBER'))
        else:
            raise SyntaxError("Invalid atom")
