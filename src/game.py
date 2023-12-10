from enums import ShootResult

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.enemy_player = player2
        self.winner = None
        self.player1.set_ships()
        self.player2.set_ships()


    def change_player(self):
        self.current_player, self.enemy_player = self.enemy_player, self.current_player

    def show_player_field(self):
        print(f"{self.current_player} turn to pick!")
        print(f"==============={self.current_player.name}================")
        self.current_player.field.show_grid()
        print("===========================================")
        self.current_player.draft_field.show_grid()

    def start_battle(self):
        while self.winner is None:
            self.show_player_field()
            x, y = self.current_player.select_coords()
            answer = self.enemy_player.check_cell(x, y)
            if answer == ShootResult.miss:
                self.current_player.draft_field.grid[x][y] = ShootResult.miss.value
                self.change_player()
            elif answer == ShootResult.kill:
                self.current_player.draft_field.grid[x][y] = ShootResult.ally_ship_dead.value
                self.enemy_player.field.grid[x][y] = ShootResult.kill.value
                if not self.enemy_player.has_ships():
                    self.winner = self.current_player
                    print(f"{self.current_player} won!")