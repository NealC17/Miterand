from .parser import Assignment, Lambda, BinaryOp, Variable, Number, Call


def Generate(node):
    if isinstance(node, Assignment):
        return f"{node.name} = {Generate(node.value)}"
    elif isinstance(node, Lambda):
        return f"lambda {node.param}: {Generate(node.body)}"
    elif isinstance(node, BinaryOp):
        return f"({Generate(node.left)} {node.op} {Generate(node.right)})"
    elif isinstance(node, Variable):
        return node.name
    elif isinstance(node, Number):
        return str(node.value)
    elif isinstance(node, Call):
        return f"{Generate(node.func)}({Generate(node.arg)})"
