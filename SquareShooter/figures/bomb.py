from figures.figure import Figure
from map.gameMap import GameMap
from map.direction import Direction
from figures.bullet import Bullet
import pygame

class Bomb(Figure):

    def __init__(self, map, pozX, pozY):
        super().__init__(map, pozX, pozY, 20, 20, (36, 87, 32))
        self.speed = 0 
        self.timer = 150

    def explode(self):
        self.map.removeFigure(self)

        bulletDirections = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in bulletDirections:
            bulletDirection = Direction(direction[0], direction[1])
            bullet = Bullet(self.map, self.pozX, self.pozY, bulletDirection)
            self.map.addFigure(bullet)

    
    def draw(self):
        pygame.draw.circle(self.map.window, self.color, (self.pozX, self.pozY), 10)

    def update(self):
        self.timer -= 1
        if self.timer < 0:
            self.explode()
