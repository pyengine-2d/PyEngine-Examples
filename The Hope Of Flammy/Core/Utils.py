from random import randint
from pyengine.Components import PositionComponent

from Core.Characters.Goutte import Goutte


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


def gen_ennemies(posr, score, game):
    ennemies = []
    while score:
        monster = None
        if score >= 5:
            monster = Goutte(game)
            score -= 5
        else:
            score = 0
        if monster:
            found = True
            while found:
                position = monster.get_component(PositionComponent)
                pos = [randint(64, 576), randint(64, 416)]
                for i in posr:
                    if i[0] + 28 > pos[0] and i[0] < pos[0] + monster.rect.width and i[1] + 28 > pos[1] and \
                            i[1] < pos[1] + monster.rect.height:
                        pass
                    else:
                        found = False
                        position.set_position(pos)
            ennemies.append(monster)

    return ennemies
