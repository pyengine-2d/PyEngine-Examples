from pyengine import Window, WindowCallbacks

from Core.Menu import Menu
from Core.Game import Game
from Core.Win import Win
from Core.Loose import Loose


class NightDev(Window):
    def __init__(self):
        super(NightDev, self).__init__(700, 500, title="Game")

        self.menu = Menu(self)
        self.game = Game(self)
        self.win = Win(self)
        self.loose = Loose(self)

        self.world = self.menu

        self.set_callback(WindowCallbacks.OUTOFWINDOW, self.game.outofwindow)

        self.run()


NightDev()


