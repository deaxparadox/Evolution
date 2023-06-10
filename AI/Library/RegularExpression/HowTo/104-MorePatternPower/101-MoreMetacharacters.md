# More Metacharacters

# `|`

Alternation, or the "or" operator. 

- If A and B are regular expressions, `A|B` will match any string any string that matches either A or B.
- `|` has very low precedence in order to make it work reasonably when you're alternating multicharacter strings. 
- `Crow|Servo` will match either `'Crow'` or `'Servo'`, not `'Cro'`, a `'w'` or an `'S'`, and `'ervo'`.

- **To match a literal `'|'`, use `\|`, or enclose it inside a character class, as in `[|]`**