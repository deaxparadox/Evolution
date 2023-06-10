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


# I, IGNORECASE

- Perform case-insensitive matching; character class and literal strings will match letters by ignoring case. 
- For example, `[A-Z]` will match lowercase letters, too.
- Full Unicode matching also works unless the ASCII flag is used to disable non-ASCII matches.
- When the Unicode patterns `[a-z]` or `[A-Z]` are used in combination with the IGNORECASE flag, they will match the 52 ASCII letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless i), ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign).
- Spam will match 'Spam', 'spam', 'spAM', or 'ſpam' (the latter is matched only in Unicode mode). This lowercasing doesn’t take the current locale into account; it will if you also set the LOCALE flag.

