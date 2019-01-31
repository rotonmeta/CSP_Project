from sudoku import *
from timeit import default_timer as timer


class Test:
    def __init__(self):
        self.puzzle = [[0 for col in range(9)] for row in range(9)]
        self.start = 0
        self.end = 0
        self.bt = 0
    # more explanation in the PDF paper that explains the work and the results

    def choose_puzzle(self, level):
        if level == 1:
            self.puzzle[0] = [7, 3, 0, 9, 0, 8, 0, 0, 0]
            self.puzzle[1] = [2, 0, 0, 0, 0, 0, 0, 8, 4]
            self.puzzle[2] = [8, 0, 0, 0, 6, 0, 3, 7, 0]
            self.puzzle[3] = [1, 0, 2, 0, 9, 6, 7, 0, 0]
            self.puzzle[4] = [5, 0, 0, 7, 0, 1, 0, 0, 8]
            self.puzzle[5] = [0, 0, 4, 8, 2, 0, 6, 0, 1]
            self.puzzle[6] = [0, 5, 3, 0, 8, 0, 0, 0, 9]
            self.puzzle[7] = [9, 2, 0, 0, 0, 0, 0, 0, 7]
            self.puzzle[8] = [0, 0, 0, 3, 0, 9, 0, 2, 6]

        if level == 2:
            self.puzzle[0] = [4, 0, 0, 0, 2, 0, 0, 0, 0]
            self.puzzle[1] = [8, 0, 5, 0, 0, 7, 4, 0, 0]
            self.puzzle[2] = [0, 9, 1, 4, 6, 0, 0, 3, 0]
            self.puzzle[3] = [0, 5, 0, 0, 9, 0, 2, 4, 0]
            self.puzzle[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0]
            self.puzzle[5] = [0, 4, 8, 0, 7, 0, 0, 1, 0]
            self.puzzle[6] = [0, 3, 0, 0, 8, 1, 6, 7, 0]
            self.puzzle[7] = [0, 0, 7, 6, 0, 0, 5, 0, 3]
            self.puzzle[8] = [0, 0, 0, 0, 5, 0, 0, 0, 9]

        if level == 3:
            self.puzzle[0] = [0, 7, 0, 0, 0, 2, 6, 0, 0]
            self.puzzle[1] = [0, 0, 6, 0, 0, 5, 3, 0, 0]
            self.puzzle[2] = [0, 2, 0, 0, 3, 0, 0, 0, 0]
            self.puzzle[3] = [8, 9, 0, 0, 0, 0, 2, 0, 0]
            self.puzzle[4] = [0, 6, 0, 4, 0, 3, 0, 1, 0]
            self.puzzle[5] = [0, 0, 1, 0, 0, 0, 0, 5, 4]
            self.puzzle[6] = [0, 0, 0, 0, 1, 0, 0, 9, 0]
            self.puzzle[7] = [0, 0, 7, 2, 0, 0, 5, 0, 0]
            self.puzzle[8] = [0, 0, 9, 8, 0, 0, 0, 7, 0]

        if level == 4:
            self.puzzle[0] = [0, 0, 0, 0, 0, 0, 3, 4, 0]
            self.puzzle[1] = [0, 0, 0, 0, 8, 0, 0, 0, 0]
            self.puzzle[2] = [0, 0, 0, 4, 0, 2, 0, 5, 7]
            self.puzzle[3] = [0, 0, 2, 0, 9, 3, 0, 6, 8]
            self.puzzle[4] = [0, 0, 3, 6, 0, 5, 7, 0, 0]
            self.puzzle[5] = [5, 6, 0, 8, 2, 0, 1, 0, 0]
            self.puzzle[6] = [7, 3, 0, 1, 0, 8, 0, 0, 0]
            self.puzzle[7] = [0, 0, 0, 0, 3, 0, 0, 0, 0]
            self.puzzle[8] = [0, 1, 9, 0, 0, 0, 0, 0, 0]

        if level == 5:
            self.puzzle[0] = [8, 0, 0, 0, 0, 0, 0, 0, 0]
            self.puzzle[1] = [0, 0, 3, 6, 0, 0, 0, 0, 0]
            self.puzzle[2] = [0, 7, 0, 0, 9, 0, 2, 0, 0]
            self.puzzle[3] = [0, 5, 0, 0, 0, 7, 0, 0, 0]
            self.puzzle[4] = [0, 0, 0, 0, 4, 5, 7, 0, 0]
            self.puzzle[5] = [0, 0, 0, 1, 0, 0, 0, 3, 0]
            self.puzzle[6] = [0, 0, 1, 0, 0, 0, 0, 6, 8]
            self.puzzle[7] = [0, 0, 8, 5, 0, 0, 0, 1, 0]
            self.puzzle[8] = [0, 9, 0, 0, 0, 0, 4, 0, 0]

    def execute(self, inference, var_sel):
        sudoku = Sudoku(self.puzzle)
        self.start = timer()
        a = backtracking_search(sudoku,
                                select_unassigned_variable=var_sel,
                                order_domain_values=unordered_domain_values,
                                inference=inference)
        self.end = timer()
        if a:
            print("Solution found")
        else:
            print("Solution not found! Check the entered puzzle for errors")
        self.bt = sudoku.bt_count

    def display(self):
        time = round(self.end - self.start, 5)
        print("Time: " + str(time) + " seconds")
        print("Num of Back Tracks: " + str(self.bt))

