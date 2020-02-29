import pygame

class Game:
    def __init__(self):
        pygame.init()

        width = 700
        height = 700

        self.screen = Screen(width, height)


    def play(self):
        while True:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.update()
        

class Screen:
    def __init__(self, width, height):
        pygame.display.set_caption("Game of Life")
        self.screen = pygame.display.set_mode((width, height))


    def update(self):
        self.screen.fill((0, 0, 0))
        pygame.display.update()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()