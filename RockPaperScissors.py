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
        
    
    