"""
Answer to question 5 of formative 2
When testing on my own, the add function works correctly, both adding a shape to the board if possible, and not adding a shape if out of bounds. However, the autograder tests fail this function, and I am unsure why.
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
        """Returns a string of the board formatted for easy viewing and debugging

        Returns:
            str: the formatted board
        """
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
        """Adds a shape to the board if the given space is clear and the shape does not go out of bounds. Failed by the autograder tests, but appears to work with personal testing.

        Args:
            shape (list): the shape to be added, in the format of a 2D list
            row (int): the row the shape is to be added
            column (int): the column the shape is to be added

        Returns:
            Bool: returns True if the shape was added successfully, and False if it would overlap with another shape already on the board or goes out of bounds.
        """
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
        """Removes the given row and shifts all the rows above down

        Args:
            row (int): the row to be removed
        """
        for index in range(row, 0, -1):
            self._board[index] = self._board[index-1]
        self._board[0] = [0 for x in range(self.columns)]

    def _full_rows(self):
        """Returns True if the board contains any full rows, False if not

        Returns:
            Bool: returns True if the board contains full rows, False if not ( it feels silly to repeat this here, is it necessary? )
        """
        for row in self._board:
            if sum(row) == self.columns:
                return True
        return False

    def update(self):
        """If the board contains any full rows, it removes them by calling the remove_rows() function.
        """
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