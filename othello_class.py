#Jeremy Parnell 27005248
#othello_class

import copy

class InvalidMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class Othello:
    
    def __init__(self,rows,columns,corner,turn,won):
        '''
        initializes all the variables used within the class
        '''          
        self._rows = int(rows)
        self._columns = int(columns) 
        self._turn = int(turn)
        self._corner = int(corner)               
        self._won = won
        self._board = []
        self._copy_board = []
        self._game_check = 0


    def turn(self):
        '''
        returns which players turn it is
        '''
        return self._turn
    

    def board(self):
        '''
        returns the current state of the board
        '''
        self._copy_board = copy.deepcopy(self._board)
        return self._board


    def new_board(self) -> [[int]]:
        '''
        creates a starting Othello game with the four correct tiles in
        the middle
        '''
        for col in range(self._columns):
            self._board.append([])
            for row in range(self._rows):
                self._board[-1].append(0)

        if self._corner == 1:
            self._board[int(self._columns/2)-1][int(self._rows/2)-1] = 1
            self._board[(int(self._columns/2))][(int(self._rows/2))] = 1
            self._board[int(self._columns/2)][int(self._rows/2)-1] = 2
            self._board[int(self._columns/2)-1][int(self._rows/2)] = 2
                
        elif self._corner == 2:
            self._board[int(self._columns/2)-1][int(self._rows/2)-1] = 2
            self._board[(int(self._columns/2))][(int(self._rows/2))] = 2
            self._board[int(self._columns/2)][int(self._rows/2)-1] = 1
            self._board[int(self._columns/2)-1][int(self._rows/2)] = 1       


    def change_turn(self):
        '''
        changes the current players turn
        '''
        if self._turn == 1:
            self._turn = 2
        elif self._turn == 2:
            self._turn = 1

            
    def disc_count(self):
        '''
        counts the number of white and black tiles and returns both counts
        in a list
        '''
        self._black = 0
        self._white = 0
        for x in self._board:
            for y in x:
                if y == 1:
                    self._black += 1
                elif y == 2:
                    self._white += 1
        return [self._black,self._white]

   
    def game_won(self):
        '''
        returns the winner of the game or if there's a tie
        '''
        if self._black == self._white:
                return 0
        elif self._won == ">":
            if self._black > self._white:
                return 1
            elif self._black < self._white:
                return 2
        elif self._won == "<":
            if self._black > self._white:
                return 2
            elif self._black < self._white:
                return 1

           
    def gamestate_check(self):
        '''
        checks the current state of the game. if a player can make a move
        it will return 0, if a player is unable to make a move, it will return
        1. if both players are unable to make a move, it will return an integer
        larger than 1
        '''
        black_move_list = []
        white_move_list = []

        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if self._board[x][y] == 0:
                    test = self._get_valid_moves(x,y,1) 
                    if test == 0:
                            black_move_list.append((y+1,x+1))

        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if self._board[x][y] == 0:
                    test = self._get_valid_moves(x,y,2) 
                    if test == 0:
                            white_move_list.append((y+1,x+1))
                            
        if self._turn == 1 and len(white_move_list) == 0:
            self._game_check += 1
        elif self._turn == 2 and len(black_move_list) == 0:
            self._game_check += 1
        else:
            self._game_check = 0
            
        if len(white_move_list) == 0 and len(black_move_list) == 0:
            self._game_check = 2           

        return self._game_check

    
    def _get_valid_moves(self,row,column,turn):
        '''
        this function is given multiple row and column coordinates on the
        board and returns 0 if it is a valid move. if it is an invalid move,
        it will return -1
        '''
        check = -1
        check_board = copy.deepcopy(self._board) 
        self._board[row][column] = turn
        original_board = copy.deepcopy(self._board)
        self.vertical(column + 1, row + 1)
        self.horizontal(column + 1, row + 1)
        self.forward_diagonal(column + 1, row + 1)
        self.backward_diagonal(column + 1, row + 1)
        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if self._board[x][y] != original_board[x][y]:
                    check = 0
                    break              
        self._board = copy.deepcopy(check_board)
        return check

    
    def get_moves(self,row,column,turn):
        '''
        this function takes a single coordinate on the board and returns 0 if it is
        a valid move. if it is an invalid move, it will return -1
        '''
        check_board = copy.deepcopy(self._board) 
        self._board[row][column] = turn
        original_board = copy.deepcopy(self._board)
        self.vertical(column + 1, row + 1)
        self.horizontal(column + 1, row + 1)
        self.forward_diagonal(column + 1, row + 1)
        self.backward_diagonal(column + 1, row + 1)
        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if self._board[x][y] != original_board[x][y]:
                    return 0           
        self._board = copy.deepcopy(check_board)
        return -1

       
    def invalid_move_check(self,row,column):
        '''
        this function checks a players move. if it is valid, the function will
        return 0. if invalid, the function returns -1
        '''
        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if self._board[x][y] != self._copy_board[x][y]:
                    if y == row - 1 and x == column - 1:
                        pass
                    else:
                        return 0
                if x == self._columns - 1 and y == self._columns - 1:
                    self._board = copy.deepcopy(self._copy_board)
                    return -1
                else:
                    pass

    def move(self,row,column):
        '''
        takes a row and a column and if that point on the board is empty,
        it will add the current player's tile to that spot. else it will raise
        an invalid move error
        '''
        if self._user_row(row):
            if self._user_column(column):
                if self._board[column-1][row-1] == 0:
                    self._board[column-1][row-1] = self._turn
                else:
                    raise InvalidMoveError()
            else:
                raise InvalidMoveError()
        else:
            raise InvalidMoveError()


    def _user_row(self, row):
        '''
        checks to make sure the amount of rows inputed is not too much or
        too little. if it is, an error will be raised
        '''
        return 1 <= row <= self._rows


    def _user_column(self, column):
        '''
        checks to make sure the amount of columns inputed is not too much or
        too little. if it is, an error will be raised
        '''
        return 1 <= column <= self._columns

        
    def horizontal(self,row,column):
        '''
        this function takes a spot on the board given in the form of row
        and column, and flips the valid tiles below and above it
        '''
        horizontal_list = []
        horizontal = []
        reverse = []
        rev_list = []
        
        for hor in range(0,len(self._board)):
            horizontal_list.append(self._board[hor][row-1])
            
        j = 0
        for hor in horizontal_list:
            if int(hor) > 0:
                horizontal = list(horizontal_list[column-1:])
                reverse = list(horizontal_list[0:column])
                rev_list = list(reverse[::-1])
                break
            j += 1

                                           
        if len(horizontal) > 1 and horizontal[0] != horizontal[1] and horizontal[1] != 0:
            j = 0
            for dia in horizontal[1:]:
                j += 1
                if dia == horizontal[0]:
                    break
                if j == len(horizontal)-1:
                    j = 0
                    break
            for dia in range(len(horizontal[0:j])):
                horizontal[dia] = self._turn

                       
        if len(rev_list) > 1 and rev_list[0] != rev_list[1] and rev_list[1] != 0:
            j = 0
            for hor in rev_list[1:]:
                j += 1
                if hor == rev_list[0]:
                    break
                if j == len(rev_list)-1:
                    j = 0
                    break
            for hor in range(len(rev_list[0:j])):
                rev_list[hor] = self._turn


        hor_list = []
        if len(horizontal) == 1:
            hor_list = rev_list[::-1]
        elif len(reverse) == 1:
            hor_list = horizontal
        else:
            hor_list = rev_list[::-1] + horizontal[1:]

        for hor in range(0,len(hor_list)):
            self._board[hor][row-1] = hor_list[hor]



    def vertical(self,row,column):
        '''
        this function takes a spot on the board given in the form of row
        and column, and flips the valid tiles to the left and the right of it
        '''
        vertical = self._board[column-1][row-1:]
        rev = self._board[column-1][:row]
        rev_list = rev[::-1]
        reverse = []

        if len(vertical) > 1 and vertical[0] != vertical[1] and vertical[1] != 0:
            j = 0
            for vert in vertical[1:]:
                j += 1
                if vert == vertical[0]:
                    break
                if j == len(vertical)-1:
                    j = 0
                    break
            for vert in range(len(vertical[0:j])):
                vertical[vert] = self._turn
                        
        if len(rev_list) > 1 and rev_list[0] != rev_list[1] and rev_list[1] != 0:
            j = 0
            for vert in rev_list[1:]:
                j += 1
                if vert == rev_list[0]:
                    break
                if j == len(rev_list)-1:
                    j = 0
                    break
            for vert in range(len(rev_list[0:j])):
                rev_list[vert] = self._turn
                
        vertical_list = []
        if len(vertical) == 1:
            vertical_list = rev_list[::-1]
        elif len(rev) == 1:
            vertical_list = vertical
        else:
            vertical_list = rev_list[::-1] + vertical[1:]

           
        self._board[column-1] = vertical_list


       
    def forward_diagonal(self,row,column):
        '''
        this function takes a spot on the board given in the form of row
        and column, and flips the valid tiles in the right upper-half of the upward
        diagonal and the right lower-half of the downward diagonal
        '''
        diagonal_list_one = []
        diagonal_list_two = []
        rev_list = []
           
        j = 0
        for dia in range(0,self._columns):
            j += 1
            if column + dia == self._columns or row - dia == 1:
                break           
        for dia in range(0,j): 
            diagonal_list_one.append(self._board[column-1+dia][row-1-dia])

            
        i = 0
        for dia in range(0,self._rows):
            i += 1
            if column - dia == 1 or row + dia == self._rows:
                break
        for dia in range(0,i): 
            diagonal_list_two.append(self._board[column-1-dia][row-1+dia])


        if len(diagonal_list_one) > 1 and diagonal_list_one[0] != diagonal_list_one[1] and diagonal_list_one[1] != 0:
            k = 0
            for dia in diagonal_list_one[1:]:
                k += 1
                if dia == diagonal_list_one[0]:
                    break
                if k == len(diagonal_list_one)-1:
                    k = 0
                    break
            for dia in range(len(diagonal_list_one[0:k])):
                diagonal_list_one[dia] = self._turn


        if len(diagonal_list_two) > 1 and diagonal_list_two[0] != diagonal_list_two[1] and diagonal_list_two[1] != 0:
            k = 0
            for dia in diagonal_list_two[1:]:
                k += 1
                if dia == diagonal_list_two[0]:
                    break
                if k == len(diagonal_list_two)-1:
                    k = 0
                    break
            for dia in range(len(diagonal_list_two[0:k])):
                diagonal_list_two[dia] = self._turn               
        rev_list = diagonal_list_two[::-1]
        
                       
        d1_list = []
        if len(diagonal_list_one) == 1:
            d1_list = rev_list
        elif len(diagonal_list_two) == 1:
            d1_list = diagonal_list_one
        else:
            d1_list = rev_list + diagonal_list_one[1:]
            
            
        for dia in range(0,len(d1_list)):
            self._board[(column-(i-1))+dia-1][(row+(i-1))-dia-1] = d1_list[dia]


            
    def backward_diagonal(self,row,column):
        '''
        this function takes a spot on the board given in the form of row
        and column, and flips the valid tiles in the left lower-half of the upward
        diagonal and the left upper-half of the downward diagonal
        '''
        diagonal_list_one = []
        diagonal_list_two = []
        rev_list = []
    
        j = 0
        for dia in range(0,self._columns):
            j += 1
            if column + dia == self._columns or row + dia == self._rows:
                break
        for dia in range(0,j): 
            diagonal_list_one.append(self._board[column-1+dia][row-1+dia])


        i = 0
        for dia in range(0,self._rows):
            i += 1
            if column - dia == 1 or row - dia == 1:
                break
        for dia in range(0,i): 
            diagonal_list_two.append(self._board[column-1-dia][row-1-dia])


        if len(diagonal_list_one) > 1 and diagonal_list_one[0] != diagonal_list_one[1] and diagonal_list_one[1] != 0:
            k = 0
            for dia in diagonal_list_one[1:]:
                k += 1
                if dia == diagonal_list_one[0]:
                    break
                if k == len(diagonal_list_one)-1:
                    k = 0
                    break
            for dia in range(len(diagonal_list_one[0:k])):
                diagonal_list_one[dia] = self._turn


        if len(diagonal_list_two) > 1 and diagonal_list_two[0] != diagonal_list_two[1] and diagonal_list_two[1] != 0:
            k = 0
            for dia in diagonal_list_two[1:]:
                k += 1
                if dia == diagonal_list_two[0]:
                    break
                if k == len(diagonal_list_two)-1:
                    k = 0
                    break
            for dia in range(len(diagonal_list_two[0:k])):
                diagonal_list_two[dia] = self._turn               
        rev_list = diagonal_list_two[::-1]

                      
        d1_list = []
        if len(diagonal_list_one) == 1:
            d1_list = rev_list
        elif len(diagonal_list_two) == 1:
            d1_list = diagonal_list_one
        else:
            d1_list = rev_list + diagonal_list_one[1:]


        for dia in range(0,len(d1_list)):
            self._board[(column-(i-1))+dia-1][(row-(i-1))+dia-1] = d1_list[dia]

        

        
                
        
        
        
        

    


        
    
