"""
implementation of 2048 game

goal: merge all pairs of like values in a single row or column
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    models the process of merging all of the tile values in a single row or column.
    This function takes the list line as a parameter and returns a new list with
    the tile values from line slid towards the front of the list and merged.
    Note that you should return a new list and you should not modify the input list.
    """
    result_list = []

    for number in line[:]:
        result_list.insert(0,0)
        if number != 0:
            result_list.remove(0)
            result_list.append(number)

    for number in line[:]:
        if number == 0:
            result_list.remove(0)
            result_list.append(0)

    for idx, val in enumerate(result_list[:]):
        if idx+1 < len(result_list):
            if result_list[idx] == result_list[idx+1] and result_list[idx] != 0:
                result_list[idx] = val*2
                result_list[idx+1] = 0

    for number in result_list:
        if number == 0:
            result_list.remove(0)
            result_list.append(0)

    return result_list


def traverse_grid(start_cell, direction, num_steps):
    """
    method to traverse the grid, used to capturing initial tiles
    """
    for step in range(num_steps):
        dummy_row = start_cell[0] + step * direction[0]
        dummy_col = start_cell[1] + step * direction[1]


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._initial_tiles = {LEFT: traverse_grid((0, 0), (1, 0), grid_height),
                               UP: traverse_grid((0,0), (0,1), grid_height),
                               RIGHT: traverse_grid((0, grid_width - 1), (1, 0), grid_height),
                               DOWN: traverse_grid((grid_height - 1, 0), (0, 1), grid_width)}

        # self._initial_tiles[LEFT]
        # self._initial_tiles[UP]
        # self._initial_tiles[RIGHT]
        # self._initial_tiles[DOWN]


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_col in range(self._grid_width)]
                          for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in self._board:
            return str(row)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # this might be the place to use the 'direction' param
        # to determine how the algorithm is applied in 'merge'

        print self._initial_tiles[direction]


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # sample = [[0, 0, 2, 4], [4, 0, 4, 0], [8, 4, 2, 0]]
        random_tile = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        random_row = (random.randint(0, self._grid_height-1))
        random_col = (random.randint(0, self._grid_width-1))

        if self.get_tile(random_row, random_col) == 0:
            self.set_tile(random_row, random_col, random_tile)
        # why do sometimes get only one tile?
        # maybe the same random index is being selected twice?


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]


def test_merge():
    """
    tests for merge function
    """

    line1 = [2, 0, 2, 4]
    line2 = [0, 0, 2, 2]
    line3 = [2, 2, 0, 0]
    line4 = [2, 2, 2, 2, 2]
    line5 = [8, 16, 16, 8]
    line6 = [8, 8]
    line7 = [4, 4, 8, 8]

    # put this in a loop
    print "Testing line1 - Computed:", merge(line1), "Expected:", [4, 4, 0, 0]
    print "Testing line2 - Computed:", merge(line2), "Expected:", [4, 0, 0, 0]
    print "Testing line3 - Computed:", merge(line3), "Expected:", [4, 0, 0, 0]
    print "Testing line4 - Computed:", merge(line4), "Expected:", [4, 4, 2, 0, 0]
    print "Testing line5 - Computed:", merge(line5), "Expected:", [8, 32, 8, 0]
    print "Testing line6 - Computed:", merge(line6), "Expected:", [16, 0]
    print "Testing line7 - Computed:", merge(line7), "Expected:", [8, 16, 0, 0]
    # maybe also test that len(line) matches len(result_list)


def test_full():
    """
    tests for whole game
    """
    gridsize1 = 4, 4
    new_game = TwentyFortyEight(gridsize1)

    print "Testing init - Computed:", new_game, "Expected:",
    print "Testing get_tile - Computed:", new_game.get_tile(0,3), "Expected:",



# test_merge()
# test_full()
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))




