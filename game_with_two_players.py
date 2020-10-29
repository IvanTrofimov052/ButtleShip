from game_calculated import *
from shooting import *


# this function for game for two players
def game_with_two_players():
    print('Game with two players')

    player_1_field = CalculatedField(make_field_for_player())
    player_1_field.show_field()

    player_2_field = CalculatedField(make_field_for_player())
    player_2_field.show_field()

    player_1_shooting_field = CalculatedShootingField()
    player_2_shooting_field = CalculatedShootingField()

    while cheking_end_of_the_game(player_1_field) and cheking_end_of_the_game(player_2_field):
        print ('start shooting firts')
        player_2_field, player_2_shooting_field = make_shoot(player_2_field, player_2_shooting_field, player_1_field)
        print('start shooting second')
        player_1_field, player_1_shooting_field = make_shoot(player_1_field, player_1_shooting_field, player_2_field)

    if cheking_end_of_the_game(player_1_field) == True:
        print("Wins the firs player")
    else:
        print("Wins the second player")

    player_1_field.show_field()
    player_2_field.show_field()