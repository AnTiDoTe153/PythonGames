import pygame

def main():
    pygame.init()
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("First Game")
    
    x = 50
    y = 60

    width = 40
    height = 60

    velocity = 15

    run = True

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x = max(0, x - velocity)
        if keys[pygame.K_RIGHT]:
            x = min(SCREEN_WIDTH - width, x + velocity)
        if keys[pygame.K_UP]:
            y = max(0, y - velocity)
        if keys[pygame.K_DOWN]:
            y = min(SCREEN_HEIGHT - height, y + velocity)

        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
        pygame.display.update()
    pygame.quit()


        




if __name__ == "__main__":
    main()