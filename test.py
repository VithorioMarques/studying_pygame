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
game_active = True

sky_surface = pygame.image.load(graphics_path+'Sky.png').convert_alpha()
ground_surface = pygame.image.load(graphics_path+'ground.png').convert_alpha()

score_surface = test_font.render('My game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (WIDTH/2,50))

snail_surface = pygame.image.load(graphics_path+'snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (0,300))

player_surf = pygame.image.load(graphics_path+'Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800



    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect,10)

        #pygame.draw.line(screen, 'Gold', (0,0),(800,400),10)

        screen.blit(score_surface,score_rect)

        snail_rect.x -= 5
        screen.blit(snail_surface, snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")

        if snail_rect.x < -28:
            snail_rect.x = WIDTH + 12
        
        # if player_rect.colliderect(snail_rect):
        #     print('collision')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
        #     print('colision')

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)