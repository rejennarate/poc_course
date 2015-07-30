"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]


    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self._board[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        non_empty_houses = 0
        for seeds in self._board:
            if seeds > 0:
                non_empty_houses += 1

        if non_empty_houses > 0:
            return False
        else:
            return True

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        num_seeds = self._board[house_num]

        # the move is legal if the number of seeds is exactly equal to its house number
        if num_seeds == house_num and num_seeds != 0:
            return True
        elif house_num == 0:
            return False
        else:
            return False

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """

        if self.is_legal_move(house_num):
            for idx in range(house_num):
                self._board[idx] += 1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1, len(self._board)):
            if self.is_legal_move(house_num):
                return house_num

        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
		After each move, move the seeds in the house closest to the store
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        plan_board = list(self._board)
        legal_moves = []
        for house_num in range(len(plan_board)):
            if self.is_legal_move(house_num):
                self.apply_move(house_num)
                legal_moves.append(house_num)

        return legal_moves


# Create tests to check the correctness of your code



# Import GUI code once you feel your code is correct
import poc_mancala_gui
import poc_mancala_testsuite
poc_mancala_gui.run_gui(SolitaireMancala())
poc_mancala_testsuite.run_suite(SolitaireMancala)