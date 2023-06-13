import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("RunR")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('images/Sky.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert()
text_surface = test_font.render('My game', False, 'Orange')

snail_surface = pygame.image.load('images/snail/snail2.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (700,300))
# snail_x_position = 700

player_surface = pygame.image.load('images/player/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(350,50))
    # snail_x_position -= 3
    # if snail_x_position < -100:
        # snail_x_position = 800
    snail_rectangle.right -= 4
    if snail_rectangle.right <= 0: snail_rectangle.left = 800
    screen.blit(snail_surface,snail_rectangle)
    # player_rectangle.left += 1
    screen.blit(player_surface,player_rectangle)

    pygame.display.update()
    clock.tick(60)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
