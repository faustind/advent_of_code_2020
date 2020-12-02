import collections

def is_valid(low, high, c, p):
    cs = collections.Counter(p)
    if c not in cs:
        c_count = 0
    else:
        c_count = cs[c]

    return low <= c_count <= high

def is_valid_2(low, high, c, p):
    low, high = low-1, high-1

    return (p[low] == c) ^ (p[high] == c)

def make_input():
    lh, cc, p = input().rstrip().split()
    low, high = map(int, lh.split('-'))
    c = cc[:-1]
    return (low, high, c, p)

def main():
    count = 0
    while True:
        try:
            low, high, c, p = make_input()
        except EOFError:
            break
        if is_valid_2(low, high, c, p):
            count += 1

    print(count)

if __name__ == "__main__":
    main()
