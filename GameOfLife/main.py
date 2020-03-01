import pygame
import math

class Game:
    def __init__(self, screenSize = 900, cells = 30, evolutionDelay = 50):
        pygame.init()

        self.evolutionDelay = evolutionDelay
        self.isClicking = False
        self.isPressingP = False
        self.pause = True
        self.totalGenerations = 0

        screenSize = screenSize
        numberOfCells = cells

        self.grid = Grid(numberOfCells, numberOfCells)
        self.screen = Screen(screenSize, screenSize, self.grid)

    def play(self):
        generationCnt = 0

        while True:
            pygame.time.delay(10)
            generationCnt += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.handleKeys()
            self.handleClick()
            
            if generationCnt >= self.evolutionDelay and not self.pause:
                generationCnt = 0
                self.totalGenerations += 1
                self.grid.nextGeneration()
            
            self.screen.update(self.totalGenerations, self.pause)

    def handleKeys(self):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_p] and self.isPressingP:
            self.isPressingP = False

        if keys[pygame.K_p] and not self.isPressingP:
            self.isPressingP = True
            self.pause = not self.pause

    def handleClick(self):
        if pygame.mouse.get_pressed()[0] == 0 and self.isClicking == True:
            self.isClicking = False

        if pygame.mouse.get_pressed()[0] == 1 and self.isClicking == False:
            mousePos = pygame.mouse.get_pos()
            self.screen.onClick(mousePos[0], mousePos[1])
            self.isClicking = True


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.values = self.__createValues()

    def __createValues(self):
        return [[ 0 for j in range(self.width)] for i in range(self.height)]

    def nextGeneration(self):
        nextValues = self.__createValues()
        myCnt = 0

        for i in range(self.height):
            for j in range(self.width):
                if(self.__lives(i, j)):
                    nextValues[i][j] = 1
                    myCnt += 1
                else:
                    nextValues[i][j] = 0

        for i in range(self.height):
            for j in range(self.width):
                self.values[i][j] = nextValues[i][j]

    def __calculateNeighbours(self, i, j):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]

        counter = 0

        for move in moves:
            if self.__isValidPosition(i + move[0], j + move[1]) and self.values[i + move[0]][j + move[1]] > 0:
                counter += 1

        return counter

    def __lives(self, i, j):
        cnt = self.__calculateNeighbours(i, j)

        if self.values[i][j] == 0: 
            if cnt == 3:
                return True
            return False
        

        if cnt < 2:
            return False
        if cnt > 3:
            return False

        return True

    def __isValidPosition(self, i, j):
        if i < 0 or i >= self.height:
            return False
        if j < 0 or j >= self.width:
            return False
        
        return True


class Screen:

    BACKGROUND_COLOR = (211,211,211)
    TOP_BAR_COLOR = (190,190,190)
    LINE_COLOR = (128,128,128)
    GRID_COLOR = (128,128,128)
    CELL_COLOR = (0, 0, 0)

    LINE_SIZE = 4
    SCORE_SPAN = 10

    def __init__(self, width, height, grid):
        pygame.display.set_caption("Game of Life")
        self.totalWidth = width
        self.totalHeight = height
        self.allScreen = pygame.display.set_mode((width, height))
        self.grid = grid

        pygame.font.init()
        self.scoreFont = pygame.font.SysFont('Arial', 20, bold = True)

        self.topBarHeight = height * 0.05

        self.height = height * 0.95
        self.width = width

        topBar = pygame.Rect(0, 0, width, self.topBarHeight)
        mainScreen = pygame.Rect(0, self.topBarHeight, self.width, self.height)

        self.topBarSurface = self.allScreen.subsurface(topBar)
        self.mainScreen = self.allScreen.subsurface(mainScreen)


    def drawTopBar(self, generation, pause):
        self.topBarSurface.fill(Screen.TOP_BAR_COLOR)

        displayMessage = 'Game of life - generation: {}'.format(generation)
        if pause:
            displayMessage += ' (paused)'

        topBarText = self.scoreFont.render(displayMessage, False, (0, 0, 0))
        self.topBarSurface.blit(topBarText, (Screen.SCORE_SPAN, Screen.SCORE_SPAN))

        startPozX = 0
        startPozY = self.topBarSurface.get_height() - Screen.LINE_SIZE + 1

        endPozX = self.topBarSurface.get_width()
        endPozY = startPozY

        pygame.draw.line(self.topBarSurface, Screen.LINE_COLOR, (startPozX, startPozY), (endPozX, endPozY), Screen.LINE_SIZE)  


    def drawMainScreen(self):
        self.mainScreen.fill(Screen.BACKGROUND_COLOR)
        cellHeight = self.__getCellHeight()
        cellWidth = self.__getCellWidth()

        for i in range(1, self.grid.width):
            pygame.draw.line(self.mainScreen, Screen.GRID_COLOR, (cellWidth * i, 0), (cellWidth * i, self.height))

        for i in range(0, self.grid.height):
            pygame.draw.line(self.mainScreen, Screen.GRID_COLOR, (0, cellHeight * i), (self.width, cellHeight * i))

        for i in range(self.grid.height):
            for j in range(self.grid.width):
                if self.grid.values[i][j] != 0:
                   pygame.draw.rect(self.mainScreen, Screen.CELL_COLOR, (j * cellWidth + 1, i * cellHeight + 1, cellWidth - 1, cellHeight - 1)) 


    def __getCellHeight(self):
        screenHeight = self.mainScreen.get_height()
        return screenHeight / self.grid.height


    def __getCellWidth(self):
        screenWidth = self.mainScreen.get_width()
        return screenWidth / self.grid.width


    def __getGridPosition(self, pozX, pozY):
        cellHeight = self.__getCellHeight()
        cellWidth = self.__getCellWidth()

        relativePozY = int(pozY - self.topBarHeight)
        relativePozX = pozX

        j = int(math.floor(relativePozX / cellWidth))
        i = int(math.floor(relativePozY / cellHeight))

        return i , j


    def onClick(self, pozX, pozY):
        i, j = self.__getGridPosition(pozX, pozY)

        if i < 0 or j < 0:
            return

        if self.grid.values[i][j] == 1:
            self.grid.values[i][j] = 0
        else:
            self.grid.values[i][j] = 1


    def update(self, generations, pause):
        self.drawMainScreen()
        self.drawTopBar(generations, pause)
        pygame.display.update()


def main():
    game = Game(cells = 30)
    game.play()

if __name__ == '__main__':
    main()