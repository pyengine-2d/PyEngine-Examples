from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent

from Core.Components.FlammyControlComponent import FlammyControlComponent


class Flammy(Entity):
    def __init__(self):
        super(Flammy, self).__init__()

        self.add_component(PositionComponent([100, 100]))
        self.add_component(SpriteComponent("Images/Flammy/Flammy.png"))
        self.add_component(FlammyControlComponent())
        self.add_component(PhysicsComponent(False))
