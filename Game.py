import pygame
from MovableFigure import MovableFigure
from Coordinates import Coordinates
from Direction import Direction
from Figure import Figure
from Map import Map

class Game:

    def __init__(self):
        pygame.init()
        self.figureList = []
        self.title = "FirstGame"
        self.map = Map(500, 500)
        self.player = MovableFigure(Coordinates(50, 50), 50, 50, 15, 20)
        self.figureList.append(self.player)

        randomFigure = Figure(Coordinates(300, 300), 20, 20)
        self.figureList.append(randomFigure)

        self.initWindow()

    def initWindow(self):
        self.window = pygame.display.set_mode((self.map.width, self.map.height))
        pygame.display.set_caption(self.title)

    def movePlayer(self):
        keys = pygame.key.get_pressed()
        move = None
        if keys[pygame.K_LEFT]:
            move = Direction.LEFT
        if keys[pygame.K_RIGHT]:
            move = Direction.RIGHT
        if keys[pygame.K_DOWN]:
            move = Direction.DOWN
        
        self.player.move(move, self.map)

    def refreshScreen(self):
        self.window.fill((0, 0, 0))
        self.drawFigures()
        pygame.display.update()

    def drawFigures(self):
        for figure in self.figureList:
            pygame.draw.rect(self.window, (255, 0, 0), (figure.coordinates.x, figure.coordinates.y, figure.width, figure.height))

    def play(self):
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.movePlayer()
            self.refreshScreen()
        pygame.quit()       