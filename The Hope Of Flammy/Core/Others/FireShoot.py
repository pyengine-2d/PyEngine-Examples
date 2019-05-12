from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent


class FireShoot(Entity):
    def __init__(self, direction, position, game):
        super(FireShoot, self).__init__()

        self.game = game

        if direction == [1, 0]:
            self.add_component(PositionComponent([position[0]+30, position[1]+12]))
            self.add_component(SpriteComponent("Images/Tirs/TirD.png"))
        elif direction == [-1, 0]:
            self.add_component(PositionComponent([position[0]-20, position[1]+12]))
            self.add_component(SpriteComponent("Images/Tirs/TirG.png"))
        elif direction == [0, 1]:
            self.add_component(PositionComponent([position[0]+6, position[1]+40]))
            self.add_component(SpriteComponent("Images/Tirs/TirB.png"))
        elif direction == [0, -1]:
            self.add_component(PositionComponent([position[0]+6, position[1]-20]))
            self.add_component(SpriteComponent("Images/Tirs/TirH.png"))
        phys = self.add_component(PhysicsComponent(False))
        phys.set_callback(self.collision)
        self.add_component(MoveComponent(direction))

    def collision(self, obj, cause):
        if obj in self.game.ennemies:
            self.game.entitysystem.entities.remove(obj)
            self.game.entitysystem.entities.remove(self)
            del self.game.ennemies[self.game.ennemies.index(obj)]
            if len(self.game.ennemies) == 0:
                self.game.door.open_door()
        elif type(obj) == type(self):
            self.game.entitysystem.entities.remove(self)
            self.game.entitysystem.entities.remove(obj)
        elif obj != self.game.flammy:
            self.game.entitysystem.entities.remove(self)
