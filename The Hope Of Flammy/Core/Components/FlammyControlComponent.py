from pyengine.Components import ControlComponent
from pyengine.Enums import ControlType, Controls
from pyengine.Components import SpriteComponent


class FlammyControlComponent(ControlComponent):
    def __init__(self):
        super(FlammyControlComponent, self).__init__(ControlType.FOURDIRECTION)
        print("test")

    def keypress(self, evt):
        super(FlammyControlComponent, self).keypress(evt)
        sprite = self.entity.get_component(SpriteComponent)
        if evt.key == self.controles[Controls.UPJUMP]:
            sprite.set_sprite("Images/Flammy/FlammyH.png")
        elif evt.key == self.controles[Controls.LEFT]:
            sprite.set_sprite("Images/Flammy/FlammyG.png")
        elif evt.key == self.controles[Controls.DOWN]:
            sprite.set_sprite("Images/Flammy/Flammy.png")
        elif evt.key == self.controles[Controls.RIGHT]:
            sprite.set_sprite("Images/Flammy/FlammyD.png")

