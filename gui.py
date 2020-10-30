from game_with_two_players import *
from game_calculated import *

# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1000
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 10)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get ():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('Make field for first player')
            field_1 = make_field_for_player()
            print('Make field for second player')
            field_2 = make_field_for_player()
            print('Nice we made two fields')

            array_first_player = init_player(field_1)
            array_second_player = init_player(field_2)

    # Обновление

    # Рендеринг
    screen.fill(WHITE)
    # render text
    label = myfont.render("Click 1 button - to play with another player  Click 2 button - to play with easy bot Click 3 button - to play with easy bot", 1, (0, 0, 0))
    screen.blit ( label, (100, 100) )
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit ()