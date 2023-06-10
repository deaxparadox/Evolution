# The Backslash Plague

- Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning.

- To match a literal backslash, one has to write `'\\\\'` as the RE string, because the regular expression must be `\\`, and each backslash must be expressed as `\\` inside a regular Python string literal.

- use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with `'r'`, so `r"\n"` is a two-character string containing `'\'` and `'n'`, while `"\n"` is a one-character string containing a newline.

[<<< Compilinng Regular Expressions](101-CompilingRegularExpressions.md) ... [Performing Matches >>>](103-PerformingMatches.md)

