# PEP 8 - Python Style Guide

https://pep8.org/

## Code Layout

- Identation: Multiple of 4
- Continuation lines
- Maximum of 79 characters
- 2 lines between top-level functions and classes, 1 line between methods inside a class
- Use of spaces in expressions

## Imports

- Should be in separate lines
- Three groups separated by blank lines:
    - Standard library
    - Third party
    - Local imports

## Naming

- Modules: short, lowercase names
- Classes: CapitalizedNaming
- Functions and methods: lowercase_with_under_scores
- Constants: ALL_CAPS
- Non-public names start with underscore

## Documentation

- Docstrings for all public modules, functions, classes, and methods.

## Tools for styling problems

These command line tools can be used in a CI pipeline, before push check PEP8 conformance, or just to help you format your code for consistency.

- pylint: Can be installed with pip in a Python environment.
- pycodestyle
- black

## pylint

- Generate config file: pyling --generate-rcfile > pylintrc

## black

- No only generates alerts but reformat code.
