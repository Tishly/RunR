import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("RunR")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('images/backgrounds_1.png')
ground_surface = pygame.image.load('images/backgrounds_2.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))

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
