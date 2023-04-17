def check_outside_field(r, c, L):
    if not (0 <= r < len(L)) or not (0 <= c < len(L[0])):
        return True
    return False


def valid_move(cell):
    if cell == 'v':
        return True
    return False


def wall(cell):
    if cell == '*':
        return True
    return False


def create_field(r):
    L = []
    for r in range(r):
        L.append(list(input()))
    return L


def find_path(r: int, c: int, lab: list, direct: str, path: list, paths_out: list):
    # base cases
    #
    if check_outside_field(r, c, lab) or wall(lab[r][c]) or valid_move(lab[r][c]):
        return

    if lab[r][c] == 'e':
        paths_out.append(path)
        # print(path)
        return

    # mark move as a valid one
    lab[r][c] = 'v'

    # recursion call
    directions = {"D": lambda x, y: (x + 1, y),
                  "U": lambda x, y: (x - 1, y),
                  "L": lambda x, y: (x, y - 1),
                  "R": lambda x, y: (x, y + 1)}
    for direct in directions:

        find_path(directions[direct](r, c)[0], directions[direct](r, c)[1], lab, direct, path + [direct], paths_out)

    # post action
    lab[r][c] = '-'

    return paths_out


rows = int(input())
cols = int(input())
labyrinth = create_field(rows)
paths_out = find_path(0, 0, labyrinth, '', [], [])
longest = []
for path in paths_out:
    if len(path) > len(longest):
        longest = path

print(f"The longest path is:\n")
print(*longest, end='')

"""
Example input:

3
5
-**-e
-----
*****

Expected output: DRRRRU
"""
