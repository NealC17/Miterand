from parser import Parser
from tokenizer import Tokenize
from generator import Generate

def interpret(code):
    out = ''
    for e in code.split('\n'):
        tokens = Tokenize(e)
        parser = Parser(tokens)
        ast = parser.parse()
        py_code = Generate(ast)
        
        out +=  py_code + '\n' #modify this part to execute

    return out
