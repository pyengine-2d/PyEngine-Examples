from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent
from random import randint


class Door(Entity):
    def __init__(self):
        super(Door, self).__init__()

        self.close = True

        self.add_component(PositionComponent([randint(50, 590), 0]))
        self.add_component(SpriteComponent("Images/Decor/PorteF.png"))
        self.add_component(PhysicsComponent(False))

    def open_door(self):
        self.get_component(SpriteComponent).set_sprite("Images/Decor/PorteO.png")
        self.close = False

    def close_door(self):
        self.get_component(SpriteComponent).set_sprite("Images/Decor/PorteF.png")
        self.close = True
