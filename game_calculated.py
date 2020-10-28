field_size = 3


class Cell:
    def __init__(self, alive):
        self.alive = alive


class CalculatedField():
    def __init__(self, field):
        self.__field = field

    def show_field(self):
        string = ""

        for i in range(0, field_size):
            string = ""

            for j in range(0, field_size):
               string += self.__field[i][j].alive

            print(string)


# this function chacking the field that make a people
def checking_field(field):
    return True


def make_field_for_player():
    field = []

    for i in range(0, field_size):
        field.append([])
        for j in range(0, field_size):
            field[i].append(Cell(input()))

    if checking_field(field) is False:
        make_field_for_player()

    return field
