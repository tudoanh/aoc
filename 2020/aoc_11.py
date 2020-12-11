from utils import *


inp = Input(11)

m = {"L": -1, ".": 0, "#": 1}


def replace(s, m):
    for char, value in m.items():
        s = s.replace(char, value)


print(list(map(lambda x: replace(x, m), inp)))

# for row in cycle(inp):
#     count = 0
#     new = []
#     for idx, seat in enumerate(row):
#         if seat == 'L' and row[idx - 1]
#     if count == 0:
#         c = Counter(''.join(
#         break
