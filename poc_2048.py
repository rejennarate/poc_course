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
    result_list = []

    for number in line:
        result_list.insert(0,0)
        if number != 0:
            result_list.remove(0)
            result_list.append(number)

    for number in line:
        if number == 0:
            result_list.remove(0)
            result_list.append(0)

    # Iterate over the list created in the previous step and create another new list
    # in which pairs of tiles in the first list are replaced with a tile of
    # twice the value and a zero tile.
    #for number in result_list:



    pairs = zip(result_list, result_list[1:])
    print pairs
    for num1, num2 in pairs:
        if num1 == num2 and num1 != 0 and num2 != 0:
            merged_num = num1+num2
            result_list.insert(num1, 0)
            result_list.insert(num1, merged_num)
            del result_list[:num2]
    #     for x, y in zip(result_list, result_list[1:]):
    #         #print result_list
    #         print x, y
    #         print result_list
            #if x == y:
                #merged_num = [x+y,0]
                #del result_list[x:y]
                #print result_list
                #result_list.insert(x, merged_num)
                #print result_list
            # elif x!= y:
            #     result_list.remove(x)
            #     result_list.append(x)

    for number in result_list:
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
    # maybe also test that len(line) matches len(result_list)

test_merge()