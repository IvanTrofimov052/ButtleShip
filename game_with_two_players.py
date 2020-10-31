from game_calculated import *
from shooting import *


def game_with_two_players(array_first_player, array_second_player, who, x, y):
    if who == 1:
        result, array_first_player[0], array_first_player[1] = make_shoot(array_first_player[0],
                                                                            array_first_player[1], x, y)

        if (result == 'past'):
            who = 2
        else:
            who = 1
    else:
        result, array_second_player[0], array_second_player[1] = make_shoot(array_second_player[0],
                                                                              array_second_player[1], x, y)
        if (result == 'past'):
            who = 1
        else:
            who = 2

    return [who, array_first_player, array_second_player, result]