import pygame
from sys import exit
from random import randint

WIDTH = 800
HEIGHT = 400

graphics_path = './UltimatePygameIntro/graphics/'
font_path = './UltimatePygameIntro/font/'

def display_score():
    current_time = int(pygame.time.get_ticks()/1000 - start_time)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def display_start_screen(score):
    game_name_surf = test_font.render("Snail Jumper", False, (111,196,169))
    game_name_rect = game_name_surf.get_rect(center = (400,80))
    screen.blit(game_name_surf, game_name_rect)
    if score == 0:
        instructions_surf = test_font.render("Menu: PRESS SPACE TO START RUN", False, (111,196,169))
        instructions_rect = instructions_surf.get_rect(center = (400,325))
        screen.blit(instructions_surf, instructions_rect)
        instructions_surf2 = test_font.render("Game: PRESS SPACE TO JUMP!!!", False, (111,196,169))
        instructions_rect2 = instructions_surf2.get_rect(center = (400,375))
        screen.blit(instructions_surf2, instructions_rect2)
    else:
        score_surf = test_font.render(f'Your score: {score}', False, (111,196,169))
        score_rect = score_surf.get_rect(center = (400,325))
        screen.blit(score_surf, score_rect)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    # play walking animation if the player is on the floor
    # display the jump surface when player is not on floor
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snail Jumper')
clock = pygame.time.Clock()
test_font = pygame.font.Font(font_path+'Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load(graphics_path+'Sky.png').convert_alpha()
ground_surface = pygame.image.load(graphics_path+'ground.png').convert_alpha()

# score_surface = test_font.render('My game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (WIDTH/2,50))

# Obstacles
snail_frame1 = pygame.image.load(graphics_path+'snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load(graphics_path+'snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame1   = pygame.image.load(graphics_path+'Fly/Fly1.png').convert_alpha()
fly_frame2   = pygame.image.load(graphics_path+'Fly/Fly2.png').convert_alpha()
fly_frames   = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surface  = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk1 = pygame.image.load(graphics_path+'Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load(graphics_path+'Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load(graphics_path+'Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

player_stand = pygame.image.load(graphics_path + 'Player/player_stand.png')
player_stand_scaled = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand_scaled.get_rect(center = (400,200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer   = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                start_time = int(pygame.time.get_ticks()/1000)

        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100),210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,10)

        # #pygame.draw.line(screen, 'Gold', (0,0),(800,400),10)

        # screen.blit(score_surface,score_rect)
        score = display_score()

        # snail_rect.x -= 5
        # screen.blit(snail_surface, snail_rect)
        # if snail_rect.x < -28:
        #     snail_rect.x = WIDTH + 12
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300

        player_animation()
        screen.blit(player_surf,player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collisions(player_rect, obstacle_rect_list)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")
        
        # if player_rect.colliderect(snail_rect):
        #     print('collision')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
        #     print('colision')
    else:
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        screen.fill((94,128,162))
        screen.blit(player_stand_scaled, player_stand_rect)
        display_start_screen(score)

    pygame.display.update()
    clock.tick(60)