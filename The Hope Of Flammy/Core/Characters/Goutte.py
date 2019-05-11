from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent


class Goutte(Entity):
    def __init__(self, game):
        super(Goutte, self).__init__()

        self.game = game

        self.add_component(PositionComponent([150, 150]))
        self.add_component(SpriteComponent("Images/Ennemi/Goutte.png"))
        self.add_component(PhysicsComponent(False))
        self.add_component(MoveComponent([0, 0], 2))

    def update(self):
        super(Goutte, self).update()
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
