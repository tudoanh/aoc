import math
from utils import *


inp = Input(10, int)

ones = 0
threes = 0

new_inp = sorted(set(inp + (0, max(inp) + 3)))

# Part 1
for i in new_inp:
    if i + 1 in new_inp:
        ones += 1
    elif i + 3 in new_inp:
        threes += 1

print(ones * threes)

# Part 2

prev = 0
s = 0
d = 1

for i in new_inp:
    if i - prev == 1:
        s += 1
    else:
        d *= (2 ** max(0, s - 1)) - max(0, s - 3)
        s = 0
    prev = i

print(d)
