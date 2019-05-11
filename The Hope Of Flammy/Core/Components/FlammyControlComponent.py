from pyengine.Components import ControlComponent, SpriteComponent, PositionComponent
from pyengine.Enums import ControlType, Controls
from pyengine import const

from Core.Others.FireShoot import FireShoot


class FlammyControlComponent(ControlComponent):
    def __init__(self):
        super(FlammyControlComponent, self).__init__(ControlType.FOURDIRECTION)
        self.vers = [0, 1]
        self.shoottimer = 0

    def keypress(self, evt):
        super(FlammyControlComponent, self).keypress(evt)
        sprite = self.entity.get_component(SpriteComponent)
        if evt.key == self.controles[Controls.UPJUMP]:
            sprite.set_sprite("Images/Flammy/FlammyH.png")
            self.vers = [0, -1]
        elif evt.key == self.controles[Controls.LEFT]:
            sprite.set_sprite("Images/Flammy/FlammyG.png")
            self.vers = [-1, 0]
        elif evt.key == self.controles[Controls.DOWN]:
            sprite.set_sprite("Images/Flammy/Flammy.png")
            self.vers = [0, 1]
        elif evt.key == self.controles[Controls.RIGHT]:
            sprite.set_sprite("Images/Flammy/FlammyD.png")
            self.vers = [1, 0]
        elif evt.key == const.K_SPACE and self.shoottimer <= 0:
            shoot = FireShoot(self.vers, self.entity.get_component(PositionComponent).get_position(),
                              self.entity.game)
            self.entity.system.add_entity(shoot)
            self.shoottimer = 10

    def update(self):
        super(FlammyControlComponent, self).update()
        self.shoottimer -= 1
