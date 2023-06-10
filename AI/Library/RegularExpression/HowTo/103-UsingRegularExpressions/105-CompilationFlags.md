# Compilation Flags

- Compilation flags let you modify some aspects of how regular expression work. 
- Flags are available in th `re` module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.
- Multiple flags can be specified by bitwise OR-ing them; `re.I | re.M` sets both the I and M flags, for example:

- `ASCII, A`: Makes several escapes like `\w`, `\b`, `\s` and `\d` match only on `ASCII` characters with the respective property.
- `DOTALL, S`: Make `.` match any character, including newlines.
- `IGNORECASE, I`: Do case-insensitive matches
- `LOCALE, L`: Do a local-aware match.
- `MULTILINE, M`: Multi-line matching, affecting `^` and `$`.
- `VERBOSE, X (for 'extended')`: Enable verbose REs, which can be organized more cleanly and understandably.

