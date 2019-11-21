from direction import Direction
from figure import Figure

class Bullet(Figure):

    def __init__(self, pozX, pozY, direction, speed = 5):
        super().__init__(pozX, pozY, 20, 20)
        self.direction = direction
        self.speed = speed

    def update(self, map):
        if self.direction == Direction.LEFT:
            self.pozX -= self.speed
        elif self.direction == Direction.RIGHT:
            self.pozX += self.speed

        if self.pozX <= 0 or self.pozX >= map.width - self.width:
            map.removeFigure(self)
