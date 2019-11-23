import pygame
from figure import Figure
from player import Player
from direction import Direction
from gameMap import GameMap
from target import Target
from observer import Observer
from event import Event

class Game(Observer):
    maxTargetCount = 4

    def notify(self, eventData = None):
        self.targetCount -= 1
        if self.targetCount <= 0:
            self.resetTargets()

    def resetTargets(self):
        self.targetCount = Game.maxTargetCount

        for i in range(self.targetCount):
            target = Target(self.map)
            target.subscribe(self)
            self.map.addFigure(target)


    def __init__(self):
        pygame.init()
        self.title = "FirstGame"
        self.map = GameMap(500, 500)
        self.player = Player(self.map, 50, 50, 50, 50, 5)
        self.map.addFigure(self.player)

        self.resetTargets()
        self.initWindow()

    def initWindow(self):
        pygame.display.set_caption(self.title)

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        move = None
        if keys[pygame.K_a]:
            move = Direction.LEFT
        if keys[pygame.K_d]:
            move = Direction.RIGHT
        if keys[pygame.K_s]:
            move = Direction.DOWN
        if keys[pygame.K_w]:
            move = Direction.UP

        if move != None:
            self.player.move(move)

        shoot = False
        if keys[pygame.K_LEFT]:
            self.player.setDirection(Direction.LEFT)
            shoot = True
        if keys[pygame.K_RIGHT]:
            self.player.setDirection(Direction.RIGHT)
            shoot = True
        if keys[pygame.K_DOWN]:
            self.player.setDirection(Direction.DOWN)
            shoot = True
        if keys[pygame.K_UP]:
            self.player.setDirection(Direction.UP)
            shoot = True

        if shoot:
            self.player.shoot()

    def refreshScreen(self):
        self.map.draw()
        pygame.display.update()

    def play(self):
        run = True
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.handleKeys()
            self.map.update()
            self.refreshScreen()
        pygame.quit()       