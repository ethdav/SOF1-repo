
class GameBoard(object):
    
    EMPTY = '.'
    PLAYER1 = 'X'
    PLAYER2 = 'O'
    
    ROWS = 6
    COLUMNS = 7
    
    def __init__(self):
        """
            Build an empty game board of 7 columns and 6 rows.
            A board is represented by a 2D array of char. the first index represent the column of the game
            and the second index represent the rows, where row = 0 represents the bottom of the column.
            for example:
            - board[0][0] is the bottom left of the board,
            - board[6][0] is the bottom right of the board, i.e. the bottom of the last column in the game
            - board[1][5] is the top place in the second column, i.e if it is occupied by a player's disk, 
              the second row is full and we cannot add another disk there.     
        """
        self._board = [[GameBoard.EMPTY]*self.ROWS for i in range(self.COLUMNS)]
        self
        
        
    def get_board(self):
        return self._board
        
    def get_valid_moves(self):
        """
        Method returning a list of valid moves (i.e. a list of integer). If there are no more moves available, 
        meaning the board is full, the method should return an empty list.
        
        @return a list of Integer representing the remaining moves available to players, an empty list if no more
        moves are available.
        
        """
        pass
                     
            
        
    
class Player(object):
    
     
    def __init__(self, gameboard,playerid):
        """
        @param gameboard the GameBoard for the game to be played by the player.
        @param playerid must be one of the two character GameBoard.PLAYER1 or GameBoard.PLAYER2
        """
        self._game = gameboard
        self._id = playerid
        
    def id(self):
        return self._id
    
    def make_move(self):
        """
        The method select a valid move to be made and return the move as an int.
        
        @return the next move from the player as an int representing in which column the next
        disk should be inserted.
        
        @throws Exception if there is no valid move left (i.e. the board is full).     
        """
        pass
 
 
 
 
################################# TESTS ############################   
def set_board_for_tests(moves, board):
    """
    Convenience method provided for setting up your board before testing. An example on how it is used
    is shown in the main method. Player1 always do the first move, then player2, then player1 and so on
    until the series of moves given in the list is exhausted.
    
    @param moves a list of int representing the series of moves to be done by the players
    @param board the GameBoard object where the moves should be done.
    @return the board after the moves have been made.
    
    """                             
    player = GameBoard.PLAYER1
    for move in moves:
        # BE CAREFUL, THE LINE BELOW WILL NOT WORK UNTIL YOU IMPLEMENT get_move(move, player)
        # IN THE CLASS GameBoard
        board.get_move(move, player); 
        
        if(player == GameBoard.PLAYER1):
            player = GameBoard.PLAYER2
        else:
            player = GameBoard.PLAYER1

    return board;


################### A basic test setting###################
board = GameBoard();
 
# list of move needed for setting up my board before testing.
# you must define the list you need for your specific test.
moves = [0,0,1,5,6,6,2,1]; 
 
# Setting the board before testing
board = GameBoard.set_board_for_tests(moves, board);
 
# My actual test. 
# Here I am testing the __srt__() method to check it is doing what I expect
print(board);


