from direction import Direction
from figure import Figure
import pygame

class Bullet(Figure):

    def __init__(self, pozX, pozY, direction, speed = 5):
        super().__init__(pozX, pozY, 20, 20, (255, 255, 0))
        self.direction = direction
        self.speed = speed

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.pozX, self.pozY), 6)

    def update(self, map):
        if self.direction == Direction.LEFT:
            self.pozX -= self.speed
        elif self.direction == Direction.RIGHT:
            self.pozX += self.speed
        elif self.direction == Direction.UP:
            self.pozY -= self.speed
        elif self.direction == Direction.DOWN:
            self.pozY += self.speed

        if self.pozX <= 0 or self.pozX >= map.width - self.width:
            map.removeFigure(self)
        if self.pozY <= 0 or self.pozY >= map.height - self.height:
            map.removeFigure(self)
