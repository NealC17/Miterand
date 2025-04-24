class Assignment: pass
class Lambda: pass
class BinaryOp: pass
class Variable: pass
class Number: pass

class Assignment:
    def __init__(self, name, value): self.name, self.value = name, value
class Lambda:
    def __init__(self, param, body): self.param, self.body = param, body
class BinaryOp:
    def __init__(self, op, left, right): self.op, self.left, self.right = op, left, right
class Variable:
    def __init__(self, name): self.name = name
class Number:
    def __init__(self, value): self.value = int(value)

# Parser class
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
        return self.assignment()

    def assignment(self):
        name = self.match('IDENT')
        self.match('ASSIGN')
        value = self.lambda_expr()
        return Assignment(name, value)

    def lambda_expr(self):
        self.match('LAMBDA')
        param = self.match('IDENT')
        self.match('DOT')
        body = self.expr()
        return Lambda(param, body)

    def expr(self):
        if self.peek() == 'LPAREN':
            self.match('LPAREN')
            left = self.expr()
            op = self.match('PLUS')
            right = self.expr()
            self.match('RPAREN')
            return BinaryOp(op, left, right)
        elif self.peek() == 'IDENT':
            return Variable(self.match('IDENT'))
        elif self.peek() == 'NUMBER':
            return Number(self.match('NUMBER'))
        else:
            raise SyntaxError("Invalid expression")
