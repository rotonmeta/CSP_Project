from test import Test
from csp import *


def main():
    time = []
    back_track = []
    # number of tests to be made on a chosen puzzle
    n_test = 5
    # inference specifies which inference to choose for executing the tests
    # we can choose between: no_inference, forward_checking and mac
    inference = mac
    # var_sel specifies the order in which will be chosen the unassigned variable
    # we can choose between: first_unassigned_variable and mrv (minimum remaining values)
    var_sel = first_unassigned_variable
    # level chooses difficulty (higher is more difficult)
    # level 1 is Easy, level 2 is Medium, level 3 is Hard, level 4 is Evil, level 5 is "Hardest"
    level = 1

    for i in range(n_test):
        test = Test()
        test.choose_puzzle(level)
        test.execute(inference, var_sel)
        back_track.append(test.bt)
        time.append(round(test.end - test.start, 5))

    print("Average time: " + str(round(sum(time) / len(time), 3)))
    print("Average backtrack: " + str(round(sum(back_track) / len(back_track))))


if __name__ == '__main__':
    main()


