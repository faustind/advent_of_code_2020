def find_row(rows: str) -> int:
    return len(rows) == 7 and sum(2 ** (6-idx) if c == 'B' else 0 for (idx, c) in enumerate(rows))

def find_col(cols: str) -> int:
    return sum(2 ** (2-idx) if c == 'R' else 0 for (idx, c) in enumerate(cols))

def seat_id(s: str) -> int:
    return find_row(s[:7]) * 8 + find_col(s[7:])

def main():
    ss = set()
    while True:
        try:
            s = input().rstrip()
        except EOFError:
            break

        ss.add(seat_id(s))

    m = max(ss)
    print(m)

    for i in range(m):
        if i not in ss and i-1 in ss and i+1 in ss:
            print(i)

if __name__ == "__main__":
    main()
