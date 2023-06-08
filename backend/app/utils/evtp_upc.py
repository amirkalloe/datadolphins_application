import random


def create_upc():
    rl = []
    id = ""
    for i in range(0, 7):
        n = random.randint(0, 9)
        rl.append(str(n))
    e = int(rl[0]) + int(rl[2]) + int(rl[4]) + int(rl[6])
    o = int(rl[1]) + int(rl[3]) + int(rl[5])
    c = (e * 3 + o) % 10
    rl.append(str(c))
    return id.join(rl)


def upc_check(upc_code: str):
    r = []
    r[:] = upc_code
    e = int(r[0]) + int(r[2]) + int(r[4]) + int(r[6])
    o = int(r[1]) + int(r[3]) + int(r[5])
    c = (e * 3 + o) % 10
    return True if c == int(r[7]) else False


if __name__ == "__main__":
    print(create_upc())
    print(upc_check('90329614'))
