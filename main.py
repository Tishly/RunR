import pygame
from sys import exit
from random import randint

def display_score():
    """A function that takes the current time,
    converts it to the player's score and displays to the screen"""
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)
    return current_time

def  obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= 5
            if obstacle_rectangle.bottom == 300: screen.blit(snail_surface,obstacle_rectangle)
            else: screen.blit(fly_surface,obstacle_rectangle)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rectangle in obstacles:
            if player.colliderect(obstacle_rectangle): return False
    return True

def player_animation():
    global player_surface, player_index
    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]
    screen.blit()

pygame.init()

# set dimensions for game user interface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("RunR")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# import background images to display
sky_surface = pygame.image.load('images/Sky.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert()

# import the obstacle character graphics and set dimensions
snail_surface = pygame.image.load('images/snail/snail2.png').convert_alpha()
fly_surface = pygame.image.load('images/fly/Fly1.png').convert_alpha()

# obstacles
obstacle_rectangle_list = []

# import the player character image and set dimensions
player_walk_1 = pygame.image.load('images/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('images/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('images/player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('images/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

game_name = test_font.render('RunR',False,(111,196,169))
game_name_rectangle = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to restart',False,(111,196,169))
game_message_rectangle = game_message.get_rect(center = (400,320))

# Event timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

# while loop to ensure game runs repeatedly
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_gravity = -25

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20

            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rectangle_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rectangle_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                # snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_b:
        #        player_backward = -3

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
        #pygame.draw.rect(screen,'#c0e8ec',score_rectangle,10)
        #screen.blit(score_surface,score_rectangle)
        score = display_score()

        #snail_rectangle.x -= 4
        #if snail_rectangle.right <= 0: snail_rectangle.left = 800
        #screen.blit(snail_surface,snail_rectangle)

        # player_rectangle.left += 1
        # if player_rectangle.left == 800: player_rectangle.left = 0

        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)

        # obstacle movement
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)

        # collision algorithm
        game_active = collisions(player_rectangle,obstacle_rectangle_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rectangle)
        obstacle_rectangle_list.clear()
        player_rectangle.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}',False, (111,196,169))
        score_message_rectangle = score_message.get_rect(center = (400,330))

        screen.blit(game_name, game_name_rectangle)
        if score == 0:
            screen.blit(game_message,game_message_rectangle)
        else:
            screen.blit(score_message,score_message_rectangle)

    pygame.display.update()
    clock.tick(60)
