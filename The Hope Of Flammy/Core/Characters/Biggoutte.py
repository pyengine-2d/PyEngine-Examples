from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent


class Biggoutte(Entity):
    def __init__(self, game):
        super(Biggoutte, self).__init__()

        self.game = game

        self.attack = 100

        self.add_component(PositionComponent([500, 400]))
        self.add_component(SpriteComponent("Images/Ennemi/Biggoutte.png"))
        phys = self.add_component(PhysicsComponent(False))
        phys.set_callback(self.collision)
        self.add_component(MoveComponent([0, 0], 1))

    def collision(self, obj, cause):
        if obj == self.game.flammy:
            self.game.flammy.collision(self, cause)

    def update(self):
        super(Biggoutte, self).update()
        posj = self.game.flammy.get_component(PositionComponent).get_position()
        pos = self.get_component(PositionComponent).get_position()
        direction = [0, 0]
        if posj[0] < pos[0]:
            direction[0] = -1
        elif posj[0] > pos[0]:
            direction[0] = 1
        if posj[1] < pos[1]:
            direction[1] = -1
        elif posj[1] > pos[1]:
            direction[1] = 1
        self.get_component(MoveComponent).set_direction(direction)
