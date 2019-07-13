from pyengine import Entity
from pyengine.Components import PositionComponent, SpriteComponent, PhysicsComponent, LifeComponent
from pyengine.Utils import Vec2

from Core.Components.FlammyControlComponent import FlammyControlComponent

from Core.Characters.Bougie import Bougie
from Core.Characters.Biggoutte import Biggoutte
from Core.Characters.Goutte import Goutte


class Flammy(Entity):
    def __init__(self, game):
        super(Flammy, self).__init__()

        self.game = game

        self.o2 = 300
        self.o2timer = 8

        self.add_component(PositionComponent(Vec2(32, 32)))
        self.add_component(SpriteComponent("Images/Flammy/Flammy.png"))
        self.add_component(FlammyControlComponent())
        phys = self.add_component(PhysicsComponent(False))
        phys.callback = self.collision
        self.add_component(LifeComponent(400))

    def collision(self, obj, cause):
        if obj in self.game.ennemies:
            life = self.get_component(LifeComponent)
            life.life = life.life - obj.attack
            self.game.entitysystem.entities.remove(obj)
            del self.game.ennemies[self.game.ennemies.index(obj)]
            if type(obj) == Biggoutte:
                g = Goutte(self.game)
                g.get_component(PositionComponent).position = obj.get_component(PositionComponent).position
                self.game.entitysystem.add_entity(g)
                self.game.ennemies.append(g)
            if len(self.game.ennemies) == 0:
                self.game.door.open_door()
        if obj in self.game.walls:
            posj = self.get_component(PositionComponent).position
            posp = self.game.door.get_component(PositionComponent).position
            if posj.x + 25 >= posp.x and posj.x <= posp.x+32:
                if not self.game.door.close:
                    self.game.next_level()

    def update(self):
        super(Flammy, self).update()

        life = self.get_component(LifeComponent)
        self.game.lifebarfront.size = Vec2(life.life, 32)
        if life.life == 0:
            self.game.loose()

        if self.o2timer <= 0 < self.o2:
            nbb = 0
            for i in self.game.ennemies:
                if type(i) == Bougie:
                    nbb += 1
            self.o2 -= 1 + nbb
            self.game.lifeo2front.size = Vec2(32, self.o2)
            self.game.lifeo2front.position = Vec2(608, 100+(300-self.o2))
            self.o2timer = 8
            if self.o2 == 0:
                self.game.loose()
        self.o2timer -= 1
