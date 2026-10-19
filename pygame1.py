import pygame
import sys 
import subprocess

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main center")

# Separated the clock and the font into their proper variables
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

text_surface = font.render('press ENTER to play Pixel Runner', True, 'White')
text_rect = text_surface.get_rect(center=(400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Indented this block so it sits exactly inside the event loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("launching game")
                subprocess.run([sys.executable, "snake.py"])
                print("welcome")
                
    screen.fill((30, 30, 30))
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(60)
    