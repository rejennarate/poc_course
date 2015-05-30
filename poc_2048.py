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
    #print line.count(0)
    #print line.count(2)
    #print line.count(4)
    #print line

    # create a result list with the same number of 0s as the length of line
    # iterate over the line input looking for non-zero entries. For each non-zero entry,
    # put the value into the next available entry of the result list (starting at position 0).
    result_list = []

    for number in line:
        result_list.insert(0,0)
        if number != 0:
            result_list.remove(0)
            #this won't work because it moves the order of the last numbers unless there's only one 0
            result_list.append(number)

    for number in line:
        if number == 0:
            result_list.remove(0)
            result_list.append(0)

    return result_list

def test_merge():
    """
    tests for merge function
    """

    line1 = [2, 0, 2, 4]
    line2 = [0, 0, 2, 2]
    line3 = [2, 2, 0, 0]
    line4 = [2, 2, 2, 2, 2]
    line5 = [8, 16, 16, 8]

    # put this in a loop
    print "Testing line1 - Computed:", merge(line1), "Expected:", [4, 4, 0, 0]
    print "Testing line2 - Computed:", merge(line2), "Expected:", [4, 0, 0, 0]
    print "Testing line3 - Computed:", merge(line3), "Expected:", [4, 0, 0, 0]
    print "Testing line4 - Computed:", merge(line4), "Expected:", [4, 4, 2, 0, 0]
    print "Testing line5 - Computed:", merge(line5), "Expected:", [8, 32, 8, 0]

test_merge()