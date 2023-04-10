import random
from random import randint

class RockPaperScissors:
    
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]
    BEST_OF_THREE_GAMES = 3
    BEST_OF_FIVE_GAMES = 5
    BEST_OF_TEN_GAMES = 10
    
    def __init__(self):
        self.turn = self.get_number_of_games()
        self.game_over = False
        self.player_score = 0
        self.computer_score = 0
        self.play_again = self.ask_to_play_again
        
    def get_player_choice(self):
        print("Input choice: press 0 for rock,1 for paper or 2 for scissors: ")
        self.player_choice = self.check_player_input()
        return self.player_choice

    def check_for_out_of_bounds_choice(self):
        if self.player_choice < 0 or self.player_choice > 2:
            print("ERROR WITH CHOICE! PLEASE ONLY CHOOSE OPTION 0,1 OR 2!")
        else:
            self.check_who_won()
    
    def get_number_of_games(self):
        pass

    def set_number_of_games(self):
        pass

    def check_number_of_rounds(self):
        pass

    def get_computer_choice(self):
        pass

    def print_out_computer_choice(self):
        pass

    def check_who_won(self):
        pass

    def print_scores(self):
        pass

    def check_score(self):
        pass

    def ask_player_to_play_again(self):
        pass

    def ask_to_play_again(self):
        pass

    def check_if_choice_is_out_of_bounds(self):
        pass

    def check_player_input(self):
        while True:
            try:
                input_ = int(input(""))
                return input_
            except ValueError:
                print("INVALID INPUT,TRY AGAIN!")

    







