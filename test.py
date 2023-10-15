import pygame
from sys import exit

graphics_path = './UltimatePygameIntro/graphics/'
font_path = './UltimatePygameIntro/font/'
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Beard Cutter')
clock = pygame.time.Clock()
test_font = pygame.font.Font(font_path+'Pixeltype.ttf', 50)

sky_surface = pygame.image.load(graphics_path+'Sky.png')
ground_surface = pygame.image.load(graphics_path+'ground.png')
text_surface = test_font.render('My game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300, 50))

    pygame.display.update()
    clock.tick(60)