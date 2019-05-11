from pyengine import GameState
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button


class Menu(GameState):
    def __init__(self):
        super(Menu, self).__init__("Menu")

        self.title = Label([0, 0], "The Hope Of Flammy", (0, 0, 0), ["arial", 35])
        self.play = Button([170, 150], "Jouer", self.launch_game, [300, 100])
        self.quit = Button([170, 300], "Quitter", self.quit_game, [300, 100])

        self.title.set_position([320 - self.title.rect.width/2, 50])
        self.play.get_label().set_font(["arial", 30])
        self.play.update_all()
        self.quit.get_label().set_font(["arial", 30])
        self.quit.update_all()

        uisystem = self.world.get_system(UISystem)
        uisystem.add_widget(self.title)
        uisystem.add_widget(self.quit)
        uisystem.add_widget(self.play)

    def quit_game(self, button, click):
        self.window.stop()

    def launch_game(self, button, click):
        self.window.set_current_state("Jeu")