class Console:
    def __init__(self):
        self.input = "input_8.txt"
        f = open(self.input, "rt")
        self.inp = [i.strip() for i in f.readlines()]

    def process(self, inp):
        var = 0
        mem = []
        idx = 0
        if not inp:
            inp = self.inp.copy()

        try:
            while idx not in mem:
                op, val = inp[idx].split()
                val = int(val)
                mem.append(idx)
                if op == "nop":
                    idx += 1
                    continue
                if op == "acc":
                    idx += 1
                    var += val
                if op == "jmp":
                    idx += val
            return (False, var)
        except Exception as e:
            return (True, var)

    def fix(self):
        mem = []
        max_attemp = [1 for k in self.inp if k.startswith("jmp")]
        for i in range(len(max_attemp)):
            print("Attempt %d" % i)
            inp = self.inp.copy()
            for idx, j in enumerate(inp[:]):
                if j.startswith("jmp") and idx not in mem:
                    inp[idx] = j.replace("jmp", "nop")
                    mem.append(idx)
                    break
            ok, res = self.process(inp)
            if ok:
                return res


def main():
    c = Console()
    part1 = c.process(None)
    part2 = c.fix()
    return part1, part2


if __name__ == "__main__":
    print(main())
