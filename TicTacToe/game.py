from player import RandomComputerPlayer, HumanPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in[self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # indexes 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')

        
    def available_moves(self):
    # ['x','x','o'] -> [(0,'x'),(1,x),(2,o)] etc
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid then move -> true, else false
        # print("square ",square, "self board", self.board, type(self.board[0]), type(" "), type(square))
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner (self, square, letter):
        # win if 3 in row or in column or in diagonal
        # row
        row_ind = square//3
        row = self.board[row_ind*3: (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True
        
        # column
        col_ind = square %3
        column = [self.board[col_ind+i*3] for i in range (3)]
        if all([spot == letter for spot in column]):
            return True
        
        # diagonals [0,2,4,6,8] spots square

        if square %2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # first diagonal, left to right
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]] # second diagonal right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game = True):
    # returns a winner or None for a tie
    if print_game:
        game.print_board_nums()

    letter = "X"  # starting letter 
    while game.empty_squares():
        # get move from X or O player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + f" makes move to square {square}")
                game.print_board()
                print("")
            
            if game.current_winner:
                if print_game:
                    print(letter + " win !")
                return letter
            # flipping players 
            letter = "O" if letter == "X" else "X" 
        
        # small break after each step
        time.sleep(0.8)

    if print_game:
        print("It\'s a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t,x_player,o_player, print_game = True)

        

