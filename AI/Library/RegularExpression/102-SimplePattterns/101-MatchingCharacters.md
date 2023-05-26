# Matching Characters

Most letters and characters will simply match themselves. 

For example:

    - the regular experssion `test` will match the string `test` exactly.

There are exceptions to this rule; some characters are special *metacharacters*, and don't match themselves.

Here’s a complete list of the metacharacters; their meanings will be:

```py
. ^ $ * + ? { } [ ] \ | ( )
```

### `[` and `]`

The first metacharacters we'll look at are `[` and `]`. They're used for specifying a character class, which is a set of characters that you wish to match. 

Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by a `'-'`.

For example: `[abc]` will match any of the characters `a`, `b`, or `c`; this is the same as `a-c`, whic huses a range to express the same set of characters. If you want to match only lowercase letters, you RE would be `[a-z]`.

### `$`

Metacharactes (except `\`) are not active inside classes. For example, `[akm$]` will match any of the characters `'a'`, `'k'`, `'m'` or `'$'`; `'$'` is usually a metacharacter, but inside a character class it's stripped of its special nature.

### `^`

You can match the characters not listed within the class by `complementing` the set. This is indicated by including a caret `'^'` as the first character of the class. 
For example, `[^5]` will match any character except `'5'`. 
If he caret appears elsewhere in a character class, it does not have special meaning. For example: `[5^]` will match either a `'5'` or a `'^'`.

### `\`

Back can be followed by various characters to sginal variaous special sequences. 
It's also used to escape all the metacharacters so you can still match them in patterns; for example, it you need to match a `[` or `\`, you can precided them with a backslash to remove their special meaning: `\` or `\\`.

### The following list of sequences:

\d: Matches any decimal digit; this is equivalent to the class [0-9].

\D: Matches any non-digit character; this is equivalent to the class [^0-9].

\s: Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S: Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w: Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W: Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

- These sequences can be included inside a character class. For example, `[\s,.]` is a character class that will match any whitespace character , or `,` or `.`.

- The final metacharacter is this section is `.`. It matches anyting except a newline character, and there's an alternative mode *(re.DOTALL)* where it will match even a newline. `.` is often used where you want to  match "any character".

- The first metacharacter for repeateing things that we'll look at is `*`. `*` doesn't match the literal character `'*'`; intead, it specifies that the previous character can be matched zero or more times.

- For example, `ca*t` will match `ct` (0, `'a'` characters), `'cat'` (1, `'a'`), `'caaat'` (3 `'a'` characters), and so forth.

- Repetitions such as `*` are *greedy*; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with fewer repetitions.

#### Quantifier: `?` 

The question mark character, matches either once or zero timse. For example, `home-?brew` matches either `'homebrew'` or `'home-brew'`.

#### Quantifier: `{m,n}`

- The most complicated quantifier is `{m, n}`, where *m* and *n* are decimal integers. This quantifier means there must be at least *m* repetitions, and at most *n*.

- example, `a/{1,3}b` will match `'a/b'`, `'a//b'`, and `'a///b'`. It won’t match 'ab', which has no slashes, or `'a////b'`, which has four.