import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.evolutionDelay = 100
        self.isClicking = False

        screenSize = 900
        numberOfCells = 80

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

            self.handleClick()
            
            if generationCnt >= self.evolutionDelay:
                generationCnt = 0
                self.grid.nextGeneration()
            
            
            self.screen.update()

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

        self.values[5][5] = 1
        self.values[5][6] = 1
        self.values[6][6] = 1

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
        self.values = nextValues

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
    def __init__(self, width, height, grid):
        pygame.display.set_caption("Game of Life")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.grid = grid

    def drawGrid(self):
        cellHeight = self.height / self.grid.height
        cellWidth = self.width / self.grid.width

        for i in range(1, self.grid.width):
            pygame.draw.line(self.screen, (211,211,211), (cellWidth * i, 0), (cellWidth * i, self.height))

        for i in range(1, self.grid.height):
            pygame.draw.line(self.screen, (211,211,211), (0, cellHeight * i), (self.width, cellHeight * i))

        for i in range(self.grid.height):
            for j in range(self.grid.width):
                if self.grid.values[i][j] != 0:
                   pygame.draw.rect(self.screen, (255, 0, 0), (i * cellHeight + 1, j * cellWidth + 1, cellHeight - 1, cellWidth - 1)) 

    def onClick(self, pozX, pozY):
        print("Click at: " + str(pozX) + ' and ' + str(pozY)) 

    def update(self):
        self.screen.fill((0, 0, 0))
        self.drawGrid()
        pygame.display.update()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()