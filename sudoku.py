from csp import *


class Sudoku(CSP):
    def __init__(self, puzzle):
        self.domains = {}
        self.neighbors = {}
        for row in range(9):
            for col in range(9):
                var = str(row) + "," + str(col)
                self.add_neighbor(var)
                if puzzle[row][col] != 0:
                    self.domains.update({var: str(puzzle[row][col])})
                else:
                    self.domains.update({var: '123456789'})

        CSP.__init__(self, None, self.domains, self.neighbors, different_values_constraint)

    # var[0] indicates the row and var[2] the column number. Example: var="1,2" => var[0]='1' var[1]=',' var[2]='2'
    def add_neighbor(self, var):
        elements = set()
        elements.update(self.get_row_elements(var))
        elements.update(self.get_col_elements(var))
        elements.update(self.get_box_elements(var))
        self.neighbors.update({var: {x for x in elements if x != var}})

    def get_row_elements(self, var):
        return {(var[0] + ',' + str(col)) for col in range(9)}

    def get_col_elements(self, var):
        return {(str(row) + ',' + var[2]) for row in range(9)}

    def get_box_elements(self, var):
        row = int(var[0])
        col = int(var[2])
        if row < 3:
            if col < 3:
                return self.helper(0, 0)
            elif col < 6:
                return self.helper(0, 3)
            else:
                return self.helper(0, 6)
        elif row < 6:
            if col < 3:
                return self.helper(3, 0)
            elif col < 6:
                return self.helper(3, 3)
            else:
                return self.helper(3, 6)
        else:
            if col < 3:
                return self.helper(6, 0)
            elif col < 6:
                return self.helper(6, 3)
            else:
                return self.helper(6, 6)

    def helper(self, start_row, start_col):
        box_elements = set()
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                box_elements.add(str(i) + ',' + str(j))
        return box_elements


