
import re 

s = re.split("\s", "16 9 3 15 3 20 6 {20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}")
print(s)

for c in s:
    if c.isnumeric():
        print(chr(ord('a') + int(c) - 1), end="")
    else:
        print(c, end="")
