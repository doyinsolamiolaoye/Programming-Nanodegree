#!/usr/bin/env python3
import random
import time
import string
import enum
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.mov = ""

    def move(self):
        # A player that always plays 'rock'
        return 'rock'

    def learn(self, my_move, their_move):
        self.mov = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def valid_input(que, options):
    while True:
        ans = input(que).lower()
        if ans in options:
            return ans


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def typewriter_simulator(message):
    # function to simulate typing
    for char in message:
        print(char, end='', flush=True)
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    # function to print and pause for two seconds after
    typewriter_simulator(Color.get_color() + message)
    time.sleep(delay)


class RandomPlayer(Player):
    # A player that chooses its moves randomly.
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    # Human player
    def __init__(self):
        super().__init__()

    def move(self):
        return valid_input("Rock, paper, scissors? >>>  ", moves)


class ReflectPlayer(Player):
    # Player that remembers & imitates what the human player played previously
    def __init__(self):
        super().__init__()

    def move(self):
        if self.mov == "":
            self.mov = random.choice(moves)
        else:
            self.learn(self.mov, self.mov)
        return self.mov


class CyclePlayer(Player):
    # A player that cycles through the three moves
    def __init__(self):
        super().__init__()

    def move(self):
        if self.mov == "":
            self.mov = random.choice(moves)
        else:
            idx = moves.index(self.mov)
            idx = (idx + 1) % len(moves)
            self.mov = moves[idx]
        return self.mov


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.check_winner(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def check_winner(self, move1, move2):
        if move1 == move2:
            print_pause("**TIE**")
        elif beats(move1, move2):
            self.p1.score += 1
            print_pause(f"**PLAYER ONE WINS**")
        else:
            self.p2.score += 1
            print_pause(f"**PLAYER TWO WINS**")
        print_pause(f"Score: Player One {self.p1.score}, Player Two "
                    f"{self.p2.score}")

    def play_game(self):
        print_pause("Game start!")
        for round in range(3):
            print_pause(f"Round {round}: ---")
            self.play_round()
            print("\n")

        self.announce_winner()
        print_pause("Game ENDS!")

    def announce_winner(self):
        print_pause("*** TOTAL SCORE ***")
        print_pause(f"PLAYER ONE: {self.p1.score} \nPLAYER TWO: "
                    f"{self.p2.score}")
        if self.p1.score > self.p2.score:
            print_pause("PLAYER ONE WINS!")
        elif self.p1.score < self.p2.score:
            print_pause("PLAYER TWO WINS")
        else:
            print_pause("DRAW!!")


if __name__ == '__main__':
    strategies = {"1": Player(),
                  "2": RandomPlayer(),
                  "3": CyclePlayer(),
                  "4": ReflectPlayer()}

    que = ("Select the player you want to play against:\n1-Rock Player"
           "\n2-Random Player\n3-Cycle Player\n4-Reflect Player\n")

    user_input = valid_input(que, ["1", "2", "3", "4"])

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
