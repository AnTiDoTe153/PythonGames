from figures.figure import Figure
from map.gameMap import GameMap

class Bomb(Figure):

    def __init__(self, map, pozX, pozY):
        super().__init__(map, pozX, pozY, 20, 20)
        self.speed = 0 