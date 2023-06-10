import re 

def re_match(text, /, *,p = re.compile(r"[a-z]+")):
    """
    re.match() is done at the start of the string
    """
    print(f"### {re_match.__name__}")
    m = p.match(text)
    if m:
        print(p, m)
        print(m.group())
        print(m.span())
    else:
        print("No match found.")
    print()

re_match("tempo")

def re_search(*,p = re.compile(r"[a-z]+")):
    """
    re.match() is done at the start of the string
    """
    def wrapper(text, /):
        nonlocal p
        print(f"### {re_search.__name__}")
        m = p.search(text)
        if m:
            print(p, m)
            print(m.group())
            print(m.span())
        else:
            print("No matcheds found")
        print()
    return wrapper

search = re_search()
search("::: message")


def re_findall(*, pattern=r"\d+"):
    """
    findall(): returns a list of matching strings
    """
    print(f"### {re_findall.__name__}")
    p = re.compile(pattern)
    def wrapper(text):
        nonlocal p 
        print(p.findall(text))
        print()
        # return p.findall(text)
    return wrapper
    
findall = re_findall()
findall("12 drummers drumming, 11 pipers pipings.")
re_findall(pattern=r"\w+")("123 is the 12323")
re_findall(pattern=r"[a-z]+")("123 is the 12323")




# def power(*, pow=1):
#     def wrapper(num, /):
#         nonlocal pow 
#         return num ** pow
#     return wrapper

# def count(num: int = 0, /):
#     if type(num) == count.__annotations__.get("num"):
#         pass 
#     else:
#         raise TypeError("num: should be int")

#     def wrapper():
#         nonlocal num 
#         num = num + 1 
#         return num
#     return wrapper
