from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent
from pyengine.Utils import Vec2


class Wall(Entity):
    def __init__(self, rotate):
        super(Wall, self).__init__()

        self.rotation = rotate
        if rotate == 0:
            self.add_component(PositionComponent(Vec2(0, 0)))
            self.add_component(SpriteComponent("Images/Decor/Mur.png"))
        elif rotate == 1:
            self.add_component(PositionComponent(Vec2(608, 0)))
            self.add_component(SpriteComponent("Images/Decor/Mur.png", 1, 90))
        elif rotate == 2:
            self.add_component(PositionComponent(Vec2(32, 448)))
            self.add_component(SpriteComponent("Images/Decor/Mur.png", 1, 180))
        elif rotate == 3:
            self.add_component(PositionComponent(Vec2(0, 32)))
            self.add_component(SpriteComponent("Images/Decor/Mur.png", 1, 270))
        else:
            raise ValueError("Rotation of Wall must be 0, 1, 2 or 3")
        self.add_component(PhysicsComponent(False))
