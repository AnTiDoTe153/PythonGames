import pygame

class Game:
    def __init__(self):
        pygame.init()

        width = 700
        height = 700
        self.grid = Grid(5, 5)
        self.screen = Screen(width, height, self.grid)

    def play(self):
        while True:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.update()


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.values = [[ 0 for j in range(width)] for i in range(height)]


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
            pygame.draw.line(self.screen, (255,255,255), (cellWidth * i, 0), (cellWidth * i, self.height))

        for i in range(1, self.grid.height):
            pygame.draw.line(self.screen, (255,255,255), (0, cellHeight * i), (self.width, cellHeight * i))


    def update(self):
        self.screen.fill((0, 0, 0))
        self.drawGrid()
        pygame.display.update()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()