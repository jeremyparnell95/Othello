#Jeremy Parnell 27005248
#othello_gui

import tkinter
import othello_class

Font = ('Arial', 20)

class Start:
    def __init__(self):
        '''
        this class creates the dialog box to set the rules and make the Othello gameboard
        '''
        
        self._start = tkinter.Tk()
        _choices = ['4','6','8','10','12','14','16']

        #the following code sets up the different rows and inputs for the dialog box
        _rules = tkinter.Label(master = self._start, text = "Othello FULL Game",font = ('Times New Roman', 34))
        _rules.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)

        _columns = tkinter.Label(master = self._start, text = 'COLUMNS:',font = Font)
        _columns.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._columns_entry = tkinter.StringVar(self._start)
        self._columns_entry.set('4')
        self._board_columns = tkinter.OptionMenu(self._start, self._columns_entry, *_choices)
        self._board_columns.grid(row = 1, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
        
        _rows = tkinter.Label(master = self._start, text = 'ROWS:',font = Font)
        _rows.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        self._rows_entry = tkinter.StringVar(self._start)
        self._rows_entry.set('4')
        self._board_rows = tkinter.OptionMenu(self._start, self._rows_entry, *_choices)
        self._board_rows.grid(row = 2, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        _first_turn = tkinter.Label(master = self._start, text = 'FIRST TURN:',font = Font)
        _first_turn.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        button_frame1 = tkinter.Frame(master = self._start)
        button_frame1.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._turn_entry = tkinter.StringVar(self._start)
        self._turn_entry.set("1")
        tkinter.Radiobutton(master = button_frame1, text = "B", variable = self._turn_entry, value = 1).grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame1, text = "W", variable = self._turn_entry, value = 2).grid(row = 0, column = 1, padx = 10)

        _corner = tkinter.Label(master = self._start, text = 'CORNER:',font = Font)
        _corner.grid(row = 4, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        button_frame2 = tkinter.Frame(master = self._start)
        button_frame2.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._corner_entry = tkinter.StringVar(self._start)
        self._corner_entry.set("1")
        tkinter.Radiobutton(master = button_frame2, text = "B", variable = self._corner_entry, value = 1).grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame2, text = "W", variable = self._corner_entry, value = 2).grid(row = 0, column = 1, padx = 10)
        
        _won = tkinter.Label(master = self._start, text = 'HOW GAME IS WON:',font = Font)
        _won.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        button_frame3 = tkinter.Frame(master = self._start)
        button_frame3.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._won_entry = tkinter.StringVar(self._start)
        self._won_entry.set(">")
        tkinter.Radiobutton(master = button_frame3, text = ">", variable = self._won_entry, value = ">").grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame3, text = "<", variable = self._won_entry, value = "<").grid(row = 0, column = 1, padx = 8)

        #setting up Ok or Cancel buttons located at the end of the dialog box
        button_frame = tkinter.Frame(master = self._start)
        button_frame.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,sticky = tkinter.N)
        _ok_button = tkinter.Button(master = button_frame, text = 'OK', font = Font, command = self._on_ok_button)
        _ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        _cancel_button = tkinter.Button(master = button_frame, text = 'Cancel', font = Font, command = self._on_cancel_button)
        _cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        #initializing variables
        self._ok_clicked = False
        self._columns = 0
        self._rows = 0
        self._turn = 0
        self._corner = 0
        self._won = '' 


    def _run(self):
        #runs the mainloop
        self._start.mainloop()
        
    def _was_ok_clicked(self):
        #checks to see if the mouse was clicked
        return self._ok_clicked

    def _get_columns(self):
        #returns the number of columns the user species to have on the gameboard
        return self._columns

    def _get_rows(self):
        #returns the number of rows the user species to have on the gameboard
        return self._rows

    def _get_turn(self):
        #returns the number corresponding to the current players turn
        return self._turn

    def _get_corner(self):
        #returns the color tile located at the top left of the beggining-four tiles
        return self._corner

    def _get_won(self):
        #returns the number corresponding to the player who won
        return self._won


    def _on_ok_button(self):
        #handles what happens when the OK button is pressed at the end of the dialog box
        self._ok_clicked = True
        self._rows = int(self._rows_entry.get())
        self._columns = int(self._columns_entry.get())
        self._turn = self._turn_entry.get()
        self._corner = self._corner_entry.get()
        self._won = self._won_entry.get()
        othello = Interface(self._rows,self._columns,self._corner,self._turn,self._won)
        othello._run
        self._start.destroy()

    def _on_cancel_button(self):
        #handles what happens when the Cancel button is pressed at the end of the dialog box
        self._start.destroy()




class Interface:
    def __init__(self,rows,columns,corner,turn,won):
        '''
        this function creates the gameboard and handles the Graphical User Interphase and all the
        actions made on it by the user
        '''
        
        #intializing variables. grabbing values from another module
        self._othello = othello_class.Othello(rows,columns,corner,turn,won)
        self._rows = rows
        self._columns = columns
        self._corner = corner
        if self._othello.turn() == 1:
            self._turn = "BLACK"
        else:
            self._turn = "WHITE"
        self._won = won
        self._is_clicked = False
        self._othello.new_board()

        #setting up the window
        self._root_window = tkinter.Tk()

        #sets up and configures the board while compensating for any resizing done to it and any of the spots on it
        self._title = tkinter.Label(master = self._root_window, text = "OTHELLO",font = ('Times New Roman', 42))
        self._title.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)
        self._display = tkinter.Label(master = self._root_window, text = "TURN: " + self._turn, font = ('Times New Roman', 28))
        self._display.grid(row = 1, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)

        self._black = tkinter.Label(master = self._root_window, text = "BLACK: 2",font = ('Times New Roman', 26))
        self._black.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.W)
        self._white = tkinter.Label(master = self._root_window, text = "WHITE: 2",font = ('Times New Roman', 26))
        self._white.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.E)

        self._canvas = tkinter.Canvas(master = self._root_window, width = 700, height = 700, background = 'dark green')
        self._canvas.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._canvas.bind('<Configure>', self._redraw_board)
        self._canvas.bind('<Button-1>', self._on_clicked)

        #column and row configurations. made it so the name 'OTHELLO' is always showing
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        
    def _on_clicked(self, event: tkinter.Event):
        '''
        handles the event the user clicks on a spot on the GUI in order to make a move.
        catches any invalid move errors as well ends the game declaring the winner at the end
        based off the rules the user specifies at the beginning of the game
        '''
        
        self._is_clicked = True
        turn = self._othello._turn
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        count = self._othello.gamestate_check()
        winner = -1

        x = int((event.y/height)*self._rows)
        y = int((event.x/width)*self._columns)

        if self._othello.get_moves(y,x,turn) == 0:
            self._place_tile()
            count = self._othello.gamestate_check()
            discs = self._othello.disc_count()
            self._black_discs = discs[0]
            self._white_discs = discs[1]
            
            self._black['text'] = "BLACK: " + str(self._black_discs)
            self._white['text'] = "WHITE: " + str(self._white_discs)
            
            if count == 2:
                winner = self._othello.game_won()
                if winner == 1:
                    self._display['text'] = 'WINNER: BLACK'
                elif winner == 2:
                    self._display['text'] = "WINNER: WHITE"
                else:
                    self._display['text'] = "WINNER: NONE"
                self._canvas.unbind('<Button-1>')
    
            elif count == 0:
                self._othello.change_turn()
                if "BLACK" in self._display['text']:
                    self._display['text'] = "Turn: WHITE"
                elif "WHITE" in self._display['text']:
                    self._display['text'] = "Turn: BLACK"

                               
    def _redraw_board(self, event: tkinter.Event):
        '''
        re/draws the board depending if any actions have been made on the board by the user
        ex. resizing, new piece, tile-flips
        '''
        self._game_board()
        self._place_tile()

        
    def _game_board(self):
        '''
        this function takes the dimensions of the board and draws a grid of cells within it to use for the gameboard
        '''
        self._canvas.delete('spot')
        spot_width = int(self._canvas.winfo_width()/self._columns)
        spot_height = int(self._canvas.winfo_height()/self._rows)
        for column in range(self._columns):
            for row in range(self._rows):
                x1 = column*spot_width
                y1 = row * spot_height
                x2 = x1 + spot_width
                y2 = y1 + spot_height
                spot = self._canvas.create_rectangle(x1,y1,x2,y2, tags = "spot")

                
    def _place_tile(self):
        '''
        this function redraws all the tiles on the board in the event of a new tile, any flips, or
        resizing of the campus
        '''
        self._canvas.delete('tile')
        spot_width = int(self._canvas.winfo_width()/self._columns)
        spot_height = int(self._canvas.winfo_height()/self._rows)

        board = self._othello.board()       #placing the colored tiles
        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if board[x][y] == 0:
                    pass
                elif board[x][y] == 1:
                    self._canvas.create_oval(spot_width*x, spot_height*y, spot_width * x+spot_width, spot_height * y+spot_height, fill = 'black', tag = 'tile')
                elif board[x][y] == 2:
                    self._canvas.create_oval(spot_width*x, spot_height*y, spot_width * x+spot_width, spot_height * y+spot_height, fill = 'white', tag = 'tile')

                    
    def _run(self):
        #runs the mainloop of the interface
        self._root_window.mainloop()

        
if __name__ == '__main__':
    Start()._run()

