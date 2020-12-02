import itertools
from typing import List

def two_entries(arr: List):
    for a, b in itertools.combinations(arr, 2):
        if a + b == 2020:
            return a * b

def three_entries(arr: List):
    for a, b, c in itertools.combinations(arr, 3):
        if a + b + c == 2020:
            return(a * b * c)

def main():
    arr = []
    while True:
        try:
            arr.append(int(input()))
        except EOFError:
            break
    # print(two_entries(arr))
    print(three_entries(arr))

if __name__ == "__main__":
    main()
