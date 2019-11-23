import pygame

class GameMap():
    def __init__(self, height, width):
        self.window = pygame.display.set_mode((width, height))
        self.height = height
        self.width = width
        self.figures = []

    def checkCollision(self, source):
        for figure in self.figures:
            if figure != source and GameMap.collisionTest(source, figure):
                return figure

        return None            

    @staticmethod    
    def collisionTest(figure1, figure2):
        figure1LeftLimit = figure1.pozX - figure1.width // 2
        figure1RightLimit = figure1.pozX + figure1.width // 2

        figure2LeftLimit = figure2.pozX - figure2.width // 2
        figure2RightLimit = figure2.pozX - figure2.width // 2

        collisionX = figure1LeftLimit >= figure2LeftLimit and figure1LeftLimit <= figure2RightLimit
        collisionX = collisionX or figure1RightLimit >= figure2LeftLimit and figure1RightLimit <= figure2RightLimit

        if not collisionX:
            return False

        figure1LeftLimit = figure1.pozY - figure1.height // 2
        figure1RightLimit = figure1.pozY + figure1.height // 2

        figure2LeftLimit = figure2.pozY - figure2.height // 2
        figure2RightLimit = figure2.pozY - figure2.height // 2

        collisionY = figure1LeftLimit >= figure2LeftLimit and figure1LeftLimit <= figure2RightLimit
        collisionY = collisionY or figure1RightLimit >= figure2LeftLimit and figure1RightLimit <= figure2RightLimit

        return collisionY        

    def update(self):
        for figure in self.figures:
            figure.update(self)

    def draw(self):
        self.window.fill((0, 0, 0))
        for figure in self.figures:
            figure.draw(self.window)

    def addFigure(self, figure):
        self.figures.append(figure)

    def removeFigure(self, figure):
        self.figures.remove(figure)
                