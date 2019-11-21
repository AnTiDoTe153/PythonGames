from direction import Direction
from figure import Figure
from gameMap import GameMap

class MovableFigure(Figure):
    def __init__(self, pozX, pozY, width, height, speed):
        super().__init__(pozX, pozY, width, height)
        self.speed = speed

    def move(self, direction, map):
        self.moveOnDirection(direction, map)

    def moveOnDirection(self, direction, map):
        if direction == Direction.UP:
            self.pozY -= self.speed
        if direction == Direction.DOWN:
            self.pozY += self.speed
        if direction == Direction.LEFT:
            self.pozX -= self.speed
        if direction == Direction.RIGHT:
            self.pozX += self.speed

        self.correctPosition(map)

    

    def correctPosition(self, map):
        self.pozY = max(0, self.pozY)
        self.pozY = min(map.height - self.height, self.pozY)

        self.pozX = max(0, self.pozX)
        self.pozX = min(map.width - self.width, self.pozX)
