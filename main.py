from time import sleep

p = "|"
for i in range(1, 101):
    exp: str = "Progress:" + "%s".rjust(4) + " %s ".ljust(30) + "\r\b"
    if i % 5 == 0:
        mul = i // 5 
        p = "\u265E" * mul
    print(exp % (i, p,), end="", flush=True)
    sleep(.01)
print()