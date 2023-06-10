# Compiling Regular Expressions

```python
import re
p = re.compile('ab*')
p

```

- re.compile() also accepts an optional flags argument, used to enable various special features and syntax variations.

```python
p = re.compile('ab*', re.IGNORECASE)
```

[<<< README](README.md) ... [Backslash Plague >>>](102-BackslashPlague.md)