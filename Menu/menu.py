from pyengine import Window, GameState
from pyengine.Systems import UISystem
from pyengine.Widgets import Label, Button
from pyengine.Utils import Color, Font


class Menu:
    def __init__(self):
        # Création de la fenêtre. Taille : 300x200. Fond : Blanc. Title : "Menu".
        self.window = Window(300, 200, (255, 255, 255))
        self.window.set_title("Menu")

        # Création de deux GameStates : un pour le menu, l'autre pour le jeu
        self.gamestate = GameState("Jeu")
        self.menustate = GameState("Menu")
        self.window.add_state(self.gamestate)
        self.window.add_state(self.menustate)

        # Création du jeu :
        #  - Un label "JEU" en 10, 10 de couleur noire et écrit en arial 18
        #  - Un bouton "Retour" en 10, 100 qui retourne au menu
        #  - Un bouton "Quitter" en 150, 100 qui quitte le jeu
        self.labeljeu = Label([10, 10], "JEU", Color(0, 0, 0), Font("arial", 18))
        self.button1jeu = Button([10, 100], "Retour", self.menu)
        self.button2jeu = Button([150, 100], "Quitter", self.quitter)

        # Récupération de l'UISystem du monde du jeu et ajout des widgets
        self.uisystemjeu = self.gamestate.get_system(UISystem)
        self.uisystemjeu.add_widget(self.labeljeu)
        self.uisystemjeu.add_widget(self.button1jeu)
        self.uisystemjeu.add_widget(self.button2jeu)

        # Création du menu :
        #  - Un label "Menu" en 10, 10 de couleur noire et écrit en arial 18 gras
        #  - Un bouton "Jouer" en 10, 100 qui va au jeu
        #  - Un bouton "Quitter" en 150, 100 qui quitte le jeu
        self.labelmenu = Label([10, 10], "MENU", Color(0, 0, 0), Font("arial", 18, True))
        self.button1menu = Button([10, 50], "Jouer", self.jouer)
        self.button2menu = Button([150, 50], "Quitter", self.quitter)

        # Récupération de l'UISystem du monde du menu et ajout des widgets
        self.uisystemmenu = self.menustate.get_system(UISystem)
        self.uisystemmenu.add_widget(self.labelmenu)
        self.uisystemmenu.add_widget(self.button1menu)
        self.uisystemmenu.add_widget(self.button2menu)

        # Définition de la GameState actuelle à celle du menu et lancement de la fenêtre
        self.window.set_current_state("Menu")
        self.window.run()

    # Fonction allant sur le menu
    def menu(self, widget, button):
        # Définition de la GameState actuelle à celle du menu
        self.window.set_current_state("Menu")

    # Fonction allant sur le jeu
    def jouer(self, widget, button):
        # Définition de la GameState actuelle à celle du jeu
        self.window.set_current_state("Jeu")

    # Fonction quittant la fenêtre
    def quitter(self, widget, button):
        # Ferme la fenêtre
        self.window.stop()


# Lance le menu
Menu()
