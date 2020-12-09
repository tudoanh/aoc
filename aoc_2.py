from utils import *

test = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

inp = Input(2)

c1 = 0
c2 = 0

for i in inp:
    ran, char, pwd = i.split()
    mi, ma = [int(j) for j in ran.split("-")]
    char = char[0]
    c = Counter(pwd)
    if mi <= c[char] <= ma:
        c1 += 1
    if (pwd[mi - 1] == char and not pwd[ma - 1] == char) or (
        pwd[ma - 1] == char and not pwd[mi - 1] == char
    ):
        c2 += 1

print(c1, c2)
