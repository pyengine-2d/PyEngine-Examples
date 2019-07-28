from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent
from pyengine.Utils import Vec2


class Goutte(Entity):
    def __init__(self, game):
        super(Goutte, self).__init__()

        self.game = game

        self.attack = 50

        self.add_component(PositionComponent(Vec2(500, 400)))
        self.add_component(SpriteComponent("Images/Ennemi/Goutte.png"))
        phys = self.add_component(PhysicsComponent(False))
        phys.callback = self.collision
        self.add_component(MoveComponent(Vec2(0, 0)))

    def collision(self, obj, cause):
        if obj == self.game.flammy:
            self.game.flammy.collision(self, cause)

    def update(self):
        super(Goutte, self).update()
        posj = self.game.flammy.get_component(PositionComponent).position
        pos = self.get_component(PositionComponent).position
        direction = Vec2()
        if posj.x < pos.x:
            direction.x = -1
        elif posj.x > pos.x:
            direction.x = 1
        if posj.y < pos.y:
            direction.y = -1
        elif posj.y > pos.y:
            direction.y = 1
        self.get_component(MoveComponent).direction = direction
