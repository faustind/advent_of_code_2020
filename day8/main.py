def execute():
    executed = set()

    acc, ci = 0, 1
    while ci <= n_ins:
        if ci in executed:
            print(f'looped: {acc}\n')
            return False
        else:
            executed.add(ci)
        i, arg = ins[ci]
        if i == 'acc':
            ci, acc = ci+1, acc+arg
        elif i == 'nop': # jmp -> nop
            ci, acc = ci+1, acc
        else:
            ci, acc = ci+arg, acc

    print('SUCCESS: ', acc)
    return True

def iterate():
    global ins

    for idx, (i, _) in enumerate(ins.values(), 1):
        if i == 'nop':
            ins[idx][0] = 'jmp'
        elif i == 'jmp':
            ins[idx][0] = 'nop'
        else:
            continue

        ok = execute()

        if ok:
            return
        else:
            if ins[idx][0] == 'nop':
                ins[idx][0] = 'jmp'
            elif ins[idx][0] == 'jmp':
                ins[idx][0] = 'nop'

def main():
    global n_ins
    while True:
        try:
            inst, arg = input().rstrip().split()
            n_ins += 1
            arg = int(arg)
            ins[n_ins] = [inst, arg]
        except EOFError:
            break
    # execute()
    iterate()

if __name__ == "__main__":
    finished = False
    in_switch = False
    n_ins, acc = 0, 0
    ins = {}
    main()
