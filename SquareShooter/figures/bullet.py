from figures.figure import Figure
from map.direction import Direction
from map.gameMap import GameMap
import pygame

class Bullet(Figure):

    def __init__(self, map, pozX, pozY, direction, speed = 5):
        super().__init__(map, pozX, pozY, 20, 20, (255, 255, 0))
        self.direction = direction
        self.speed = speed
        self.cnt = 0

    def draw(self):
        pygame.draw.circle(self.map.window, self.color, (self.pozX, self.pozY), 6)

    def update(self):
        self.pozX += int(self.speed * self.direction.dirX)
        self.pozY += int(self.speed * self.direction.dirY)

        self.checkCollision()

        if self.pozX <= 0 or self.pozX >= self.map.width - self.width:
            self.map.removeFigure(self)
            return
        if self.pozY <= 0 or self.pozY >= self.map.height - self.height:
            self.map.removeFigure(self)
            return
    

