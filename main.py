# TODO: checking_field
# TODO: in make_field_for_player link for cell neightboards
# TODO: shooting field
# TODO: shooting
# TODO: stoping the game


from game_with_two_players import *
from game_with_easy_bot import *
from game_with_hard_bot import *


# this function return the method of creating account that choose user
def get_method_of_game():
    method_of_game = input()

    return method_of_game


def main():
    # get the methos of creating account
    method_of_game = get_method_of_game()

    # there we start game depending on method of game
    if "two players" in method_of_game:
        game_with_two_players()
    elif "easy bot" in method_of_game:
        game_with_easy_bot()
    else:
        game_with_hard_bot()


main()