from pyengine import World
from pyengine.Systems import UISystem
from pyengine.Widgets import Label
from pyengine.Utils import Font, Colors, Vec2


class Loose(World):
    def __init__(self, game):
        super(Loose, self).__init__(game.window)

        l1 = Label(Vec2(), "Dommage...", Colors.BLACK.value, Font("arial", 30))
        l2 = Label(Vec2(), "Vous avez perdu.", Colors.BLACK.value, Font("arial", 30))

        l1.position = Vec2(320 - l1.rect.width / 2, 190)
        l2.position = Vec2(320 - l2.rect.width / 2, 230)

        uisystem = self.get_system(UISystem)
        uisystem.add_widget(l1)
        uisystem.add_widget(l2)
