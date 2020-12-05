def count_trees(right, down):
    r, d = 0, 0
    count = 0
    while d < len(carte):
        if carte[d][r%len(carte[0])] == tree:
            count += 1
        r, d = r + right, d + down
    return count


def main():
    while True:
        try:
            carte.append(input().rstrip())
        except EOFError:
            break
    c = 1
    for s in ss:
        c *= count_trees(*s)
    print(c)

if __name__ == "__main__":
    tree = '#'
    slope = (3, 1)
    ss = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    carte = []
    main()
