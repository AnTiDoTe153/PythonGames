from direction import Direction
from figure import Figure
from gameMap import GameMap
from bullet import Bullet

class Player(Figure):
    def __init__(self, map, pozX, pozY, width, height, speed):
        super().__init__(map, pozX, pozY, width, height)
        self.speed = speed
        self.shootDelay = 0
        self.direction = Direction.RIGHT

    def move(self, direction):
        self.moveOnDirection(direction)

    def shoot(self):
        if self.shootDelay == 0:
            bullet = Bullet(self.map, self.pozX, self.pozY, self.direction)
            self.map.addFigure(bullet)
            self.shootDelay = 10
        else:
            self.shootDelay -= 1

    def moveOnDirection(self, direction):
        if direction == Direction.UP:
            self.pozY -= self.speed
            self.direction = Direction.UP
        if direction == Direction.DOWN:
            self.pozY += self.speed
            self.direction = Direction.DOWN
        if direction == Direction.LEFT:
            self.pozX -= self.speed
            self.direction = Direction.LEFT
        if direction == Direction.RIGHT:
            self.pozX += self.speed
            self.direction = Direction.RIGHT

        self.correctPosition()

    def setDirection(self, direction):
        self.direction = direction

    def correctPosition(self):
        self.pozY = max(self.height // 2, self.pozY)
        self.pozY = min(self.map.height - self.height // 2, self.pozY)

        self.pozX = max(self.width // 2, self.pozX)
        self.pozX = min(self.map.width - self.width // 2, self.pozX)
