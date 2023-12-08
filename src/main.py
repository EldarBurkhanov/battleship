from player import Player, Bot, Human
from game import Game

player1: Player = Human("Riki")
player2: Player = Bot("Nikita")

def start(player1, player2):
    game = Game(player1, player2)
    game.start_battle()

if __name__ == '__main__':
    start(player1, player2)