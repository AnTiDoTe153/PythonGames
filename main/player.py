from direction import Direction
from figure import Figure
from gameMap import GameMap
from bullet import Bullet

class Player(Figure):
    def __init__(self, pozX, pozY, width, height, speed):
        super().__init__(pozX, pozY, width, height)
        self.speed = speed
        self.shootDelay = 0
        self.direction = Direction.RIGHT

    def move(self, direction, map):
        self.moveOnDirection(direction, map)

    def shoot(self, map):
        
        if self.shootDelay == 0:
            bullet = Bullet(self.pozX, self.pozY, self.direction)
            map.addFigure(bullet)
            self.shootDelay = 10
        else:
            self.shootDelay -= 1
        

    def moveOnDirection(self, direction, map):
        if direction == Direction.UP:
            self.pozY -= self.speed
        if direction == Direction.DOWN:
            self.pozY += self.speed
        if direction == Direction.LEFT:
            self.pozX -= self.speed
            self.direction = Direction.LEFT
        if direction == Direction.RIGHT:
            self.pozX += self.speed
            self.direction = Direction.RIGHT

        self.correctPosition(map)

    def correctPosition(self, map):
        self.pozY = max(0, self.pozY)
        self.pozY = min(map.height - self.height, self.pozY)

        self.pozX = max(0, self.pozX)
        self.pozX = min(map.width - self.width, self.pozX)
