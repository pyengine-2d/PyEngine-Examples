from pyengine import Window

from Core.Menu import Menu
from Core.Game import Game

window = Window(640, 480, (255, 255, 255))
window.set_title("The Hope Of Flammy")

menu = Menu()
jeu = Game()

window.add_state(jeu)
window.add_state(menu)

window.set_current_state("Menu")
window.run()