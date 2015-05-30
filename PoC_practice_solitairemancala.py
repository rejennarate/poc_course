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
        self._starting_configuration = [0]
        self._current_configuration = []

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._starting_configuration = configuration
        # if current_configuration is already set, return so that current_configuration isn't overwritten
        self._current_configuration = self._starting_configuration[::-1]


    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self._current_configuration)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._starting_configuration[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        non_empty_houses = 0
        for seeds in self._current_configuration[:-1]:
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
        num_seeds = self._current_configuration[house_num]

        list_length = len(self._current_configuration)-1
        # print num_seeds # 2
        # print list_length # 3
        # print house_num # 1
        # print self._current_configuration # [4, 2, 2, 0]

        # the move is legal if the number of seeds is exactly equal to the number of houses/store to its right
        # list length is not the way to do this because with different sized lists, it fails
        if num_seeds == (list_length - house_num) and num_seeds != 0:
            print num_seeds
            # print house_num
            # print list_length
            # print self._current_configuration.index(-1)
            # print 'true'
            return True
        else:
            print num_seeds
            #print 'false'
            return False

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        # current_configuration = [0, 5, 3, 1, 1, 0, 0]
        # keep the value of house_num in a variable before clobbering it with 0
        previous_seeds = self._current_configuration[house_num]
        self._current_configuration[house_num] = 0
        left_side = self._current_configuration[:house_num+1]

        # should probably add + 1 to seeds in list until previous_seeds = 0
        # decrement using previous_seeds -= 1
        right_side = [seeds + 1 for seeds in self._current_configuration[house_num+1:]]
        self._current_configuration = left_side + right_side
        return self._current_configuration


    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in reversed(self._current_configuration):
            # print self._current_configuration
            # print house_num
            if self.is_legal_move(house_num) == True:
                print "true"
                # print self.is_legal_move(house_num)
                return house_num
            else:
                print "false"
                # print self._current_configuration
                return self._current_configuration[-1]

        #return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
		After each move, move the seeds in the house closest to the store
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        return []


# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    # config1 = [0, 0, 1, 1, 3, 5, 0]
    config1 = [0, 2, 2]
    my_game.set_board(config1)

    #print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    #print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    #print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    #print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    #print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected", False
    #print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected", False
    #print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected", False
    #print "Testing is_legal_move - Computed:", my_game.is_legal_move(4), "Expected", False
    # print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected", False
    # print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected", False
    #print "Testing apply_move - Computed:", my_game.apply_move(1), "Expected", [0, 0, 4, 2, 2, 1, 1]
    #print "Testing choose_move - Computed:", my_game.choose_move(), "Expected", 4
    # add more tests here

test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())








