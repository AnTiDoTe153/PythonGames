from figures.figure import Figure
from figures.healthBar import HealthBar
from figures.bullet import Bullet
from map.gameMap import GameMap
from event import Event
import pygame
import random

class Powerup(Figure):
    
    targetHeight = 50
    targetWidth = 50
    targetColor = (30,144,255)

    def __init__(self, map, pozX = None, pozY = None):
        if pozX == None:
            pozX = random.randrange(0, map.width - Powerup.targetWidth)
        if pozY == None:
           pozY = random.randrange(0, map.height - Powerup.targetHeight)

        Figure.__init__(self, map, pozX, pozY, Powerup.targetWidth, Powerup.targetHeight, Powerup.targetColor)

        self.targetImg = pygame.transform.scale(pygame.image.load('powerup.png'), (self.height, self.width))

    def draw(self):
        self.map.window.blit(self.targetImg, (self.pozX - self.height // 2, self.pozY - self.width // 2))
        
    def update(self):
        self.checkCollision()
    
