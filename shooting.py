from game_calculated import *


class CalculatedShootinField:
    field = []

    def __init__(self):
        for i in range(0, field_size):
            self.field.append([])
            for j in range(0, field_size):
                self.field[i].append(Cell(int(0)))


def get_where_shoot():
    x = int(input())
    y = int(input())

    if x > field_size or x < 0 or y > field_size or y < 0:
        get_where_shoot()

    return [x, y]


def make_shoot(field, shooting_field):
    coords = get_where_shoot()

    if shooting_field.field[coords[0]][coords[1]].alive == True:
        get_where_shoot()

    if field.make_shoot(coords[0], coords[1]):
        shooting_field.field[coords[0]][coords[1]].alive = True

        make_shoot(field, shooting_field)

