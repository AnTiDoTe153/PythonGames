from figures.figure import Figure
from figures.bullet import Bullet
from figures.bomb import Bomb
from map.direction import Direction
from map.gameMap import GameMap
from shootStyle.shootStyle import ShootStyle
from shootStyle.normalShooting import NormalShooting
from shootStyle.shotgunShooting import ShotgunShooting

class Player(Figure):
    def __init__(self, map, pozX, pozY, width, height, speed):
        super().__init__(map, pozX, pozY, width, height)
        self.speed = speed
        self.bombDelay = 0
        self.direction = Direction(1, 0)
        self.shootStyle = ShotgunShooting(self)

    def move(self, direction):
        self.moveOnDirection(direction)

    def shoot(self):
        self.shootStyle.shoot()

    def placeBomb(self):
        if self.bombDelay == 0:
            bomb = Bomb(self.map, self.pozX, self.pozY)
            self.map.addFigure(bomb)
            self.bombDelay = 50

    def moveOnDirection(self, direction):
        self.pozX += self.speed * direction.dirX
        self.pozY += self.speed * direction.dirY

        self.correctPosition()

    def setDirection(self, direction):
        self.direction = direction

    def correctPosition(self):
        self.pozY = max(self.height // 2, self.pozY)
        self.pozY = min(self.map.height - self.height // 2, self.pozY)

        self.pozX = max(self.width // 2, self.pozX)
        self.pozX = min(self.map.width - self.width // 2, self.pozX)

    def update(self):
        if self.bombDelay > 0:
            self.bombDelay -= 1
