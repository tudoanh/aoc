def check(li, n):
    for i in li:
        if n - i in li:
            return True
    return False


def main():
    f = open("input_9.txt", "rt")
    inp = [int(i.strip()) for i in f.readlines()]
    start = 0
    pream = 25
    invalid = 0

    for i in inp[pream:]:  # << Part 1
        if not check(inp[start : pream + start], i):
            invalid = i
            break
        start += 1

    a = 0
    c = 0

    for i in range(len(inp)):  # << Part 2
        print("Attemp %d" % a)
        for idx, j in enumerate(inp[a:]):
            c += j
            if c > invalid:
                c = 0
                a += 1
                break
            if c == invalid:
                valid = inp[a : idx + a + 1]
                return sum([min(valid), max(valid)])

    return invalid


if __name__ == "__main__":
    print(main())
