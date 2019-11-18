import pygame
from figure import Figure
from movableFigure import MovableFigure
from direction import Direction
from gameMap import GameMap

class Game:

    def __init__(self):
        pygame.init()
        self.figureList = []
        self.title = "FirstGame"
        self.map = GameMap(500, 500)
        self.player = MovableFigure(50, 50, 50, 50, 5)
        self.figureList.append(self.player)

        randomFigure = Figure(300, 300, 20, 20)
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
        if keys[pygame.K_UP]:
            move = Direction.UP
        
        self.player.move(move, self.map)

    def refreshScreen(self):
        self.window.fill((0, 0, 0))
        self.drawFigures()
        pygame.display.update()

    def drawFigures(self):
        for figure in self.figureList:
            figure.draw(self.window)

    def play(self):
        run = True
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.movePlayer()
            self.refreshScreen()
        pygame.quit()       