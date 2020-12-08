import collections

def row():
    r = input()
    if all(c.isspace() for c in r):
        return ""
    else:
        return r

def read_g():
    global finished
    g = collections.Counter()
    n = 0
    r = row()
    while r:
        n += 1 # nmembers in g
        g.update(r)
        try:
            r = row()
        except EOFError:
            r, finished = "", True
    return n, g

def anyone_count():
    count = 0
    while not finished:
       _, g = read_g()
       count += len(g)

    print(count)

def everyone_count():
    count = 0
    while not finished:
        n, g = read_g()
        count += sum(1 if v == n else 0 for v in g.values())
    print(count)

def main():
    # anyone_count()
    everyone_count()






if __name__ == "__main__":
    finished = False
    main()
