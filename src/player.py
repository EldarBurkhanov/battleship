from enums import ShootResult
from field import Battleground
import random


class Player:

    def __init__(self, name):
        self.name = name
        self.field = Battleground()
        self.draft_field = Battleground()

    def set_ships(self):
        raise NotImplemented("Must be implemented in sub-classes!")


    def select_coords(self) -> tuple[int, int]:
        raise NotImplemented("Must be implemented in sub-classes!")

    def check_cell(self, x, y) -> ShootResult:
        if self.field.grid[x][y] == 0:
            print(f"{x} {y} miss!")
            return ShootResult.miss
        elif self.field.grid[x][y] == 1:
            print(f"{x} {y} hit!")
            self.field.grid[x][y] = 3
            return ShootResult.kill

    def has_ships(self) -> bool:
        for i in self.field.grid:
            for j in i:
                if j == 1:
                    return True

        return False

    def __repr__(self):
        return self.name


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def set_ships(self):
        self.field.auto_place_ships()
        print(f"All ships for Bot succesfully instaled!")

    def select_coords(self) -> tuple[int, int]:
        x = random.randint(0, len(self.field.grid) - 1)
        y = random.randint(0, len(self.field.grid[0]) - 1)
        return x, y


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def select_coords(self) -> tuple[int, int]:
        while True:
            x, y = map(int, input(f"{self.name}, enter coords: ").split())
            if 0 <= x <= 9 and 0 <= y <= 9:
                return x, y
            print("Coordinates out of bounds.")

    def set_ships(self):
        self.field.place_ships()
        print(f"All ships for player {self.name} successfully installed!")

