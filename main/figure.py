import pygame

class Figure:

    def __init__(self, pozX, pozY, width, height, color = (255, 0, 0)):
        self.pozX = pozX
        self.pozY = pozY
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.pozX, self.pozY, self.width, self.height))
