from utils import *

test = TestInput(1, int)
inp = Input(1, int)

for a, b in combinations(inp, 2):  # Part 1
    if a + b == 2020:
        print(a * b)

for a, b, c in combinations(inp, 3):  # Part 2
    if a + b + c == 2020:
        print(a * b * c)
