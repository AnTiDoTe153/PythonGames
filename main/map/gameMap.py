from figures.figure import Figure
import pygame

class GameMap():
    def __init__(self, window):
        self.window = window
        self.height = window.get_height()
        self.width = window.get_width()
        self.figures = []           

    def update(self):
        for figure in self.figures:
            figure.update()

    def draw(self):
        self.window.fill((0, 0, 0))
        for figure in self.figures:
            figure.draw()

    def addFigure(self, figure):
        self.figures.append(figure)

    def removeFigure(self, figure):
        self.figures.remove(figure)
                