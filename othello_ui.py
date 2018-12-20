#Jeremy Parnell 27005248
#othello_ui

import othello_class

def _board_rows():
    '''
    prompts the user for the number of rows on the board
    '''
    rows = int(input())
    return rows



def _board_columns():
    '''
    prompts the user for the number of columns on the board
    '''
    columns = int(input())
    return columns
        

        
def _first_turn():
    '''
    prompts the user for the player whose turn will go first in the game
    '''
    first = input()
    if first.strip().upper() == 'B':
        return 1
    elif first.strip().upper() == 'W':
        return 2
    
    
    

def _first_location():
    '''
    prompts the user for the player who will have the top left and bottom
    right corner for the starting 4 middle tiles
    '''
    corner = input()
    if corner.strip().upper() == 'B':
        return 1
    elif corner.strip().upper() == 'W':
        return 2
    return corner

           
   
def _won():
    '''
    prompts the user for the rule to win the game
    '''
    game_is_won = input()
    return game_is_won
    


def _get_space():
    '''
    during their turn, this function prompts the player for a spot on
    the board to place their tile
    '''
    while True:
        try:
            space = input()
            if len(space.split()) == 2:
                return space
            else:
                print("INVALID")
                pass 
        except:
            print("INVALID")
            pass


def _print_turn():
    '''
    this function prints out the current player's turn
    '''
    if othello.turn() == 1:
        turn = "B"
    if othello.turn() == 2:
        turn = "W"
    print("TURN: {}".format(turn))


def _print_count():
    '''
    this function prints out the current tile count on the board
    for both players
    '''
    count = othello.disc_count()
    black = count[0]
    white = count[1]
    print("B: {}  W: {}".format(black,white))


def _print_board(rows,columns):
    '''
    this function prints the board
    '''
    board = othello.board()
    for x in range(0,columns):
        content = ''
        for y in range(0,rows):
            if board[y][x] == 0:
                content += "." + "  "
            elif board[y][x] == 1:
                content += "B" + "  "
            elif board[y][x] == 2:
                content += "W" + "  "
        print(content)
        


def _print_winner():
    '''
    this function prints out the winning player
    '''
    winner = othello.game_won()
    if winner == 1:
        print("WINNER: B")
    elif winner == 2:
        print("WINNER: W")
    elif winner == 0:
        print("WINNER: NONE")


def _move(board_rows,board_columns):
    '''
    this function carries out the move of each player. it takes care of user
    input as well as the necessary tile flips. if the move made is invalid,
    it will prompt the player to make a new move
    '''
    while True:
        try:
            player_move = _get_space()
            input_row = int(player_move.split()[0])
            input_column = int(player_move.split()[1])

            othello.move(input_row,input_column)
            othello.vertical(input_row,input_column)
            othello.horizontal(input_row,input_column)
            othello.forward_diagonal(input_row,input_column)
            othello.backward_diagonal(input_row,input_column)
            if othello.invalid_move_check(input_row,input_column) == -1:
                raise othello_class.InvalidMoveError()
            print("VALID")
        except:
            print("INVALID")
            continue
        break

def _runs_ui(rows,columns):
    '''
    this function handles the UI portion of the program. printing out all
    the visuales and keeping track of the gamestate.5 prompting for player moves
    and finishing the game when there are no more moves to be made
    '''
    othello.change_turn()
    while True:
        _print_count()
        _print_board(rows,columns)
        count = othello.gamestate_check()
        if count == 0:
            othello.change_turn()
        if count >= 2:
            break
        if count < 2:
            _print_turn()
            _move(rows,columns) 

if __name__ == "__main__":
    print("FULL")
    rows = _board_rows()
    columns = _board_columns()
    turn = _first_turn()
    corner = _first_location()
    win = _won()
    othello = othello_class.Othello(rows,columns,corner,turn,win)
    othello.new_board()
    _runs_ui(rows,columns)
    _print_winner()
   
   
    




        
            
        
        
    
    
    
    

