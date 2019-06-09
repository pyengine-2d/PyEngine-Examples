from random import randint
from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2

from Core.Characters.Goutte import Goutte
from Core.Characters.Biggoutte import Biggoutte
from Core.Characters.Bougie import Bougie


def gen_pos(nb):
    pos = []
    while nb:
        p = Vec2(randint(64, 576), randint(64, 416))
        found = False
        for i in pos:
            if i.x+28 > p.x and i.x < p.x+28 and i.y+28 > p.y and i.y < p.y+28:
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
        if score >= 8:
            monster = Biggoutte(game)
            score -= 8
        elif score >= 5:
            monster = Goutte(game)
            score -= 5
        elif score >= 2:
            monster = Bougie(game)
            score -= 2
        else:
            score = 0
        if monster:
            found = True
            while found:
                position = monster.get_component(PositionComponent)
                pos = Vec2(randint(64, 576), randint(64, 416))
                for i in posr:
                    if i.x + 28 > pos.x and i.x < pos.x + monster.rect.width and i.y + 28 > pos.y and \
                            i.y < pos.y + monster.rect.height:
                        pass
                    else:
                        found = False
                        position.position = pos
            ennemies.append(monster)

    return ennemies
