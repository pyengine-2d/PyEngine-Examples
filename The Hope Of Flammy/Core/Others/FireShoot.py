from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent
from Core.Characters.Biggoutte import Biggoutte
from Core.Characters.Goutte import Goutte
from pyengine.Utils import Vec2


class FireShoot(Entity):
    def __init__(self, direction, position, game):
        super(FireShoot, self).__init__()

        self.game = game

        if direction == Vec2(1, 0):
            self.add_component(PositionComponent(Vec2(position.x+30, position.y+12)))
            self.add_component(SpriteComponent("Images/Flammy/Tir.png", 1, 270))
        elif direction == Vec2(-1, 0):
            self.add_component(PositionComponent(Vec2(position.x-20, position.y+12)))
            self.add_component(SpriteComponent("Images/Flammy/Tir.png", 1, 90))
        elif direction == Vec2(0, 1):
            self.add_component(PositionComponent(Vec2(position.x+6, position.y+40)))
            self.add_component(SpriteComponent("Images/Flammy/Tir.png", 1, 180))
        elif direction == Vec2(0, -1):
            self.add_component(PositionComponent(Vec2(position.x+6, position.y-20)))
            self.add_component(SpriteComponent("Images/Flammy/Tir.png"))
        phys = self.add_component(PhysicsComponent(False))
        phys.callback = self.collision
        self.add_component(MoveComponent(direction*5))

    def collision(self, obj, cause):
        if obj in self.game.ennemies:
            self.game.entitysystem.entities.remove(obj)
            self.game.entitysystem.entities.remove(self)
            del self.game.ennemies[self.game.ennemies.index(obj)]
            if type(obj) == Biggoutte:
                g = Goutte(self.game)
                g.get_component(PositionComponent).position = obj.get_component(PositionComponent).position
                self.game.entitysystem.add_entity(g)
                self.game.ennemies.append(g)
            if len(self.game.ennemies) == 0:
                self.game.door.open_door()
        elif type(obj) == type(self):
            self.game.entitysystem.entities.remove(self)
            self.game.entitysystem.entities.remove(obj)
        elif obj != self.game.flammy:
            self.game.entitysystem.entities.remove(self)
