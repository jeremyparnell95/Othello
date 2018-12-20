#Jeremy Parnell 27005248
#othello_gui

import tkinter
import othello_class

Font = ('Arial', 20)

class Start:
    def __init__(self):
        self._start = tkinter.Tk()
        choices = ['4','6','8','10','12','14','16']
        
        rules = tkinter.Label(master = self._start, text = "Othello FULL Game",font = ('Times New Roman', 34))
        rules.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)

        columns = tkinter.Label(master = self._start, text = 'COLUMNS:',font = Font)
        columns.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._columns_entry = tkinter.StringVar(self._start)
        self._columns_entry.set('4')
        self._board_columns = tkinter.OptionMenu(self._start, self._columns_entry, *choices)
        self._board_columns.grid(row = 1, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
        
        rows = tkinter.Label(master = self._start, text = 'ROWS:',font = Font)
        rows.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        self._rows_entry = tkinter.StringVar(self._start)
        self._rows_entry.set('4')
        self._board_rows = tkinter.OptionMenu(self._start, self._rows_entry, *choices)
        self._board_rows.grid(row = 2, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        first_turn = tkinter.Label(master = self._start, text = 'FIRST TURN:',font = Font)
        first_turn.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        button_frame1 = tkinter.Frame(master = self._start)
        button_frame1.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._turn_entry = tkinter.StringVar(self._start)
        self._turn_entry.set("1")
        tkinter.Radiobutton(master = button_frame1, text = "B", variable = self._turn_entry, value = 1).grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame1, text = "W", variable = self._turn_entry, value = 2).grid(row = 0, column = 1, padx = 10)

        corner = tkinter.Label(master = self._start, text = 'CORNER:',font = Font)
        corner.grid(row = 4, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        button_frame2 = tkinter.Frame(master = self._start)
        button_frame2.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._corner_entry = tkinter.StringVar(self._start)
        self._corner_entry.set("1")
        tkinter.Radiobutton(master = button_frame2, text = "B", variable = self._corner_entry, value = 1).grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame2, text = "W", variable = self._corner_entry, value = 2).grid(row = 0, column = 1, padx = 10)
        
        won = tkinter.Label(master = self._start, text = 'HOW GAME IS WON:',font = Font)
        won.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        button_frame3 = tkinter.Frame(master = self._start)
        button_frame3.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        self._won_entry = tkinter.StringVar(self._start)
        self._won_entry.set(">")
        tkinter.Radiobutton(master = button_frame3, text = ">", variable = self._won_entry, value = ">").grid(row = 0, column = 0, padx = 10)
        tkinter.Radiobutton(master = button_frame3, text = "<", variable = self._won_entry, value = "<").grid(row = 0, column = 1, padx = 8)

        button_frame = tkinter.Frame(master = self._start)
        button_frame.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,sticky = tkinter.N)
        ok_button = tkinter.Button(master = button_frame, text = 'OK', font = Font, command = self._on_ok_button)
        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        cancel_button = tkinter.Button(master = button_frame, text = 'Cancel', font = Font, command = self._on_cancel_button)
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        
        self._ok_clicked = False
        self._columns = 0
        self._rows = 0
        self._turn = 0
        self._corner = 0
        self._won = '' 


    def run(self):
        self._start.mainloop()
        
    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_columns(self):
        return self._columns

    def get_rows(self):
        return self._rows

    def get_turn(self):
        return self._turn

    def get_forner(self):
        return self._corner

    def get_won(self):
        return self._won


    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._rows = int(self._rows_entry.get())
        self._columns = int(self._columns_entry.get())
        self._turn = self._turn_entry.get()
        self._corner = self._corner_entry.get()
        self._won = self._won_entry.get()
        othello = Interface(self._rows,self._columns,self._corner,self._turn,self._won)
        othello.new_game
        othello.run
        self._start.destroy()

    def _on_cancel_button(self) -> None:
        self._start.destroy()




class Interface:
    def __init__(self,rows,columns,corner,turn,won):
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

        self._root_window = tkinter.Tk()
        
        self._title = tkinter.Label(master = self._root_window, text = "OTHELLO",font = ('Times New Roman', 42))
        self._title.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)
        self._display = tkinter.Label(master = self._root_window, text = "TURN: " + self._turn,font = ('Times New Roman', 28))
        self._display.grid(row = 1, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)

        self._black = tkinter.Label(master = self._root_window, text = "BLACK: 2",font = ('Times New Roman', 26))
        self._black.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.W)
        self._white = tkinter.Label(master = self._root_window, text = "WHITE: 2",font = ('Times New Roman', 26))
        self._white.grid(row = 1, column = 0, padx = 0, pady = 0, sticky = tkinter.E)

        self._canvas = tkinter.Canvas(master = self._root_window, width = 700, height = 700, background = 'dark green')
        self._canvas.grid(row = 2, column = 0, padx = 0, pady = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._canvas.bind('<Configure>', self.redraw_board)
        self._canvas.bind('<Button-1>', self._on_clicked)
        
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        

    def _on_clicked(self, event: tkinter.Event):
        self._is_clicked = True
        turn = self._othello._turn
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        count = self._othello.gamestate_check()
        winner = -1

        x = int((event.y/height)*self._rows)
        y = int((event.x/width)*self._columns)

        if self._othello.get_valid_moves(y,x,turn) == 0:
            self.place_tile()
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
                end = GameOver(winner)
                end.run()
    
            elif count == 0:
                self._othello.change_turn()
                if "BLACK" in self._display['text']:
                    self._display['text'] = "Turn: WHITE"
                elif "WHITE" in self._display['text']:
                    self._display['text'] = "Turn: BLACK"
                
                    
                
            
                
    def redraw_board(self, event: tkinter.Event):
        self.game_board()
        self.place_tile()
        

    def game_board(self):
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


    def place_tile(self):
        self._canvas.delete('tile')
        spot_width = int(self._canvas.winfo_width()/self._columns)
        spot_height = int(self._canvas.winfo_height()/self._rows)

        board = self._othello.board()
        for x in range(0,self._columns):
            for y in range(0,self._rows):
                if board[x][y] == 0:
                    pass
                elif board[x][y] == 1:
                    self._canvas.create_oval(spot_width*x, spot_height*y, spot_width * x+spot_width, spot_height * y+spot_height, fill = 'black', tag = 'tile')
                elif board[x][y] == 2:
                    self._canvas.create_oval(spot_width*x, spot_height*y, spot_width * x+spot_width, spot_height * y+spot_height, fill = 'white', tag = 'tile')

    def new_game(self):
        self._root_window.destroy()
                       
    def run(self):
        self._root_window.mainloop()


class GameOver:
    def __init__(self,winner):
        if winner == 1:
            self._winner = "BLACK"
        elif winner == 2:
            self._winner = "WHITE"
        else:
            self._winner = "NO"
            
        self._root_window = tkinter.Tk()

        self._end = tkinter.Label(master = self._root_window, text = "GAME OVER",font = ('Times New Roman', 42))
        self._end.grid(row = 0, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)
        self._winner = tkinter.Label(master = self._root_window, text = "{} PLAYER WON!".format(self._winner),font = ('Times New Roman', 36))
        self._winner.grid(row = 1, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)
        self._choice = tkinter.Label(master = self._root_window, text = "Play Again?",font = ('Times New Roman', 32))
        self._choice.grid(row = 2, column = 0, columnspan = 2, padx = 0, pady = 0, sticky = tkinter.N)

        button_frame = tkinter.Frame(master = self._root_window)
        button_frame.grid(row = 3, column = 0, columnspan = 3, padx = 10, pady = 10,sticky = tkinter.N)
        yes_button = tkinter.Button(master = button_frame, text = 'Yes', font = Font, command = self._on_yes_button)
        yes_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        no_button = tkinter.Button(master = button_frame, text = 'No', font = Font, command = self._on_no_button)
        no_button.grid(row = 0, column = 1, padx = 10, pady = 10)

    def _on_yes_button(self):
        Start().run()
        self._root_window.destroy()
               
    def _on_no_button(self):
        self._root_window.destroy()
        
    def run(self):
        self._root_window.mainloop()


               
if __name__ == '__main__':
    Start().run()
