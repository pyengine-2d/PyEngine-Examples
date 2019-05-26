from pyengine import GameState
from pyengine.Systems import UISystem
from pyengine.Widgets import Label
from pyengine.Utils import Font, Color


class Loose(GameState):
    def __init__(self):
        super(Loose, self).__init__("Loose")

        l1 = Label([0, 0], "Dommage...", Color(0, 0, 0), Font("arial", 30))
        l2 = Label([0, 0], "Vous avez perdu.", Color(0, 0, 0), Font("arial", 30))

        l1.set_position([320 - l1.rect.width / 2, 190])
        l2.set_position([320 - l2.rect.width / 2, 230])

        uisystem = self.get_system(UISystem)
        uisystem.add_widget(l1)
        uisystem.add_widget(l2)
