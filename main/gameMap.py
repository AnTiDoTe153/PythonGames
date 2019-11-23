from figure import Figure
import pygame

class GameMap():
    def __init__(self, height, width):
        self.window = pygame.display.set_mode((width, height))
        self.height = height
        self.width = width
        self.figures = []

    def checkCollision(self):
        for i in range(len(self.figures) - 1):
            for j in range(i + 1, len(self.figures)):
                if GameMap.collisionTest(self.figures[i], self.figures[j]):
                    self.figures[i].onCollision(self.figures[j])
                    self.figures[j].onCollision(self.figures[i])

        return None            

    @staticmethod    
    def collisionTest(figure1, figure2):
        figure1LeftLimit = figure1.pozX - figure1.width // 2
        figure1RightLimit = figure1LeftLimit + figure1.width

        figure2LeftLimit = figure2.pozX - figure2.width // 2
        figure2RightLimit = figure2LeftLimit + figure2.width

        collisionX = figure1LeftLimit >= figure2LeftLimit and figure1LeftLimit <= figure2RightLimit
        collisionX = collisionX or figure1RightLimit >= figure2LeftLimit and figure1RightLimit <= figure2RightLimit

        if not collisionX:
            return False
        
        figure1LeftLimit = figure1.pozY - figure1.height // 2
        figure1RightLimit = figure1LeftLimit + figure1.height

        figure2LeftLimit = figure2.pozY - figure2.height // 2
        figure2RightLimit = figure2LeftLimit + figure2.height

        collisionY = figure1LeftLimit >= figure2LeftLimit and figure1LeftLimit <= figure2RightLimit
        collisionY = collisionY or figure1RightLimit >= figure2LeftLimit and figure1RightLimit <= figure2RightLimit


        return collisionY     

    def update(self):
        for figure in self.figures:
            figure.update(self)

        self.checkCollision()

    def draw(self):
        self.window.fill((0, 0, 0))
        for figure in self.figures:
            figure.draw(self.window)

    def addFigure(self, figure):
        self.figures.append(figure)

    def removeFigure(self, figure):
        self.figures.remove(figure)
                