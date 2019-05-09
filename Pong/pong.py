from pyengine import Window, GameState, Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, MoveComponent, ControlComponent
from pyengine.Enums import ControlType, Controls, WorldCallbacks
from pyengine.Components.ControlComponent import const
from pyengine.Systems import EntitySystem


class Jeu:
    def __init__(self):
        self.window = Window(800, 400, (255, 255, 255))
        self.window.set_title("Pong")

        self.game = GameState("GAME")
        self.window.add_state(self.game)

        self.world = self.game.get_world()
        self.world.set_callback(WorldCallbacks.OUTOFWINDOW, self.outofwindow)

        self.j1 = Entity()
        self.j1.add_component(PositionComponent([10, 175]))
        spritej1 = self.j1.add_component(SpriteComponent("images/texture.png"))
        spritej1.set_size([20, 50])
        controlj1 = self.j1.add_component(ControlComponent(ControlType.UPDOWN))
        controlj1.set_control(Controls.UPJUMP, const.K_w)
        controlj1.set_control(Controls.DOWN, const.K_s)
        self.j1.add_component(PhysicsComponent(False))

        self.j2 = Entity()
        self.j2.add_component(PositionComponent([770, 175]))
        spritej2 = self.j2.add_component(SpriteComponent("images/texture.png"))
        spritej2.set_size([20, 50])
        controlj2 = self.j2.add_component(ControlComponent(ControlType.UPDOWN))
        controlj2.set_control(Controls.UPJUMP, const.K_UP)
        controlj2.set_control(Controls.DOWN, const.K_DOWN)
        self.j2.add_component(PhysicsComponent(False))

        self.ball = Entity()
        self.ball.add_component(PositionComponent([390, 190]))
        spriteballe = self.ball.add_component(SpriteComponent("images/texture.png"))
        spriteballe.set_size([20, 20])
        physball = self.ball.add_component(PhysicsComponent(False))
        physball.set_callback(self.collision)
        self.ball.add_component(MoveComponent([1, 1]))

        entitysystem = self.world.get_system(EntitySystem)
        entitysystem.add_entity(self.j1)
        entitysystem.add_entity(self.j2)
        entitysystem.add_entity(self.ball)

        self.window.run()

    def collision(self, obj, cause):
        move = self.ball.get_component(MoveComponent)
        move.set_direction([-move.get_direction()[0], move.get_direction()[1]])

    def outofwindow(self, obj, pos):
        if obj == self.j1:
            position = self.j1.get_component(PositionComponent)
            if pos[1] <= 0:
                position.set_position([10, 0])
            else:
                position.set_position([10, 400])
        elif obj == self.j2:
            position = self.j2.get_component(PositionComponent)
            if pos[1] <= 0:
                position.set_position([770, 0])
            else:
                position.set_position([770, 400])
        else:
            if pos[0] < 10 or pos[0] > 790:
                position = self.ball.get_component(PositionComponent)
                position.set_position([390, 190])
            else:
                move = self.ball.get_component(MoveComponent)
                move.set_direction([move.get_direction()[0], -move.get_direction()[1]])


Jeu()
