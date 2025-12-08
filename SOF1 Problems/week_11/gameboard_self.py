
class GameBoard:

    def __init__(self, rows=6, columns=7):
        self._board = [[0 for x in range(columns)] for x in range(rows)]
        self.width = columns
        self.player1 = 1
        self.player2 = 2

    def __str__(self):
        output = ""
        for row in self._board:
            output += "+---+---+---+---+---+---+---+\n"
            for col in row:
                output += "| "
                if col == 0:
                    output += ". "
                elif col == 1:
                    output += "\033[92mx\033[00m "
                elif col == 2:
                    output += "\033[91mo\033[00m "
            output += "|\n"
        output += "+===+===+===+===+===+===+===+\n" + \
                "| 0 | 1 | 2 | 3 | 4 | 5 | 6 |\n" + \
                "+===+===+===+===+===+===+===+"
        return output
    
    def move(self, move, player):
        if player not in (1,2):
            raise ValueError("Player must be either 1 or 2")
        elif move > self.width or move < 0:
            raise ValueError("Invalid move")
        elif move not in self.get_valid_move():
            raise ValueError("Invalid move")
        
        for row in range(len(self._board)-1,-1,-1):
            if self._board[row][move] in (1,2):
                continue
            elif self._board[row][move] == 0:
                self._board[row][move] = player
                break

    def get_valid_move(self):
        valid = set()
        for col in range(self.width):
            if self._board[0][col] == 0:
                valid.add(col)
        return valid

    def iswinner(self):
        pass

def main():
    game = GameBoard()
    for x in range(6):
        game.move(0,2)
    print(game.get_valid_move())
    print(game)

if __name__ == "__main__":
    main()