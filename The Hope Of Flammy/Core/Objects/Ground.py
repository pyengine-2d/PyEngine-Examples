from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent
from pyengine.Utils import Vec2


class Ground(Entity):
    def __init__(self):
        super(Ground, self).__init__()

        self.add_component(PositionComponent(Vec2()))
        self.add_component(SpriteComponent("Images/Decor/sol.png"))
