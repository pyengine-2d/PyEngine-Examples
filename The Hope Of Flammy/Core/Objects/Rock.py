from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent


class Rock(Entity):
    def __init__(self, position):
        super(Rock, self).__init__()

        self.add_component(PositionComponent(position))
        self.add_component(SpriteComponent("Images/Decor/Caillou.png", 2))
        self.add_component(PhysicsComponent(False))
