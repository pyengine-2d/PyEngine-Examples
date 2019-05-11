from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, LifeBarComponent

from Core.Components.FlammyControlComponent import FlammyControlComponent


class Flammy(Entity):
    def __init__(self, game):
        super(Flammy, self).__init__()

        self.game = game

        self.o2 = 300
        self.o2timer = 10

        self.add_component(PositionComponent([100, 100]))
        self.add_component(SpriteComponent("Images/Flammy/Flammy.png"))
        self.add_component(FlammyControlComponent())
        phys = self.add_component(PhysicsComponent(False))
        phys.set_callback(self.collision)
        self.add_component(LifeBarComponent(400))

    def collision(self, obj, cause):
        if obj in self.game.ennemies:
            life = self.get_component(LifeBarComponent)
            life.update_life(life.life - obj.attack)
            self.game.entitysystem.entities.remove(obj)
            del self.game.ennemies[self.game.ennemies.index(obj)]

    def update(self):
        super(Flammy, self).update()

        life = self.get_component(LifeBarComponent)
        self.game.lifebarfront.set_size([life.life, 32])

        if self.o2timer <= 0 < self.o2:
            self.o2 -= 1
            self.game.lifeo2front.set_size([32, self.o2])
            self.game.lifeo2front.set_position([608, 100+(300-self.o2)])
            self.o2timer = 10
        self.o2timer -= 1
