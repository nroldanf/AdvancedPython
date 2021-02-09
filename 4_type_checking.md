# Type Checking

Python is a Dynamic Typing language, no type have to be declared and all types are checked in runtime.

Type hints help the IDE to warn about type checking on input params and return values. This is totally optional, the interpreter will ignore the type hints added.

## mypy (Defacto standard type checker)

Commandline type checker. This works for Python 3.6 or newer.

- Can be installed with:

```shell
pip install mypy
```

## Incorporing type hints

- Type hints are allowed for Python built-in objects and custom instances of classes.
- PEP-484 and mypy for extended reference.
- TYpe checking can be seen as a kind of documentation, that allows easier ways to maintain the code.
- Totally ptional.
