import pygame


def main():
    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))

    canvas = pygame.Surface((width, height))

    p1_camera = pygame.Rect(0,0,400,300)
    p2_camera = pygame.Rect(400,0,400,300)
    p3_camera = pygame.Rect(0,300,400,300)
    p4_camera = pygame.Rect(400,300,400,300)

    sub1 = canvas.subsurface(p1_camera)
    sub2 = canvas.subsurface(p2_camera)
    sub3 = canvas.subsurface(p3_camera)
    sub4 = canvas.subsurface(p4_camera)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.draw.line(sub2, (255,255,255), (0,0), (0,300))
        pygame.draw.line(sub4, (255,255,255), (0,0), (0,300))
        pygame.draw.line(sub3, (255,255,255), (0,0), (400,0))
        pygame.draw.line(sub4, (255,255,255), (0,0), (400,0))

        pygame.draw.rect(sub1, (255, 0, 0), (50, 50, 50, 50))
        pygame.draw.rect(sub2, (255, 0, 0), (50, 50, 50, 50))
        pygame.draw.rect(sub3, (255, 0, 0), (50, 50, 50, 50))
        pygame.draw.rect(sub4, (255, 0, 0), (50, 50, 50, 50))

        # draw player 1's view  to the top left corner
        screen.blit(sub1, (0,0))
        # player 2's view is in the top right corner
        screen.blit(sub2, (400, 0))
        # player 3's view is in the bottom left corner
        screen.blit(sub3, (0, 300))
        # player 4's view is in the bottom right corner
        screen.blit(sub4, (400, 300))

        pygame.display.update()





if __name__ == '__main__':
    main()