from game_calculated import *
from shooting import *

# this function initilization player - make his fields
def init_player(field):
    player_field = CalculatedField(field)
    shooting_field = CalculatedShootingField()

    return [player_field, shooting_field]


# this function make a shoot
def make_shoot(field, shooting_field, x, y):
        if shooting_field.field[x][y].alive == True:
            return ["Your shoot here", field, shooting_field]

        shooting_field.field[x][y].alive = True

        if field.make_shoot(x, y):
            return ["strike", field, shooting_field]

        return ['past', field, shooting_field]
