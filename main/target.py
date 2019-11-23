from figure import Figure
from gameMap import GameMap
from bullet import Bullet
from event import Event
import random

class Target(Figure, Event):
    
    targetHeight = 30
    targetWidth = 30

    def __init__(self, map, pozX, pozY):
        Event.__init__()
        Figure.__init__(map, pozX, pozY, Target.targetWidth, Target.targetHeight)

    def __init__(self, map):
        Event.__init__(self)
        pozX = random.randrange(0, map.width - Target.targetWidth)
        pozY = random.randrange(0, map.height - Target.targetHeight)
        Figure.__init__(self, map, pozX, pozY, Target.targetWidth, Target.targetHeight)

    def onCollision(self, figure):
        self.map.removeFigure(self)
        self.notify(None)
