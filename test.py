import pygame
from sys import exit

WIDTH = 800
HEIGHT = 400

graphics_path = './UltimatePygameIntro/graphics/'
font_path = './UltimatePygameIntro/font/'
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Beard Cutter')
clock = pygame.time.Clock()
test_font = pygame.font.Font(font_path+'Pixeltype.ttf', 50)

sky_surface = pygame.image.load(graphics_path+'Sky.png')
ground_surface = pygame.image.load(graphics_path+'ground.png')
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load(graphics_path+'snail/snail1.png')
snail_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300, 50))
    snail_x_pos -= 3
    screen.blit(snail_surface,(snail_x_pos,265))
    if snail_x_pos < -28:
        snail_x_pos = WIDTH + 12
    pygame.display.update()
    clock.tick(60)