from pyengine import GameState
from pyengine.Systems import EntitySystem, UISystem
from pyengine.Widgets import Image

from Core.Characters.Flammy import Flammy
from Core.Characters.Goutte import Goutte
from Core.Objects.Wall import Wall
from Core.Objects.Ground import Ground


class Game(GameState):
    def __init__(self):
        super(Game, self).__init__("Jeu")

        self.entitysystem = self.world.get_system(EntitySystem)
        self.uisystem = self.world.get_system(UISystem)

        self.flammy = Flammy(self)
        self.walls = [Wall(0), Wall(1), Wall(2), Wall(3)]
        self.door = Door()
        self.ennemies = [Goutte(self)]
        self.ground = Ground()

        for i in self.walls:
            self.entitysystem.add_entity(i)
        self.entitysystem.add_entity(self.ground)
        self.entitysystem.add_entity(self.door)
        for i in self.ennemies:
            self.entitysystem.add_entity(i)
        self.entitysystem.add_entity(self.flammy)

        lifebarback = Image([100, 0], "Images/Barres/BarredeVieF.png")
        self.lifebarfront = Image([100, 0], "Images/Barres/BarredeVie.png")
        lifeo2back = Image([608, 100], "Images/Barres/BarredeO2F.png")
        self.lifeo2front = Image([608, 100], "Images/Barres/BarredeO2.png")

        self.uisystem.add_widget(lifebarback)
        self.uisystem.add_widget(lifeo2back)
        self.uisystem.add_widget(self.lifebarfront)
        self.uisystem.add_widget(self.lifeo2front)

    def next_level(self):
        if self.level == self.nblevel:
            self.window.set_current_state("Win")
        else:
            self.level += 1


