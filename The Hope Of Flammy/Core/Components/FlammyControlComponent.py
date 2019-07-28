from pyengine.Components import ControlComponent, SpriteComponent, PositionComponent
from pyengine import const, ControlType, Controls
from pyengine.Utils import Vec2

from Core.Others.FireShoot import FireShoot


class FlammyControlComponent(ControlComponent):
    def __init__(self):
        super(FlammyControlComponent, self).__init__(ControlType.FOURDIRECTION)
        self.vers = Vec2(0, 1)
        self.shoottimer = 0

    def movebykey(self, eventkey):
        print(eventkey)
        super(FlammyControlComponent, self).movebykey(eventkey)
        sprite = self.entity.get_component(SpriteComponent)
        if eventkey == self.controles[Controls.UPJUMP]:
            sprite.sprite = "Images/Flammy/FlammyH.png"
            self.vers = Vec2(0, -1)
        elif eventkey == self.controles[Controls.LEFT]:
            sprite.sprite = "Images/Flammy/FlammyG.png"
            self.vers = Vec2(-1, 0)
        elif eventkey == self.controles[Controls.DOWN]:
            sprite.sprite = "Images/Flammy/Flammy.png"
            self.vers = Vec2(0, 1)
        elif eventkey == self.controles[Controls.RIGHT]:
            sprite.sprite = "Images/Flammy/FlammyD.png"
            self.vers = Vec2(1, 0)
        elif eventkey == const.K_SPACE and self.shoottimer <= 0:
            shoot = FireShoot(self.vers, self.entity.get_component(PositionComponent).position,
                              self.entity.game)
            self.entity.system.add_entity(shoot)
            self.shoottimer = 10

    def update(self):
        super(FlammyControlComponent, self).update()
        self.shoottimer -= 1
