from game_calculated import *

# this function for game for two players
def game_with_two_players():
    player_1_field = CalculatedField(make_field_for_player())
    player_1_field.show_field()
    player_2_field = CalculatedField(make_field_for_player())
    player_2_field.show_field()
    print("Game with Players start")