from figure import Figure
from gameMap import GameMap
from bullet import Bullet
from event import Event
import random

class Target(Figure, Event):
    
    targetHeight = 30
    targetWidth = 30
    maxHealth = 100

    def __init__(self, map, pozX = None, pozY = None):
        Event.__init__(self)
        if pozX == None:
            pozX = random.randrange(0, map.width - Target.targetWidth)
        if pozY == None:
           pozY = random.randrange(0, map.height - Target.targetHeight)

        Figure.__init__(self, map, pozX, pozY, Target.targetWidth, Target.targetHeight)

        self.health = Target.maxHealth

    def onCollision(self, figure):
        if isinstance(figure, Bullet):
            self.map.removeFigure(figure)
            if self.health <= 0:
                self.map.removeFigure(self)
                self.notify(None)
            else:
                self.health -= 10
