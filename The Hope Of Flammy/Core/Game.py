from pyengine import GameState
from pyengine.Systems import EntitySystem

from Core.Characters.Flammy import Flammy
from Core.Characters.Goutte import Goutte
from Core.Objects.Wall import Wall
from Core.Objects.Ground import Ground


class Game(GameState):
    def __init__(self):
        super(Game, self).__init__("Jeu")

        self.flammy = Flammy()
        self.walls = [Wall(0), Wall(1), Wall(2), Wall(3)]
        self.ennemies = [Goutte(self)]
        self.ground = Ground()

        entitysystem = self.world.get_system(EntitySystem)
        for i in self.walls:
            entitysystem.add_entity(i)
        entitysystem.add_entity(self.ground)
        for i in self.ennemies:
            entitysystem.add_entity(i)
        entitysystem.add_entity(self.flammy)



