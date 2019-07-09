from pyengine import Entity, ControlType
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, ControlComponent


class Player(Entity):
    def __init__(self, game, pos):
        super(Player, self).__init__()

        self.game = game

        self.add_component(PositionComponent(pos))
        sprite = self.add_component(SpriteComponent("Assets/Character/idle.png"))
        sprite.scale = 0.3
        phys = self.add_component(PhysicsComponent())
        phys.callback = self.collision
        self.add_component(ControlComponent(ControlType.CLASSICJUMP))

    def set_pos(self, pos):
        self.get_component(PositionComponent).position = pos

    def collision(self, e, cinfos):
        if e.get_component(SpriteComponent).sprite == "Assets/Tiles/Chest.png":
            self.game.end_level()
        elif e.get_component(SpriteComponent).sprite == "Assets/Obstacles/Saw.png":
            self.game.loose()
