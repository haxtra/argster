# argster

Short and sweet command line argument parser for Python. Designed for direct script embedding.


## Features

- command based interface
- command aliases (shorthands)
- flags / options
- flag grouping
- argument aliases
- small: 979b / 38 loc w/o comments


## Usage

### Basic

```python
# app.py
import argster
from sys import argv

args = argster.parse(argv[1:])
print(args)

# alternatively:
# from argster import argster
# args = argster(argv[1:])
```
Result
```console
$ app.py cmd -abc=3 -d=4 --foo --bar=baz

{
    '$': ['cmd'],
    'a': True,
    'b': True,
    'c': '3',
    'd': '4',
    'foo': True,
    'bar': 'baz'
}
```

### Commands

Arguments that do not start with `-` are recognized as commands, or free values, and stored in `$` sublist (see below).


### Aliases and defaults

- aliases and defaults are set in one go using dict as a second param
- flags (options without a value ie `-f` or `--foo`) always evaluate to `True`
- defaults are only used in absence of a param
- commands don't use default values and should be set to `None`

```python
args = argster.parse(sys.argv[1:], {
    # short|long: default
    'cmd|command': None,
    'sub|subcommand': None,
    'f|foo': 'fail',
    'b|bar': False,
    'l|leet': 1337,
})
```
Result
```console
$ app.py cmd sub -f -b=baz

{
    '$': ['command', 'subcommand'],
    'foo': True,
    'bar': 'baz',
    'leet': 1337
}
```

## Cheatsheet

```
cmd      -- command
-a       -- a=True
-a=1     -- a="1"
-abc     -- a=True, b=True, c=True
-abc=3   -- a=True, b=True, c="3"
--opt    -- opt=True
--opt=3  -- opt="3"
-x       -- when aliased => expanded=True
```

## Direct embedding

Minified version is provided in `argster-min.py` file, which has comments and empty lines removed.


## Limitations

- no type casts
- no checks for required values
- no complains over superfluous args
- no validation
- no arrays, use delimiters
- no multi args, use delimiters
- no lookahead, use explicit `=` for assignment
- no auto help pages


## Prior art

Argster is inspired by node's `minimist` module.


## License

MIT