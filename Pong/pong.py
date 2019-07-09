from pyengine import Window, Entity, const, Controls, ControlType, WindowCallbacks
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent, ControlComponent
from pyengine.Systems import EntitySystem
from pyengine.Utils import Colors, Vec2
from random import randint


class Jeu:
    def __init__(self):
        # Création de la fenêtre de jeu de taille 800x400, de fond blanc et titre "Pong"
        self.window = Window(800, 400, Colors.WHITE.value)
        self.window.title = "Pong"

        # Définition du callback OUTOFWINDOW
        self.window.set_callback(WindowCallbacks.OUTOFWINDOW, self.outofwindow)

        # Création de l'entité pour la barre du joueur à gauche avec :
        #  - Un PositionComponent avec les positions 10, 175
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 50
        #  - Un ControlComponent avec un ControlType UPDOWN auquel on définit les touches à Z et S (azerty)
        #  - Un PhysicsComponent sans l'affection par la gravité
        self.j1 = Entity()
        self.j1.add_component(PositionComponent(Vec2(10, 175)))
        spritej1 = self.j1.add_component(SpriteComponent("images/texture.png"))
        spritej1.size = Vec2(20, 50)
        controlj1 = self.j1.add_component(ControlComponent(ControlType.UPDOWN))
        controlj1.set_control(Controls.UPJUMP, const.K_w)
        controlj1.set_control(Controls.DOWN, const.K_s)
        self.j1.add_component(PhysicsComponent(False))

        # Création de l'entité pour la barre du joueur à droite avec :
        #  - Un PositionComponent avec les positions 770, 175
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 50
        #  - Un ControlComponent avec un ControlType UPDOWN auquel on définit les touches aux flèches haut et bas
        #  - Un PhysicsComponent sans l'affection par la gravité
        self.j2 = Entity()
        self.j2.add_component(PositionComponent(Vec2(770, 175)))
        spritej2 = self.j2.add_component(SpriteComponent("images/texture.png"))
        spritej2.size = Vec2(20, 50)
        controlj2 = self.j2.add_component(ControlComponent(ControlType.UPDOWN))
        controlj2.set_control(Controls.UPJUMP, const.K_UP)
        controlj2.set_control(Controls.DOWN, const.K_DOWN)
        self.j2.add_component(PhysicsComponent(False))

        # Création de l'entité pour la balle avec :
        #  - Un PositionComponent avec les positions 390, 190
        #  - Un SpriteComponent avec le sprite texture.png que l'on redimensionne en 20, 20
        #  - Un PhysicsComponent sans l'affection par la gravité dont on définit le callback de collision
        #  - Un MoveComponent avec comme direction random
        self.ball = Entity()
        self.ball.add_component(PositionComponent(Vec2(390, 190)))
        spriteballe = self.ball.add_component(SpriteComponent("images/texture.png"))
        spriteballe.size = Vec2(20, 20)
        physball = self.ball.add_component(PhysicsComponent(False))
        physball.callback = self.collision
        self.ball.add_component(MoveComponent(Vec2(randint(1, 5), randint(1, 5))))

        # Ajout des entités au monde via l'EntitySystem
        entitysystem = self.window.world.get_system(EntitySystem)
        entitysystem.add_entity(self.j1)
        entitysystem.add_entity(self.j2)
        entitysystem.add_entity(self.ball)

        # Lancement du jeu
        self.window.run()

    # Callback de collision
    # Activé quand la balle rencontre un joueur (étant les seuls autre entités)
    def collision(self, obj, cause):
        # On récupère le MoveComponent de la balle pour inverser sa direction en x
        move = self.ball.get_component(MoveComponent)
        move.direction = Vec2(-move.direction.x, move.direction.y)

    # Callback OUTOFWINDOW
    # Activé quand un élément sort de l'écran
    def outofwindow(self, obj, pos):
        # Si notre objet est le joueur 1
        if obj == self.j1:
            # On récupère le PositionComponent du J1 pour le "bloquer" dans l'écran
            position = self.j1.get_component(PositionComponent)
            if pos.y <= 0:
                position.position = Vec2(10, 0)
            else:
                position.position = Vec2(10, 350)

        # Si notre objet est le joueur 2
        elif obj == self.j2:
            # On récupère le PositionComponent du J2 pour le "bloquer" dans l'écran
            position = self.j2.get_component(PositionComponent)
            if pos.y <= 0:
                position.position = Vec2(770, 0)
            else:
                position.position = Vec2(770, 350)

        # Si notre objet est la balle
        else:
            # Si la balle sort de l'écran sur les cotés
            if pos.x < 10 or pos.x > 790:
                # On replace la balle au centre
                position = self.ball.get_component(PositionComponent)
                position.position = Vec2(390, 190)
                self.ball.get_component(MoveComponent).direction = Vec2(randint(1, 5), randint(1, 5))
            # Si la balle sort de l'écran par le haut
            else:
                # On inverse la direction y du movement de la base
                move = self.ball.get_component(MoveComponent)
                move.direction = Vec2(move.direction.x, -move.direction.y)


# Lancement du jeu
Jeu()
