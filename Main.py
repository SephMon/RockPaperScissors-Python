from RockPaperScissors import RockPaperScissors

r = RockPaperScissors()


def welcome_message():
    print("*************************")
    print("*       Welcome to      *")
    print("*    RockPaperScissors  *")
    print("*************************")


welcome_message()

while not r.game_over:
    r.player_choice = r.get_player_choice()
    r.out_of_bounds()



