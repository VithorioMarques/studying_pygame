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

sky_surface = pygame.image.load(graphics_path+'Sky.png').convert_alpha()
ground_surface = pygame.image.load(graphics_path+'ground.png').convert_alpha()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load(graphics_path+'snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (0,300))

player_surf = pygame.image.load(graphics_path+'Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300, 50))

    snail_rect.x -= 3
    screen.blit(snail_surface, snail_rect)
    
    screen.blit(player_surf,player_rect)

    if snail_rect.x < -28:
        snail_rect.x = WIDTH + 12
    
    pygame.display.update()
    clock.tick(60)