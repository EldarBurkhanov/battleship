from player import Player, Bot, Human
from game import Game

def create_player(player_type: str, player_name: str) -> Player:
    """Creates an instance of bot or player based on player input before game starts
    :param player_type:
    :param player_name:
    :return:
    """
    if player_type == 'bot':
        return Bot(player_name)
    elif player_type == 'human':
        return Human(player_name)

def get_player_input(player_number: int) -> tuple[str, str]:
    """Gets pre-game information about players for seting presset and validate info
    :param player_number:
    :return:
    """
    while True:
        player_type = input(f"Enter type of player {player_number} (bot/human): ").lower()
        player_name = input(f"Enter nickname for player {player_number}: ")

        if player_type in ['bot', 'human']:
            return player_type, player_name
        else:
            print("Invalid player type. Please enter 'bot' or 'human'.")

def start():
    """Game starter
    :return:
    """
    player1_type, player1_name = get_player_input(1)
    player2_type, player2_name = get_player_input(2)

    player1 = create_player(player1_type, player1_name)
    player2 = create_player(player2_type, player2_name)

    game = Game(player1, player2)
    game.start_battle()

if __name__ == '__main__':
    start()

