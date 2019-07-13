from pyengine import World, MouseButton
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button
from pyengine.Utils import Vec2, Font


class Loose(World):
    def __init__(self, window):
        super(Loose, self).__init__(window)
        self.window = window

        self.uisys = self.get_system(UISystem)

        self.ltitle = Label(Vec2(), "Perdu...", font=Font(size=45))
        self.ltitle.position = Vec2(self.window.width/2 - self.ltitle.rect.width/2, 50)
        self.bplay = Button(Vec2(self.window.width/2 - 100, 170), "Rejouer", self.replay, Vec2(200, 70))
        self.bplay.label.font = Font(size=25)
        self.bstop = Button(Vec2(self.window.width/2 - 100, 320), "Quitter", self.stop, Vec2(200, 70))
        self.bstop.label.font = Font(size=25)

        self.uisys.add_widget(self.ltitle)
        self.uisys.add_widget(self.bplay)
        self.uisys.add_widget(self.bstop)

    def replay(self):
        self.window.world = self.window.game

    def stop(self):
        self.window.stop()
