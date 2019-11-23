from figure import Figure
from gameMap import GameMap
import random

class Target(Figure):
    
    targetHeight = 30
    targetWidth = 30

    def __init__(self, pozX, pozY):
        super().__init__(pozX, pozY, Target.targetWidth, Target.targetHeight)

    def __init__(self, map):
        pozX = random.randrange(0, map.width - Target.targetWidth)
        pozY = random.randrange(0, map.height - Target.targetHeight)
        super().__init__(pozX, pozY, Target.targetWidth, Target.targetHeight)
    
