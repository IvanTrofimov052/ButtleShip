field_size = 3
cout_cell = 3


class Cell:
    neightboards = []

    def __init__(self, alive):
        self.alive = bool(alive)


class CalculatedField():
    def __init__(self, field):
        self.__field = field

    def show_field(self):
        string = ""

        for i in range(0, field_size):
            string = ""
            for j in range(0, field_size):
               string += str(self.__field[i][j].alive)

            print(string)

    def make_shoot(self, x, y):
        if self.__field[x][y].alive is True:
            self.__field[x][y].alive = False

            return True

        return False

    def get_field(self):
        return self.__field


# this function chacking the field that make a people
def checking_field(field):
    cout = 0

    for i in range(0, field_size):
        for j in range(0, field_size):
            cout += field[i][j].alive

    return cout == cout_cell


def make_field_for_player():
    field = []

    for i in range(0, field_size):
        field.append([])
        for j in range(0, field_size):
            field[i].append(Cell(int(input())))

    for i in range(0, field_size):
        for j in range(0, field_size):
            field[i][j].neightboards.append(field[(i+1) % field_size][j])
            field[i][j].neightboards.append(field[(i + 1) % field_size][(j + 1) % field_size])
            field[i][j].neightboards.append(field[(i - 1) % field_size][j])
            field[i][j].neightboards.append(field[(i + 1) % field_size][(j - 1) % field_size])
            field[i][j].neightboards.append(field[i][(j - 1) % field_size])
            field[i][j].neightboards.append(field[i][(j + 1) % field_size])
            field[i][j].neightboards.append(field[(i - 1) % field_size][(j + 1) % field_size])
            field[i][j].neightboards.append(field[(i - 1) % field_size][(j - 1) % field_size])

    if checking_field(field) is False:
        make_field_for_player()

    return field


def cheking_end_of_the_game(field):
    array = field.get_field()

    for i in range(0, field_size):
        for j in range(0, field_size):
            if array[i][j].alive == True:
                return True

    return False