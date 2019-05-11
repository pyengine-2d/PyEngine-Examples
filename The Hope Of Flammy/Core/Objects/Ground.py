from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent


class Ground(Entity):
    def __init__(self):
        super(Ground, self).__init__()

        self.add_component(PositionComponent([0, 0]))
        self.add_component(SpriteComponent("Images/Decor/sol.png"))