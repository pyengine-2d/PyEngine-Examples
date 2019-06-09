from pyengine import World
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Widgets import Image
from pyengine.Components import PositionComponent
from pyengine.Utils import Vec2

from random import randint

from Core.Characters.Flammy import Flammy
from Core.Objects.Wall import Wall
from Core.Objects.Rock import Rock
from Core.Objects.Ground import Ground
from Core.Objects.Door import Door

from Core.Utils import gen_pos, gen_ennemies


class Game(World):
    def __init__(self, game):
        super(Game, self).__init__(game.window)

        self.game = game

        self.entitysystem = self.get_system(EntitySystem)
        self.uisystem = self.get_system(UISystem)
        self.nblevel = 10
        self.level = 1

        self.flammy = Flammy(self)
        self.walls = [Wall(0), Wall(1), Wall(2), Wall(3)]
        self.door = Door()
        self.ground = Ground()
        self.rocks = []
        self.ennemies = []

        lifebarback = Image(Vec2(100, 0), "Images/Barres/BarredeVieF.png")
        self.lifebarfront = Image(Vec2(100, 0), "Images/Barres/BarredeVie.png")
        lifeo2back = Image(Vec2(608, 100), "Images/Barres/BarredeO2F.png")
        self.lifeo2front = Image(Vec2(608, 100), "Images/Barres/BarredeO2.png")

        for i in self.walls:
            self.entitysystem.add_entity(i)
        self.entitysystem.add_entity(self.ground)
        self.entitysystem.add_entity(self.door)
        self.create_level(self.level)
        self.entitysystem.add_entity(self.flammy)

        self.uisystem.add_widget(lifebarback)
        self.uisystem.add_widget(lifeo2back)
        self.uisystem.add_widget(self.lifebarfront)
        self.uisystem.add_widget(self.lifeo2front)

    def create_level(self, nb):
        for i in self.rocks:
            self.entitysystem.entities.remove(i)
        for i in self.ennemies:
            self.entitysystem.entities.remove(i)

        self.flammy.get_component(PositionComponent).position = Vec2(32, 32)
        self.flammy.o2 = 300
        self.lifeo2front.size = [32, 300]
        self.lifeo2front.position = Vec2(608, 100)
        self.door.close_door()

        self.rocks = []
        self.ennemies = []
        posr = gen_pos(randint(2, 7))
        for i in posr:
            self.rocks.append(Rock(i))
        for i in gen_ennemies(posr, randint(2, 11)*nb, self):
            self.ennemies.append(i)
        for i in self.rocks:
            self.entitysystem.add_entity(i)
        for i in self.ennemies:
            self.entitysystem.add_entity(i)

    def next_level(self):
        if self.level == self.nblevel:
            self.window.world = self.game.win
        else:
            self.level += 1
            self.create_level(self.level)

    def loose(self):
        self.window.world = self.game.loose



