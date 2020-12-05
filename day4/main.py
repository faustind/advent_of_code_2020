import string


def main():
    count = 0
    while not finished:
        if is_valid_passport(read_passport()):
            count += 1
    print(count)


def read_passport():
    global finished
    d = {}
    r = row()
    while r:
        for k, v in (kv.split(":") for kv in r.split()):
            d[k] = v
        try:
            r = row()
        except EOFError:
            finished = True
            r = ""
    return d


def is_valid_passport(ps):
    for k in valid_keys:
        if k not in ps:
            return False
        if not validators[k](ps[k]):
            return False
    return True


def row():
    r = input()
    if all(c.isspace() for c in r):
        return ""
    else:
        return r


def hgt(x):
    if x[-2:] == "cm":
        return 150 <= int(x[:-2]) <= 193
    if x[-2:] == "in":
        return 59 <= int(x[:-2]) <= 76
    return False


def hcl(x):
    return (
        len(x) == 7
        and x[0] == "#"
        and all(c in string.digits or c in string.ascii_lowercase[:6] for c in x[1:])
    )


validators = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and all(c in string.digits for c in x),
    "cid": lambda x: True,
}


if __name__ == "__main__":
    finished = False
    valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    main()
