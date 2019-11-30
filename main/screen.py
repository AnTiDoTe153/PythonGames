import pygame
from map.gameMap import GameMap

class Screen():

    LINE_SIZE = 4
    LINE_COLOR = (128,128,128)
    TOP_BAR_COLOR = (211,211,211)

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

        topBarHeight = height * 0.1
        mainScreenHeight = height * 0.9

        topBar = pygame.Rect(0, 0, width, topBarHeight)
        mainScreen = pygame.Rect(0, topBarHeight, width, mainScreenHeight)

        self.topBarSurface = self.screen.subsurface(topBar)
        self.mainScreenSurface = self.screen.subsurface(mainScreen)
        self.map = GameMap(self.mainScreenSurface)


    def refreshTopBar(self):
        self.topBarSurface.fill(Screen.TOP_BAR_COLOR)

        startPozX = 0
        startPozY = self.topBarSurface.get_height() - Screen.LINE_SIZE + 1

        endPozX = self.topBarSurface.get_width()
        endPozY = startPozY

        pygame.draw.line( self.topBarSurface, Screen.LINE_COLOR, (startPozX, startPozY), (endPozX, endPozY), Screen.LINE_SIZE)  


    def refresh(self):

        self.refreshTopBar()
        self.map.draw()

        self.screen.blit(self.screen, (0, 0))

        pygame.display.update()



