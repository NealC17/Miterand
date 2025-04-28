from .parser import Parser
from .tokenizer import Tokenize
from .generator import Generate
from .python_repl import PythonREPL


def interpret(code):
    repl = PythonREPL()
    output = ''

    # Split code into lines
    lines = code.strip().split('\n')

    expr_lines = []  # buffer for expression lines

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if ':=' in line:
            # Assignment — immediately parse and execute
            tokens = Tokenize(line)
            parser = Parser(tokens)
            ast = parser.parse()
            py_code = Generate(ast)
            result = repl.run(py_code)
            output += result
        else:
            # Not assignment — buffer the expression
            expr_lines.append(line)

    # Instead of joining expressions into one, interpret each separately
    for expr_line in expr_lines:
        tokens = Tokenize(expr_line)
        parser = Parser(tokens)
        ast = parser.parse()
        py_code = Generate(ast)
        result = repl.run(py_code)
        output += result

    output = output.replace("> >", ">\n>")
    return output
