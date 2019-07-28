from pyengine.Entities import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent


class Block(Entity):
    def __init__(self, sprite, pos):
        super(Block, self).__init__()

        self.add_component(PositionComponent(pos))
        sprite = self.add_component(SpriteComponent(sprite))
        sprite.scale = 0.4
        self.add_component(PhysicsComponent(False))
