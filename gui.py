from game_with_two_players import *
from game_calculated import *
from shooting import *

# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 50 * field_size + 250
HEIGHT = 50 * field_size
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

# class DrawingCell:
#     def __init__(self,x ,y, alive):
#         self.x = x
#         self.y = y
#         self.alive = alive
#
#
# class DrawingShootingFiel:
#     def __init__(self, x, y, field):
#         for i in range()

def draw_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j].alive is True:
                pygame.draw.rect(screen, GREEN, (j*50, i*50, 49, 49))
            else:
                pygame.draw.rect(screen, RED, (j*50, i*50, 49, 49))

game_mode = 0
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

            who = 1

            game_mode = 1

    if game_mode == 1:
        if who == 1:
            x = int ( input () )
            y = int ( input () )

            result = game_with_two_players(array_first_player, array_second_player, who, x, y )

            who = result[0]
            array_first_player = result[1]
            array_second_player = result[2]

            array_first_player[1].show_field()

            print('fck')
        else:
            x = int ( input () )
            y = int ( input () )

            result = game_with_two_players(array_first_player, array_second_player, who, x, y)

            who = result[0]

            array_first_player = result[1]
            array_second_player = result[2]

            print('nnn')

            array_second_player[1].show_field()

        # Рендеринг
        screen.fill ( WHITE )

        myfont_1 = pygame.font.SysFont("monospace", 50)

        if who == 1:
            draw_field(array_first_player[1].field)
        else:
            draw_field(array_second_player[1].field)


        label = myfont_1.render(result[3], 1, (0, 0, 0))
        screen.blit(label, (200, 0))

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
    else:
        # Обновление

        # Рендеринг
        screen.fill(WHITE)
        # render text
        label = myfont.render("Click 1 button - to play with another player  Click 2 button - to play with easy bot Click 3 button - to play with easy bot", 1, (0, 0, 0))
        screen.blit(label, (100, 100))
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

pygame.quit()