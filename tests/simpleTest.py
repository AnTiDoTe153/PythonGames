import pygame


def main():
    pygame.init()

    width = 700
    height = 700

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test")

    while True:
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50))
        pygame.display.update()
        





if __name__ == '__main__':
    main()