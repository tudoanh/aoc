inp = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split(
    "\n"
)

# inp = open("inputs/input_24.txt", "rt").read().strip().split("\n")


def parse(e):
    e = (
        e.replace("nw", " NW ")
        .replace("sw", " SW ")
        .replace("ne", " NE ")
        .replace("se", " SE ")
        .replace("e", " e ")
        .replace("w", " w ")
    )
    return e


# Create empty grid
grid = {}


# Use complex number to represend adjection tiles by directions
E = 1
NE = 1j
SE = 1 - 1j

W = -1
NW = -1 + 1j
SW = -1j

m = dict(e=E, NE=NE, SE=SE, w=W, NW=NW, SW=SW)


def find(inp):
    e = parse(inp).split()
    cor = 0 + 0j
    for i in e:
        cor += m[i]

    if cor in grid:
        grid[cor] = not grid[cor]
    else:
        grid[cor] = True


for move in inp:
    find(move)

print("=== Part 1")
res = [i for i in grid.values() if i]
print(len(res))


def sum_neighbor(board, x):
    return sum([board.get(x + m[n], False) for n in m])


def play():
    # Add neighbors
    for x in grid.copy():
        for n in m:
            z = x + m[n]
            if z not in grid:
                grid[z] = False

    # Game of life logic
    board = grid.copy()
    for x in board:
        nb = sum_neighbor(board, x)
        if board[x] is True and (nb == 0 or nb > 2):
            grid[x] = False
        if board[x] is False and nb == 2:
            grid[x] = True


print("=== Part 2")
for i in range(100):
    play()


res = [i for i in grid.values() if i]
print(len(res))
