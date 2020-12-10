import itertools


def main():
    arr = []
    while True:
        try:
            arr.append(int(input().rstrip()))
        except EOFError:
            break
    bad = find_bad(arr)
    print("BAD: ", bad)
    print(weakness(arr, bad))


def find_bad(arr):
    for idx in range(25, len(arr)):
        if any(
            e1 + e2 == arr[idx]
            for e1, e2 in itertools.combinations(arr[idx - 25 : idx], 2)
        ):
            continue
        else:
            return arr[idx]


def weakness(arr, bad):
    low, hi = 0, 1
    less, big = float('inf'), float('-inf')
    while True:
        s = sum(arr[low:hi])
        if s < bad:
            hi += 1
        elif s > bad:
            low += 1
        else:
            keys = arr[low:hi]
            keys.sort()
            print('KEYS: ', keys[0], keys[-1])
            return keys[0] + keys[-1]


if __name__ == "__main__":
    main()
