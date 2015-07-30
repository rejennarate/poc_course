"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class()

    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([0]), "Test #0: init")

    # test the set_board and get_num_seeds methods
    config1 = [0, 0, 1, 1, 3, 5, 0]
    game.set_board(config1)
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: set_board")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")

    # test the is_game_won method
    suite.run_test(game.is_game_won(), False, "Test #2: is_game_won")

    # test the is_legal_move method
    suite.run_test(game.is_legal_move(0), False, "Test #3a: is_legal_move")
    suite.run_test(game.is_legal_move(1), False, "Test #3b: is_legal_move")
    suite.run_test(game.is_legal_move(2), False, "Test #3c: is_legal_move")
    suite.run_test(game.is_legal_move(3), False, "Test #3d: is_legal_move")
    suite.run_test(game.is_legal_move(4), False, "Test #3e: is_legal_move")
    suite.run_test(game.is_legal_move(5), True, "Test #3f: is_legal_move")
    suite.run_test(game.is_legal_move(6), False, "Test #3g: is_legal_move")

    # test the apply_move method - not sure why this method returns "none"
    # suite.run_test(game.apply_move(5), [0, 0, 4, 2, 2, 1, 1], "Test #4: apply_move")

    # test the choose_move method
    suite.run_test(game.choose_move(), 5, "Test #5: choose_move")

    # report number of tests and failures
    suite.report_results()
