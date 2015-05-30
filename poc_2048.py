"""
implementation of 2048 game

goal: merge all pairs of like values in a single row or column
"""

# class Game2048:

    # def __init__(self):


def merge(line):
    """
    models the process of merging all of the tile values in a single row or column.
    This function takes the list line as a parameter and returns a new list with
    the tile values from line slid towards the front of the list and merged.
    Note that you should return a new list and you should not modify the input list.
    """



def test_merge():
    """
    test code for merge function
    """

    line1 = [2, 0, 2, 4]
    line2 = [0, 0, 2, 2]
    line3 = [2, 2, 0, 0]
    line4 = [2, 2, 2, 2, 2]
    line5 = [8, 16, 16, 8]

    # put this in a loop
    print "Testing line1 - Computed:" merge(line1), "Expected:", [4, 4, 0, 0]
    print "Testing line2 - Computed:" merge(line2), "Expected:", [4, 0, 0, 0]
    print "Testing line3 - Computed:" merge(line3), "Expected:", [4, 0, 0, 0]
    print "Testing line4 - Computed:" merge(line4), "Expected:", [4, 4, 2, 0, 0]
    print "Testing line5 - Computed:" merge(line5), "Expected:", [8, 32, 8, 0]