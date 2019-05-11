from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent


class Wall(Entity):
    def __init__(self, rotate):
        super(Wall, self).__init__()

        self.rotation = rotate
        if rotate == 0:
            self.add_component(PositionComponent([0, 0]))
            self.add_component(SpriteComponent("Images/Decor/Mur.png"))
        elif rotate == 1:
            self.add_component(PositionComponent([608, 0]))
            self.add_component(SpriteComponent("Images/Decor/Mur1.png"))
        elif rotate == 2:
            self.add_component(PositionComponent([32, 448]))
            self.add_component(SpriteComponent("Images/Decor/Mur2.png"))
        elif rotate == 3:
            self.add_component(PositionComponent([0, 32]))
            self.add_component(SpriteComponent("Images/Decor/Mur3.png"))
        else:
            raise ValueError("Rotation of Wall must be 0, 1, 2 or 3")
        self.add_component(PhysicsComponent(False))
