from shootStyle.shootStyle import ShootStyle
from figures.figure import Figure
from figures.bullet import Bullet

class NormalShooting(ShootStyle):

    def __init__(self, figure):
        super().__init__(figure)
        self.shootDelay = 0

    def shoot(self):
        if self.shootDelay == 0:
            bullet = Bullet(self.figure.map, self.figure.pozX, self.figure.pozY, self.figure.direction)
            self.figure.map.addFigure(bullet)
            self.shootDelay = 10
        else:
            self.shootDelay -= 1