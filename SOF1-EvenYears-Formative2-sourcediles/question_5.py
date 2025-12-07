"""
Answer to question 5 of formative 2
"""
import copy

class Blotris:
    def __init__(self, rows, columns):
        if rows < 5 or columns < 5:
            raise ValueError("Rows and columns must be greater than or equal to 5")
        self.rows = rows
        self.columns = columns
        self._board = [[0 for x in range(columns)] for x in range(rows)]

    def __str__(self):
        output = ""
        for row in self._board:
            for column in row:
                if column == 0:
                    output += "[ ]"
                elif column == 1:
                    output += "[#]"
            output += "\n"
        return output

    def add(self, shape, row, column):
        old_board = copy.deepcopy(self._board)
        try:
            for s_row in range(len(shape)):
                for s_col in range(len(shape[s_row])):
                    if shape[s_row][s_col] == 1:
                        if (self._board[row+s_row][column+s_col] + shape[s_row][s_col]) > 1:
                            self._board = old_board
                            return False
                        self._board[row+s_row][column+s_col] = 1
            self.update()
            return True
        except IndexError:
            self._board = old_board
            return False
        
    def remove_row(self, row):
        for index in range(row, 0, -1):
            self._board[index] = self._board[index-1]
        self._board[0] = [0 for x in range(self.columns)]

    def _full_rows(self):
        for row in self._board:
            if sum(row) == self.columns:
                return True
        return False

    def update(self):
        while self._full_rows() is True:
            for row in range(len(self._board)):
                if sum(self._board[row]) == self.columns:
                    self.remove_row(row)
                               
def main():
    blotris = Blotris(8,5)
    shape1 = [[0,1,1,1,1]]
    shape2 = [[1],[1],[1],[1]]
    shape3 = [[0,1,1],[1,1,0]]
    blotris.add(shape1, 7, 0)
    blotris.add(shape3, 5, 1)
    print(blotris)
    blotris.add(shape2, 4, 0)
    print(blotris)
    
if __name__ == "__main__":
    main()