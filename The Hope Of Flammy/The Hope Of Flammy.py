from pyengine import Window
from pyengine.Utils import Colors

from Core.Menu import Menu
from Core.Game import Game
from Core.Win import Win
from Core.Loose import Loose

window = Window(640, 480, Colors.WHITE.value)
window.set_title("The Hope Of Flammy")

menu = Menu()
jeu = Game()
win = Win()
loose = Loose()

window.add_state(jeu)
window.add_state(menu)
window.add_state(win)
window.add_state(loose)

window.set_current_state("Menu")
window.run()
