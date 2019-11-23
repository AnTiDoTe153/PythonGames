import pygame

class Figure:

    def __init__(self, map, pozX, pozY, width, height, color = (220,20,60)):
        self.map = map
        self.pozX = pozX
        self.pozY = pozY
        self.width = width
        self.height = height
        self.color = color
    
    def checkCollision(self):
        for figure in self.map.figures:
            if figure != self and Figure.collisionTest(self, figure):
                self.onCollision(figure)
                figure.onCollision(self)

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

    def draw(self):
        pygame.draw.rect(self.map.window, self.color, (self.pozX - self.width // 2, self.pozY - self.height // 2, self.width, self.height))

    def onCollision(self, source):
        pass

    def update(self):
        pass
