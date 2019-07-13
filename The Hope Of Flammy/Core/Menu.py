from pyengine import World
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button
from pyengine.Utils import Colors, Font, Vec2


class Menu(World):
    def __init__(self, game):
        super(Menu, self).__init__(game.window)

        self.game = game
        self.title = Label(Vec2(0, 0), "The Hope Of Flammy", Colors.BLACK.value, Font("arial", 35))
        self.play = Button(Vec2(170, 150), "Jouer", self.launch_game, Vec2(300, 100))
        self.quit = Button(Vec2(170, 300), "Quitter", self.quit_game, Vec2(300, 100))

        self.title.position = Vec2(320 - self.title.rect.width/2, 50)
        self.play.label.font = Font("arial", 30)
        self.quit.label.font = Font("arial", 30)

        uisystem = self.get_system(UISystem)
        uisystem.add_widget(self.title)
        uisystem.add_widget(self.quit)
        uisystem.add_widget(self.play)

    def quit_game(self):
        self.window.stop()

    def launch_game(self):
        self.window.world = self.game.jeu
