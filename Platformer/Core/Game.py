from pyengine import World
from pyengine.Systems import EntitySystem
from pyengine.Utils import Vec2

import json

from Core.Objects.Player import Player
from Core.Objects.Blocks import Block


class Game(World):
    def __init__(self, window):
        super(Game, self).__init__(window)
        self.level = 1
        self.maxlevel = 2

        self.esys = self.get_system(EntitySystem)

        self.player = Player(self, Vec2(10, 10))
        self.esys.add_entity(self.player)

        self.blocks = []

        self.load_level()

    def outofwindow(self, e, pos):
        if e == self.player:
            with open("Levels/" + str(self.level) + ".json", "r") as f:
                datas = json.load(f)
            pos = Vec2()
            pos.coords = datas["player"]
            self.player.set_pos(pos)

    def loose(self):
        self.level = 1
        self.load_level()

        self.window.world = self.window.loose

    def load_level(self):
        for i in self.blocks:
            self.esys.remove_entity(i)
        self.blocks = []

        with open("Levels/"+str(self.level)+".json", "r") as f:
            datas = json.load(f)
        pos = Vec2()
        pos.coords = datas["player"]

        for k, v in datas["blocks"].items():
            if k == "grass":
                sprite = "Assets/Tiles/Grass.png"
            elif k == "treasure":
                sprite = "Assets/Tiles/Chest.png"
            elif k == "saw":
                sprite = "Assets/Obstacles/Saw.png"
            else:
                print("Unknown block : "+k)
                break
            for i in v:
                p = Vec2()
                p.coords = i
                self.blocks.append(Block(sprite, p))

        for i in self.blocks:
            self.esys.add_entity(i)
        self.player.set_pos(pos)

    def end_level(self):
        if self.maxlevel == self.level:
            self.level = 1
            self.load_level()

            self.window.world = self.window.win
        else:
            self.level += 1
            self.load_level()
