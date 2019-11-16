import pygame
from enum import Enum

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

TITLE = "First Game"

class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    def __init__(self, coordinates, width, height):
        self.coordinates = coordinates
        self.width = width
        self.height = height

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class MovableFigure(Figure):
    def __init__(self, coordinates, width, height, speed):
        super().__init__(coordinates, width, height)
        self.speed = speed

    def move(self, direction):
        if direction == Direction.UP:
            self.coordinates.y = max(0, self.coordinates.y - self.speed)
        if direction == Direction.DOWN:
            self.coordinates.y = min(SCREEN_HEIGHT - self.height, self.coordinates.y + self.speed)
        if direction == Direction.LEFT:
            self.coordinates.x = max(0, self.coordinates.x - self.speed)
        if direction == Direction.RIGHT:
            self.coordinates.x = min(SCREEN_WIDTH - self.width, self.coordinates.x + self.speed)


def initWindow():
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    return window

def movePlayer(player):
    keys = pygame.key.get_pressed()
    move = None
    if keys[pygame.K_LEFT]:
        move = Direction.LEFT
    if keys[pygame.K_RIGHT]:
        move = Direction.RIGHT
    if keys[pygame.K_UP]:
       move = Direction.UP
    if keys[pygame.K_DOWN]:
        move = Direction.DOWN
    player.move(move)

def drawFigures(window, figureList):
    for figure in figureList:
        pygame.draw.rect(window, (255, 0, 0), (figure.coordinates.x, figure.coordinates.y, figure.width, figure.height))

def main():
    pygame.init()
    window = initWindow()
    
    figureList = []
    player = MovableFigure(Coordinates(50, 50), 50, 50, 15)
    figureList.append(player)


    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        movePlayer(player)
        window.fill((0, 0, 0))

        drawFigures(window, figureList)
        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()