from utils import *


inp = Input(10, int)

ones = 0
threes = 0

new_inp = sorted(set(inp + (0, max(inp) + 3)))

# Part 1
# for i in new_inp:
#     if i + 1 in new_inp:
#         ones += 1
#     elif i + 3 in new_inp:
#         threes += 1
#
# print(ones * threes)

# Part 2

A = []
B = []

for i in new_inp:
    if i + 1 in new_inp:
        A.append(i)
    elif i + 3 in new_inp:
        A.append(i)
        B.append(A)
        A = []

B[-1].append(max(inp) + 3)

count = 1
for s in B:
    P = list(powerset(s[1:-1]))
    print(P)
    count *= len(P)

print(count)
print(B)
