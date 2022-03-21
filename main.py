import pygame, sys

pygame.init()
pygame.display.set_caption("Kingdom")

Screen_Width = 1400
Screen_Height = 800

# Player Image
player_image = pygame.image.load("Assets/player.png").convert_alpha()
player_image_tr = pygame.transform.scale(player_image, (50,25))



screen = pygame.display.set_mode((Screen_Width, Screen_Height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((100,100,50))

    pygame.display.flip()