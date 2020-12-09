import re
import functools


def p1():
    with open("input_7.txt", "rt") as f:
        inp = [i.strip() for i in f.readlines() if "no" not in i]
        splited = [i.split(" contain ") for i in inp]
        holds = [i[0].rstrip(" bags") for i in splited if "shiny gold" in i[1]]
        for i in range(10):
            for color in holds:
                for line in splited:
                    if color in line[1]:
                        c = line[0].rstrip(" bags")
                        if c not in holds:
                            holds.append(c)
        return set(holds)


def get(m, c):
    if m[c] == 1:
        return 0
    else:
        res = sum([m[c][i] * get(m, i) + m[c][i] for i in m[c]])
        return res


def p2():
    with open("input_7.txt", "rt") as f:
        inp = [i.strip() for i in f.readlines()]
        m = {}
        for i in inp:
            splited = i[:-1].split(" contain ")
            color = splited[0].rstrip(" bags")
            info = splited[1]
            if not re.match("\d+", info):
                m[color] = 1
            else:
                m[color] = {s[2:].rstrip(" bags"): int(s[0]) for s in info.split(", ")}

        return get(m, "shiny gold")


if __name__ == "__main__":
    print(len(p1()))
    print(p2())
