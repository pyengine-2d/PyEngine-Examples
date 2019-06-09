from pyengine import Window
from pyengine.Utils import Colors

from Core.Menu import Menu
from Core.Game import Game
from Core.Win import Win
from Core.Loose import Loose


class Main:
    def __init__(self):
        self.window = Window(640, 480, Colors.WHITE.value)
        self.window.title = "The Hope Of Flammy"

        self.menu = Menu(self)
        self.jeu = Game(self)
        self.win = Win(self)
        self.loose = Loose(self)

        self.window.world = self.menu
        self.window.run()

Main()
