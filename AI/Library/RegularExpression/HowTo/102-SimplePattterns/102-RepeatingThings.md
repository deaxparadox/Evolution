# Repeating things

- Being able to match varying sets of characters is the first things regular expression can do.

- Another capability is that you can specify that portions of the RE must be repeated a certain number of times.

## `*`

- `*` doesn't match the literal character `'*'`; instead, it specifies that the previous character can be matched zero or mote times, instead of exactly once.

- For example, `ca*t` will match `'ct'` (0 `'a'` characters), `'cat'` (1 `'a'`), `'caaat'` (3 `'a'` characters), and so forth.

- Repetitions such as `*` are *greedy*, when repeating a RE, the matching engine will try to repeat it as many times as possible.

- `*` matches zero or more times.

## `+` 

- Another repeating metacharacter is `+`, which matches one or more times. 

- `+` requires at least one occurrence.

- ca+t will match `'cat'` (1 `'a'`), `'caaat'` (3 `'a'`s), but won’t match `'ct'`.

## `?`

- The question mark character, `?`, matches either once or zero times.

- For example, `home-?brew` matches either `'homebrew'` or `'home-brew'`.

## `{m, n}`

- The most complicated qualifier is `{m, n}`, where m and n decimal integers. 

- this quantifier means there must be at least *m* repetitions, and at most *n*.

- For example, `a/{1,3}b` will match `'a/b'`, `'a//b'`, and `'a///b'`. It won’t match `'ab'`, which has no slashes, or `'a////b'`, which has four.

- You can omit either *m* or *n*; in that case, a reasonable value is assumed for the missing value. Omitting *m* is interpreted as a lower limit of 0, while omitting *n* results in an upper bound of infinity.

**`{0,}` is the same as `*`, `{1,}` is equivalent to `+`, and `{0,1}` is the same as `?`. It’s better to use `*`, `+`, or `?` when you can**