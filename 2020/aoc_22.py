inp1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split(
    "\n\n"
)

inp2 = """Player 1:
43
19

Player 2:
2
29
14""".split(
    "\n\n"
)

inp3 = open("inputs/input_22.txt", "rt").read().strip().split("\n\n")


def parse(inp):
    p1 = [int(i) for i in inp[0].split("\n")[1:]]
    p2 = [int(i) for i in inp[1].split("\n")[1:]]
    return p1, p2


def cal(p):
    p.reverse()
    c = 0
    for a, b in enumerate(p, 1):
        c += a * b
    return c


## Part 1
def play(p1, p2):
    while p1 and p2:
        # print(f"P1 deck {p1}")
        # print(f"P2 deck {p2}")
        x = p1.pop(0)
        y = p2.pop(0)
        if x > y:
            p1.append(x)
            p1.append(y)
        if y > x:
            p2.append(y)
            p2.append(x)
    if p1:
        return p1
    return p2


print("==== Part 1")
print("Test")
p1, p2 = parse(inp1)
print(cal(play(p1, p2)))

print("REAL")
p1, p2 = parse(inp3)
print(cal(play(p1, p2)))

## Part 2
def play(p1, p2, game=1):
    mem = {}
    round = 1
    while p1 and p2:
        # print(f"P1 deck {p1}")
        # print(f"P2 deck {p2}")
        check = (tuple(p1), tuple(p2))
        if not check in mem:
            mem[check] = True
        else:
            return 1, p1
        x = p1.pop(0)
        y = p2.pop(0)
        p1_win = x > y
        p2_win = y > x
        if len(p1) >= x and len(p2) >= y:
            # Sub game
            who, result = play(p1.copy()[:x], p2.copy()[:y], game=game + 1)
            if who == 1:
                p1_win = True
                p2_win = False
            else:
                p2_win = True
                p1_win = False

        if p1_win:
            p1.append(x)
            p1.append(y)
            # print(f"Round {round} Game {game} P1 win")
        if p2_win:
            p2.append(y)
            p2.append(x)
            # print(f"Round {round} Game {game} P2 win")
        round += 1
    if p1:
        return 1, p1
    return 2, p2


print("==== Part 2")
print("Test")
p1, p2 = parse(inp1)
print(cal(play(p1, p2)[1]))

print("Test 2")
p1, p2 = parse(inp2)
print(cal(play(p1, p2)[1]))

print("REAL")
p1, p2 = parse(inp3)
print(cal(play(p1, p2)[1]))
