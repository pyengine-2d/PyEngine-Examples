from pyengine import Window, World
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button
from pyengine.Utils import Colors, Font, Vec2


class Menu:
    def __init__(self):
        # Création de la fenêtre. Taille : 300x200. Fond : Blanc. Title : "Menu".
        self.window = Window(300, 200, Colors.WHITE.value)
        self.window.title = "Menu"

        # Création de deux World : un pour le menu, l'autre pour le jeu
        self.gworld = World(self.window)
        self.mworld = World(self.window)

        # Création du jeu :
        #  - Un label "JEU" en 10, 10 de couleur noire et écrit en arial 18
        #  - Un bouton "Retour" en 10, 100 qui retourne au menu
        #  - Un bouton "Quitter" en 150, 100 qui quitte le jeu
        self.labeljeu = Label(Vec2(10, 10), "JEU", Colors.BLACK.value, Font("arial", 18))
        self.button1jeu = Button(Vec2(10, 50), "Retour", self.menu)
        self.button2jeu = Button(Vec2(150, 50), "Quitter", self.quitter)

        # Récupération de l'UISystem du monde du jeu et ajout des widgets
        self.uisystemjeu = self.gworld.get_system(UISystem)
        self.uisystemjeu.add_widget(self.labeljeu)
        self.uisystemjeu.add_widget(self.button1jeu)
        self.uisystemjeu.add_widget(self.button2jeu)

        # Création du menu :
        #  - Un label "Menu" en 10, 10 de couleur noire et écrit en arial 18 gras
        #  - Un bouton "Jouer" en 10, 100 qui va au jeu
        #  - Un bouton "Quitter" en 150, 100 qui quitte le jeu
        self.labelmenu = Label(Vec2(10, 10), "MENU", Colors.BLACK.value, Font("arial", 18, True))
        self.button1menu = Button(Vec2(10, 50), "Jouer", self.jouer)
        self.button2menu = Button(Vec2(150, 50), "Quitter", self.quitter)

        # Récupération de l'UISystem du monde du menu et ajout des widgets
        self.uisystemmenu = self.mworld.get_system(UISystem)
        self.uisystemmenu.add_widget(self.labelmenu)
        self.uisystemmenu.add_widget(self.button1menu)
        self.uisystemmenu.add_widget(self.button2menu)

        # Définition du World actuel à celui du menu et lancement de la fenêtre
        self.window.world = self.mworld
        self.window.run()

    # Fonction allant sur le menu
    def menu(self, widget, button):
        # Définition du World actuel à celui du menu
        self.window.world = self.mworld

    # Fonction allant sur le jeu
    def jouer(self, widget, button):
        # Définition du World actuel à celui du jeu
        self.window.world = self.gworld

    # Fonction quittant la fenêtre
    def quitter(self, widget, button):
        # Ferme la fenêtre
        self.window.stop()


# Lance le menu
Menu()
