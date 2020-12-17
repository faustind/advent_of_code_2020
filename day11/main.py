from copy import deepcopy


def valid(layout, i, j):
    return 0 <= i < len(layout) and 0 <= j < len(layout[0])

def count_occ2(layout, i, j):
    count = 0
    for r, c in adjacency:
        nr, nc = i + r, j + c
        while True:
            if not valid(layout, nr, nc):
                break
            if layout[nr][nc] in ['L', '#']:
                if layout[nr][nc] == '#':
                    count += 1
                break
            nr, nc = nr + r, nc + c
    return count

def count_occ(layout, i, j):
    count = 0
    for r, c in adjacency:
        nr, nc = i + r, j + c
        count += 1 if valid(layout, nr, nc) and layout[nr][nc] == "#" else 0
    return count


def rotate(layout):
    l = deepcopy(layout)
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == "L" and count_occ2(layout, i, j) == 0:
                l[i][j] = "#"
            elif layout[i][j] == "#" and count_occ2(layout, i, j) >= 5:
                l[i][j] = "L"
            else:
                continue
    return l


def main():
    layout = []

    while True:
        try:
            layout.append(list(input().strip()))
        except EOFError:
            break

    while True:
        nl = deepcopy(layout)
        layout = rotate(nl)
        if nl == layout:
            break

    fcount = sum(
        1 if layout[i][j] == "#" else 0
        for i in range(len(layout))
        for j in range(len(layout[i]))
    )

    print("FINAL OCCUPIED: ", fcount)


if __name__ == "__main__":
    adjacency = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1),
    ]

    main()
