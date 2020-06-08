from shootStyle.shootStyle import ShootStyle
from figures.figure import Figure
from figures.bullet import Bullet
from map.direction import Direction
import math 

class ShotgunShooting(ShootStyle):

    def __init__(self, figure):
        super().__init__(figure)
        self.shootDelay = 0
        self.shootingAngle = 3.14 / 8

    def shoot(self):
        if self.shootDelay == 0:
            playerDirection = self.figure.direction
            bullet = Bullet(self.figure.map, self.figure.pozX, self.figure.pozY, playerDirection)
            self.figure.map.addFigure(bullet)

            leftDir = Direction(playerDirection.dirX * math.cos(self.shootingAngle) - playerDirection.dirY * math.sin(self.shootingAngle), playerDirection.dirX * math.sin(self.shootingAngle) + playerDirection.dirY * math.cos(self.shootingAngle))
            leftBullet = Bullet(self.figure.map, self.figure.pozX, self.figure.pozY, leftDir)
            self.figure.map.addFigure(leftBullet)

            rightDir = Direction(playerDirection.dirX * math.cos(-self.shootingAngle) - playerDirection.dirY * math.sin(-self.shootingAngle), playerDirection.dirX * math.sin(-self.shootingAngle) + playerDirection.dirY * math.cos(-self.shootingAngle))
            rightBullet = Bullet(self.figure.map, self.figure.pozX, self.figure.pozY, rightDir)
            self.figure.map.addFigure(rightBullet)

            
            self.shootDelay = 20
        else:
            self.shootDelay -= 1