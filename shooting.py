from game_calculated import *


class CalculatedShootingField:
    def __init__(self):
        self.field = []
        for i in range(0, field_size):
            self.field.append([])
            for j in range(0, field_size):
                self.field[i].append(Cell(int(0)))

    def show_field(self):
        string = ""

        for i in range(0, field_size):
            string = ""
            for j in range(0, field_size):
               string += str(self.field[i][j].alive)

            print(string)


def get_where_shoot():
    x = int(input())
    y = int(input())

    if x > field_size or x < 0 or y > field_size or y < 0:
        get_where_shoot()

    return [x, y]


def make_shoot(field, shooting_field, field_2):
    if cheking_end_of_the_game(field) and cheking_end_of_the_game(field_2):
        coords = get_where_shoot()

        if shooting_field.field[coords[0]][coords[1]].alive == True:
            print("your shoot yhere")
            get_where_shoot()

        shooting_field.field[coords[0]][coords[1]].alive = True

        if field.make_shoot(coords[0], coords[1]) and cheking_end_of_the_game(field) and cheking_end_of_the_game(field_2):
            print("nice")
            make_shoot(field, shooting_field, field_2)

        return [field, shooting_field]

    return [field, shooting_field]

