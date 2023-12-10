from typing import List, Tuple, Union
import random


class Battleground:
    rotation = {
        "up":    (-1, 0),
        "down":  (1, 0),
        "right": (0, 1),
        "left":  (0, -1),
    }

    def __init__(self, col: int = 10, row: int = 10) -> None:
        self.row: int = row
        self.col: int = col
        self.grid: List[List[int]] = [[0] * row for _ in range(col)]

    def show_grid(self) -> None:
        """Shows field grid
        :return:
        """
        for row in self.grid:
            print(row)


    def is_valid_cell(self, x: int, y: int) -> bool:
        """Out of bounds check
        Returned True or False
        :param x:
        :param y:
        :return:
        """
        return 0 <= x < self.row and 0 <= y < self.col

    def has_ship_around(self, x: int, y: int, radius: int = 1) -> bool:
        # In future add Specific mark for each SHIP
        """Checking grid around current cell
        :param x:
        :param y:
        :param radius:
        :return:
        """
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                nx, ny = x + dx, y + dy
                if self.is_valid_cell(nx, ny) and self.grid[nx][ny] == 1:
                    return True
        return False

    def is_ship_placement_valid(self, x: int, y: int, rot: str, length: int) -> bool:
        # In future add check for incorrect "KEY" for placement
        """Check whole ship elemetns for correction
        - Check Validation [Out of bounds check]
        - Check Is there any ships around
        - Current cell check
        :param x:
        :param y:
        :param rot:
        :param length:
        :return:
        """
        for i in range(length):
            xr, yr = self.rotation[rot]
            new_x, new_y = x + i * xr, y + i * yr

            if (not self.is_valid_cell(new_x, new_y) or
                    self.grid[new_x][new_y] == 1 or
                    self.has_ship_around(new_x, new_y)):
                return False

        return True

    def place_ship(self, x: int, y: int, rot: str, length: int) -> None:
        # Change nickname because of Similar naming place_ship and place_ships
        """This function places ships without validation
        so it uses only after validation all cells"""

        cur_pos: List[int] = [x, y]
        for _ in range(length):
            xr, yr = self.rotation[rot]
            self.grid[cur_pos[0]][cur_pos[1]] = 1
            cur_pos[0] += xr
            cur_pos[1] += yr

    def auto_place_ships(self, ships: List[int] = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]) -> None:
        """Auto ship placement in grid
        :param ships:
        :return:
        """
        ship_lengths: List[int] = ships[:]

        for length in ship_lengths:
            ship_placed: bool = False

            while not ship_placed:
                x: int = random.randint(0, self.row - length)
                y: int = random.randint(0, self.col - length)
                rot: str = random.choice(list(self.rotation.keys()))

                if self.is_ship_placement_valid(x, y, rot, length):
                    self.place_ship(x, y, rot, length)
                    ship_placed = True


    def place_ships(self, ships: List[int] = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]) -> None:
        """Manual ship placement on grid
        :param ships:
        :return:
        """
        ship_lengths: List[int] = ships[:]

        for length in ship_lengths:
            ship_placed: bool = False

            while not ship_placed:
                try:
                    x, y, rot = map(
                        str,
                        input(
                            f"Enter coordinates and rotation (e.g., 'x y up') for a ship of length {length}: "
                        ).split(),
                    )
                    x, y = int(x), int(y)

                    if self.is_ship_placement_valid(x, y, rot, length):
                        self.place_ship(x, y, rot, length)
                        print("Ship placed successfully!")
                        ship_placed = True
                    else:
                        print("Invalid placement. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for coordinates.")

