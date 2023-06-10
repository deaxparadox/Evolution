# Module level functions


- the `re` module also provides top-level functions called *match()*, *search()*, *findall()*, *sub()*, and so forth.
- there functions take the same argument corresponding pattern method will the RE string added as the first argument, and still return either `None` or a `match object` instance.


```python
>>> print(re.match(r'From\s+', 'Fromage amk'))
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')  
<re.Match object; span=(0, 5), match='From '>
```


[<<< Performing Matches](103-PerformingMatches.md) ... [Compilation Flags >>>](105-CompilationFlags.md)
