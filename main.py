# board
# displaying
# start game - > play game
# handle turn
# checking results, who win
    # check rows
    # check columns
    # check diagonals
# checking tie
# flip player

# displaying a board
def display_board(board):
    for i in range(0,len(board),3):
        print('|'.join(board[i:i+3]))

#handle a turn
def handle_turn(board, current_player):
    
    print(current_player, "'s turn")
    position = input("Choose a position from 1-9: ")
    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position)-1
        if board[position]=='-':
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = current_player
    display_board(board)

#checking results, if over
def check_if_over(board, winner):
    global game_going
    winner = check_for_winner(board, winner)
    check_if_tie(board)
    return winner

def check_for_winner(board, winner):
    # check rows
    # check columns 
    # check diagonals
    row_winner = check_rows(board, winner)
    column_winner = check_colums(board, winner)
    diagonal_winner = check_diagonals(board, winner)

    return row_winner or column_winner or diagonal_winner

def check_rows(board, winner):
    global game_going
    # return the winner
    for i in range(0,len(board),3):
        if all(element == board[i] and element!='-' for element in board[i:i+3]):
            winner = board[i]
            game_going = False
    return winner

def check_colums(board, winner):
    global game_going
    for i in range(0,3):
        if all(element == board[i] and element!='-' for element in board[i:i+7:3]):
            winner = board[i]
            game_going = False
    return winner


def check_diagonals(board, winner):
    global game_going
    if all(element == board[0] and element!='-' for element in board[0:9:4]):
        winner = board[0]
        game_going = False
    elif all(element == board[2] and element!='-' for element in board[2:7:2]):
        winner = board[2]
        game_going = False
    return winner

def check_if_tie(board):
    global game_going
    if '-' not in board:
        game_going = False
        

# flip player
def flip_player(current_player):
    if current_player == 'X':
        current_player = "O"
    else:
        current_player = "X"
    return current_player

# play the game tic tac toe
def play_game(board, winner, current_player):

    # display intial board
    display_board(board)

    # while the game is going 
    while game_going:

        # handle a one turn of a current player
        handle_turn(board, current_player)

        # check if game ended
        winner = check_if_over(board, winner)

        # flip to the other player
        current_player = flip_player(current_player)
    
    # the game has ended
    if winner:
        print("Winner is ", winner)
    else:
        print("Tie")

# board
board = ['-']*9
game_going = True
winner = None
current_player = "X"  
    
play_game(board, winner, current_player)


