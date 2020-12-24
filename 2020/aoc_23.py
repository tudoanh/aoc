import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


## Part 1
def part_1(n=100):
    inp = [int(i) for i in list("389125467")]
    for i in range(n):
        choose = inp[0]
        logging.debug(f"--- Round {i + 1}")
        logging.debug(f"Init {inp}")
        logging.debug(f"Choose {choose}")

        # pick 3 numbers after choosen
        picks = inp[1:4]
        del inp[1:4]
        logging.debug(f"Picks {picks}")

        # find destination
        if choose > 1:
            des = choose - 1
        else:
            des = max(inp)
        while des in picks:
            if des > 1:
                des -= 1
            else:
                des = max(inp)
        logging.debug(f"Destination {des}")

        # Insert picked labels after destination
        idx = inp.index(des)
        inp.insert(idx + 1, picks[0])
        inp.insert(idx + 2, picks[1])
        inp.insert(idx + 3, picks[2])

        logging.debug(f"Final {inp}")
        logging.debug("\n")

        # Make next label first index
        z = inp.pop(0)
        inp.append(z)

    # Return result
    i = inp.index(1)
    return "".join(map(str, inp[i + 1 :] + inp[:i]))


print(f"Part 1: {part_1()}")

## Part 2
def part_2(n=10_000_000):
    inp = [int(i) for i in list("389125467")]

    i = inp.index(1)
    return inp[i + 1] * inp[i + 2]


print(f"Part 2: {part_2()}")
