import pygame
from map.gameMap import GameMap

class Screen():

    LINE_SIZE = 4
    LINE_COLOR = (128,128,128)
    TOP_BAR_COLOR = (211,211,211)

    SCORE_SPAN = 10

    def __init__(self, width, height):
        pygame.font.init()
        self.scoreFont = pygame.font.SysFont('Arial', 20, bold = True)
        self.screen = pygame.display.set_mode((width, height))

        topBarHeight = height * 0.05
        mainScreenHeight = height * 0.95

        topBar = pygame.Rect(0, 0, width, topBarHeight)
        mainScreen = pygame.Rect(0, topBarHeight, width, mainScreenHeight)

        self.topBarSurface = self.screen.subsurface(topBar)
        self.mainScreenSurface = self.screen.subsurface(mainScreen)
        self.map = GameMap(self.mainScreenSurface)


    def refreshTopBar(self, score):
        self.topBarSurface.fill(Screen.TOP_BAR_COLOR)

        scoreText = self.scoreFont.render('Score: {}'.format(score), False, (0, 0, 0))
        self.topBarSurface.blit(scoreText, (Screen.SCORE_SPAN, Screen.SCORE_SPAN))

        startPozX = 0
        startPozY = self.topBarSurface.get_height() - Screen.LINE_SIZE + 1

        endPozX = self.topBarSurface.get_width()
        endPozY = startPozY

        pygame.draw.line( self.topBarSurface, Screen.LINE_COLOR, (startPozX, startPozY), (endPozX, endPozY), Screen.LINE_SIZE)  


    def refresh(self, score):

        self.refreshTopBar(score)
        self.map.draw() 

        pygame.display.update()



