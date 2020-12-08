# {"light red bags": [(1, "bright white"), (2, "muted yellow")]}
import collections

def process_row():
    """Return tuple of (v)"""
    global finished
    global bags
    try:
        r = input()
    except EOFError:
        finished = True
        return
    ss = r.split() # don't process period at the end
    m = ' '.join(ss[:2])
    bags[m] = collections.defaultdict(lambda: {'weight': float('inf'), 'capacity':0})
    if ss[4] == 'no': # m contain no other bag
        return
    del ss[:4] # remove 1st 4 words
    while ss:
        n, c1, c2 = ss[:3]
        bags[m][' '.join([c1, c2])] = {'weight': 1, 'capacity': int(n)}
        del ss[:4]

def possibilities():
    keys = list(bags)
    for k in keys:
        for i in keys:
            for j in keys:
                through_k = bags[i][k]['weight'] + bags[k][j]['weight']
                if through_k < bags[i][j]['weight']:
                    bags[i][j]['weight'] = through_k

    return sum(1 if bags[k]['shiny gold']['weight'] < float('inf') else 0 for k in bags)

def how_many(s):
    return sum(bags[s][b]['capacity'] * (how_many(b)+1) for b in bags[s])

def main():
    while not finished:
        process_row()

    # print(possibilities())
    print(how_many('shiny gold'))


if __name__ == "__main__":
    bags = {}
    finished = False
    main()
