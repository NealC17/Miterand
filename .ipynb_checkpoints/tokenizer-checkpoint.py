import re


def Tokenize(code):
    tokens = []
    token_spec = [
        ('NUMBER',  r'\d+'),
        ('LAMBDA',  r'L'),
        ('IDENT',   r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('ASSIGN',  r':='),
        ('DOT',     r'\.'),
        ('LPAREN',  r'\('),
        ('RPAREN',  r'\)'),
        ('PLUS',    r'\+'),
        ('SKIP',    r'[ \t]+'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP':
            tokens.append((kind, value))
    return tokens



