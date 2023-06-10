# Performing Matches

- *match()*: Determine if the RE matches at the begining of the string.
- *search()*: Scan through a string, looking for any location wher ethis RE matches.
- *findall()*: Find all substrings where the RE matches, and returns them as a list.
- *fileiter()*: Find all substrings where the RE matches, and returns them as an iterator.


```python
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')
`
```

- An empty string shouldn’t match at all, since + means ‘one or more repetitions’. match() should return None in this case, 

```python
>>> p.match("")
>>> print(p.match(""))
None
```

- Now, let’s try it on a string that it should match, such as `tempo`. In this case, `match()` will return a match object, so you should store the result in a variable for later use.

```python
>>> m = p.match('tempo')
>>> m
```

Now you can query the match object for information about the matching string.

- Match object instances also have several methods and attributes; the most important ones are:
    1. **group()**: Return the string matched by the RE
    2. **start()**: Return the starting position of the match
    3. **end()**: Return the ending position of the match
    4. **span()**: Return the tuple containing the (start, end) positions of the match.

```python
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)
```

- `group()` returns the substring that was matched by the RE.
- `start()` and `end()` return the starting and ending index of the match.
- `span()` returns both start and end indexes in a single tuple.


```python
>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)
```

- the most common style is to store the `match object` in a variable, and then check if it was None.

```python
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
```

Two pattern methods return all the the matches for a pattern. 

- *findall()* returns a list of matching strings.

```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```


- *finditer()*: methods return a sequence of match object instances as an iterator:

```python
>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator  
<callable_iterator object at 0x...>
>>> for match in iterator:
...     print(match.span())
... 
(0, 2)
(22, 24)
(29, 31)
```

[<<< Backslash Plague](102-BackslashPlague.md) ... [Module-Level Functions >>>](104-Module-LevelFunctions.md)
