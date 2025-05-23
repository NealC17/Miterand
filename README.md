# Miterand

**Authors:** 
- Haydon Behl
- Neal Chandra

## Overview

Miterand is a minimal toolkit that parses untyped Lambda Calculus expressions and compiles them into executable Python code. It serves both as an educational demonstration of functional programming concepts (α, β, η conversions, currying) and as a lightweight interpreter that can be embedded in Python projects.

## Features & Results

- **Lambda Calculus Support**: Definitions of anonymous functions (`Lx.x`) and multi-argument currying (`Lx.Ly.(x+y)`).
- **Boolean Logic**: Encodes `TRUE`, `FALSE`, and an `IF` combinator purely with functions.
- **Arithmetic Operations**: Supports numeric expressions and nested function calls, e.g., `add(1)(add(2)(3))` evaluates to `6`.
- **Correctness**: Verified through a suite of basic tests (see `basic_tests.ipynb`) showing:
  - Increment and compose: `f := Lx.(x+1)`, `g := Lx.(x+2)`, `g(f(1)) → 4`
  - Arithmetic currying: `add := Lx.Ly.(x+y)`, `add(1)(add(2)(3)) → 6`
  - Boolean logic: `IF TRUE 1 2 → 1`, `IF FALSE 1 2 → 2`.

## Creation Process

1. **Tokenizer (`tokenizer.py`)**
   - Transforms source code into a token sequence: numbers, identifiers, lambda markers (`L`), operators, parentheses.

2. **Parser (`parser.py`)**
   - Implements a recursive-descent parser that builds an AST with nodes:
     - `Assignment`, `Lambda`, `BinaryOp`, `Variable`, `Number`, `Call`.
   - Supports chained lambdas and left-associative application.

3. **Generator (`generator.py`)**
   - Converts AST nodes into valid Python expressions:
     - `Lambda(param, body) → lambda param: <body>`
     - `Call(func, arg) → <func>(<arg>)`
     - Arithmetic and variable references maintain Python syntax.

4. **Interpreter (`interpreter.py`)**
   - Splits source into assignments and expressions.
   - Uses `Tokenize` + `Parser` + `Generate` to get Python code.
   - Executes code in a persistent Python REPL subprocess (`python_repl.py`), capturing output after each prompt.

## Quickstart

1. **Install requirements** (none beyond standard library).
2. **Run basic tests**:
   ```bash
   pip install -r requirements.txt # if any
   jupyter notebook basic_tests.ipynb
   ```
3. **Use `interpret` in your code**:
   ```python
   from miterand.interpreter import interpret

   code = '''
   add := Lx.Ly.(x + y)
   result := add(2)(3)
   result
   '''
   print(interpret(code))  # >>> 5
   ```
   
## Install over PyPI
   ```bash
   pip install miterand
   ```

## Application & Extensions

- **Educational Tool**: Visualize the correspondence between Lambda Calculus and Python lambdas.
- **Prototype Compiler**: Foundation for more advanced functional-to-imperative language compilers.
- **Extensible**: Easily add features—such as multi-argument built-ins, let-bindings, or type-checking—by extending the parser and generator.

## Future Work

- **η‑conversion simplification**: Automatically remove redundant λ-abstractions.
- **Support for recursion**: Add fixed-point combinators (e.g., `Y` combinator).
- **Error Handling**: Better syntax error messages with line/column annotations.
- **Optimizations**: Inline small lambdas and apply α-renaming to avoid variable capture.

---

*Miterand bridges the gap between theoretical functional programming and practical Python execution.*

