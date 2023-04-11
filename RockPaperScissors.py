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
        print("Input choice: press 0 for rock, 1 paper or 2 for scissor: ")
        self.player_choice = self.check_input()
        return self.player_choice

    def out_of_bounds(self):
        if self.player_choice < 0 or self.player_choice > 3:
            print("ERROR WITH CHOICE! TRY AGAIN")
        else:
            self.check_who_won()

    def get_number_of_games(self):
        print("Please enter number of rounds,press 1 for 3 rounds, 2 for 5 rounds or 3 for 10 rounds: ")
        self.level = self.check_input()
        self.level = self.set_number_of_games()
        return self.level

    def set_number_of_games(self):
        if self.level == 1:
            return RockPaperScissors.BEST_OF_THREE_GAMES
        elif self.level == 2:
            return RockPaperScissors.BEST_OF_FIVE_GAMES
        elif self.level == 3:
            return RockPaperScissors.BEST_OF_TEN_GAMES
        self.check_number_of_rounds()
        return self.level

    def check_number_of_rounds(self):
        if self.level < 1 or self.level > 3:
            print("INVALID CHOICE")
            self.get_number_of_games()
        else:
            self.get_player_choice()

    def get_computer_choice(self):
        return random.randint(0,2)

    def print_out_computer_choice(self):
        self.computer_choice = self.get_computer_choice()
        print(f"you chose level {self.turn}")
        print("Computer chose: ")
        print(RockPaperScissors.game_images[self.computer_choice])
        print("Player chose: ")
        print(RockPaperScissors.game_images[self.player_choice])

    def check_who_won(self):
        self.print_out_computer_choice()
        if self.player_choice == 0 and self.computer_choice == 0:
            self.player_score +=1
            self.print_score()
            self.check_score(self.player_score)
        elif self.computer_choice == 0 and self.player_choice == 2:
            self.computer_score +=1
            self.print_score()
            self.check_score(self.computer_score)
        elif self.computer_choice > self.player_choice:
            self.computer_score +=1
            self.print_score()
            self.check_score(self.computer_score)
        elif self.player_choice > self.computer_choice:
            self.player_score +=1
            self.print_score()
            self.check_score(self.player_score)
        elif self.computer_choice == self.player_choice:
            print("DRAW!")

    def print_score(self):
        print(f"Player score is {self.player_score}")
        print(f"Computer score is {self.computer_score}")

    def check_score(self,score):
        if score >= self.turn:
            self.ask()
            self.ask_to_play_again()

    def ask(self):
        print("Do you want to play again: ")
        self.play_again = self.check_input()


    def ask_to_play_again(self):
        while self.play_again != 1 and self.play_again != 2:
            self.out_of_bounds_check_two()
            self.play_again = int(input("Press 1 to play again or 2 to quit:"))

        if self.play_again == 2:
            self.game_over = True
        else:
            self.player_score = 0
            self.computer_score = 0
            self.turn = self.get_number_of_games()


    def out_of_bounds_check_two(self):
        if self.play_again < 1 or self.play_again > 2:
            print("INVALID CHOICE! TRY AGAIN!")


    def check_input(self):
        while True:
            try:
                input_ = int(input(""))
                return input_
            except ValueError:
                print("INVALID INPUT")