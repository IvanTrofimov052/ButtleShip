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

