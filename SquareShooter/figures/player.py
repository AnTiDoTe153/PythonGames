from figures.figure import Figure
from figures.bullet import Bullet
from map.direction import Direction
from map.gameMap import GameMap
from shootStyle.shootStyle import ShootStyle
from shootStyle.normalShooting import NormalShooting

class Player(Figure):
    def __init__(self, map, pozX, pozY, width, height, speed):
        super().__init__(map, pozX, pozY, width, height)
        self.speed = speed
        self.shootDelay = 0
        self.direction = Direction.RIGHT
        self.shootStyle = NormalShooting(self)

    def move(self, direction):
        self.moveOnDirection(direction)

    def shoot(self):
        self.shootStyle.shoot()

    def moveOnDirection(self, direction):
        if direction == Direction.UP:
            self.pozY -= self.speed
            self.direction = Direction.UP
        elif direction == Direction.DOWN:
            self.pozY += self.speed
            self.direction = Direction.DOWN
        elif direction == Direction.LEFT:
            self.pozX -= self.speed
            self.direction = Direction.LEFT
        elif direction == Direction.RIGHT:
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
