def main():
    def backtrack(e, idx):
        if e in computed:
            return
        computed[e] = 0
        for child_idx, child in enumerate(arr[idx+1: idx+4], idx+1):
            if child - e > 3:
                break
            backtrack(child, child_idx)

            computed[e] += computed[child]

    arr = [0]
    computed = {}

    while True:
        try:
            arr.append(int(input().rstrip()))
        except EOFError:
            break

    arr.sort()
    arr.append(arr[-1] + 3)

    computed[arr[-1]] = 1
    backtrack(arr[0], 0)

    print(computed[arr[0]])

    # print(count_diff(arr))



def count_diff(arr):
    c1, c3 = 0, 0
    for (e1, e2) in zip(arr, arr[1:]):
        if e2 - e1 == 1:
            c1 += 1
        if e2 - e1 == 3:
            c3 += 1
    return c1 * c3

if __name__ == "__main__":
    main()
