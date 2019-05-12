from random import randint


def gen_pos(nb):
    pos = []
    while nb:
        p = [randint(64, 576), randint(64, 416)]
        found = False
        for i in pos:
            if i[0]+28 > p[0] and i[0] < p[0]+28 and i[1]+28 > p[1] and i[1] < p[1]+28:
                found = True
                break
        if not found:
            pos.append(p)
            nb -= 1
    return pos
