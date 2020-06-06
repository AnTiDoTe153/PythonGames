import pygame
from figures.figure import Figure
from figures.player import Player
from figures.target import Target
from figures.bomb import Bomb

from map.direction import Direction
from map.gameMap import GameMap

from screen import Screen
from observer import Observer
from event import Event

class Game(Observer):
    maxTargetCount = 4

    def __init__(self):
        pygame.init()
        self.title = "FirstGame"
        self.score = 0

        self.screen = Screen(800, 800)
        self.map = self.screen.map
        self.player = Player(self.map, 50, 50, 50, 50, 5)
        self.map.addFigure(self.player)

        self.map.addFigure(Bomb(self.map, 200, 200))

        self.resetTargets()
        self.initWindow()

    def notify(self, eventData = None):
        self.score += 10
        self.targetCount -= 1
        if self.targetCount <= 0:
            self.resetTargets()

    def resetTargets(self):
        self.targetCount = Game.maxTargetCount

        for i in range(self.targetCount):
            target = Target(self.map)
            target.subscribe(self)
            self.map.addFigure(target)


    def initWindow(self):
        pygame.display.set_caption(self.title)

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        move = None
        if keys[pygame.K_a]:
            move = Direction(-1, 0) # move left
        elif keys[pygame.K_d]:
            move = Direction(1, 0) # move right
        elif keys[pygame.K_s]:
            move = Direction(0, 1) # move down
        elif keys[pygame.K_w]:
            move = Direction(0, -1) # move up

        if move != None:
            self.player.move(move)

        shootDirection = None
        if keys[pygame.K_LEFT]:
            shootDirection = Direction(-1, 0) # move left
        elif keys[pygame.K_RIGHT]:
            shootDirection = Direction(1, 0) # move right
        elif keys[pygame.K_DOWN]:
            shootDirection = Direction(0, 1) # move down
        elif keys[pygame.K_UP]:
            shootDirection = Direction(0, -1) # move up
        

        if shootDirection != None:
            self.player.setDirection(shootDirection)
            self.player.shoot()


    def play(self):
        run = True
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.handleKeys()
            self.map.update()
            self.screen.refresh(self.score)
        pygame.quit()       