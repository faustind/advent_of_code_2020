import itertools


def main():
    my_time = int(input())
    line2 = itertools.filterfalse(lambda c: c == "x", input().rstrip().split(","))

    _ts = list(map(int, line2))

    ts = _ts[:]

    soon = None

    while True:
        if all(t - my_time >= 0 for t in ts):
            soon = min(ts, key=lambda t: t - my_time)
            break
        for idx, t in enumerate(ts):
            if t - my_time < 0:
                ts[idx] += _ts[idx]

    print(_ts)
    print(ts)
    print([t - my_time for t in ts])

    print((soon - my_time) * _ts[ts.index(soon)])


if __name__ == "__main__":
    main()
