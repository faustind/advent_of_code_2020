def wp():
    """Move the way point according to instructions."""
    pass

def main2():
    e, s, w, n = "E", "S", "W", "N"
    south, east = 0, 0
    wsouth, weast = -1, 10
    #   N
    # W    E
    #   S
    while True:
        try:
            row = input().rstrip()
            i = row[0]
            k = int(row[1:])
            if i == 'F':
                # move boat
                east += k * weast
                south += k * wsouth
            # waypoint mvt
            if i == e:
                weast += k
            if i == w:
                weast += -k
            if i == n:
                wsouth += -k
            if i == s:
                wsouth += k
            if i == 'R':
                for _ in range(k // 90):
                    weast, wsouth = -wsouth, weast
            if i == 'L':
                for _ in range(k // 90):
                    weast, wsouth = wsouth, -weast

        except EOFError:
            break

    print(abs(south) + abs(east))


def main():
    e, s, w, n = "E", "S", "W", "N"
    south, east = 0, 0
    #   N
    # W    E
    #   S
    l = {
        "E": {"0": "E", "90": "N", "180": "W", "270": "S"},
        "S": {"0": "S", "90": "E", "180": "N", "270": "W"},
        "W": {"0": "W", "90": "S", "180": "E", "270": "N"},
        "N": {"0": "N", "90": "W", "180": "S", "270": "E"},
    }
    r = {
        "E": {"0": "E", "90": "S", "180": "W", "270": "N"},
        "S": {"0": "S", "90": "W", "180": "N", "270": "E"},
        "W": {"0": "W", "90": "N", "180": "E", "270": "S"},
        "N": {"0": "N", "90": "E", "180": "S", "270": "W"},
    }

    curr_dir = e

    while True:
        try:
            row = input().rstrip()
            i = row[0]
            k = int(row[1:])
            if i == 'R':
                curr_dir = r[curr_dir][row[1:]]
            if i == 'L':
                curr_dir = l[curr_dir][row[1:]]
            if i == 'F':
                if curr_dir == e:
                    east += k
                if curr_dir == w:
                    east += -k
                if curr_dir == n:
                    south += -k
                if curr_dir == s:
                    south += k
            if i == e:
                east += k
            if i == w:
                east += -k
            if i == n:
                south += -k
            if i == s:
                south += k

        except EOFError:
            break

    print(abs(south) + abs(east))


if __name__ == "__main__":
    main2()
