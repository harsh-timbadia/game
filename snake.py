import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
test_surface = test_font.render('my game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800


    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    mouse_pos = pygame.mouse.get_pos()

    if player_rect.collidepoint((mouse_pos)):
        print('collision')
    pygame.display.update()
    clock.tick(60)

""" #day 1 progress
:ive learnt to use basics of py game,
there are many functions and inside all functions are more functions
its my first time seeing that many functions,
progress till now
-> learnt to make a display from python code.
-> using pygame time clock for fps setting
-> learnt to set captions
-> learnt to add images
-> learnt that every image is a surface and its updation 60 times a seconds
-> added a snail and did its animation
-> its easy just a bit of learning in form of keywords instead of paragraphs """


#day 1 night session 
#nvm im not gonna write anything here but im donig codeing 