from fltk import *
import time
import random
#Started on 4/29/2026
#Non-OOP version
#light green: 179, 214, 101
#dark green: 172, 208, 94
#Press light green: 197, 224, 137
#Press dark green: 192, 220, 131
#Dark Press: 210, 185, 157 
#Light Press: 223, 195, 163

def but_cb(wid, data):
    global board
    row, col = data
    for bomb in bombs:
        #at the start of the game if the user clicks on a bomb, change bomb to another location and update the board
        if (row, col) == bomb:
            wid.color(FL_RED)
            wid.redraw()
            print("Game Over")
            return
    

#make bombs
def bomb_maker():
    bombs = []
    while len(bombs)< 10:
        pos = (random.randint(0,9), random.randint(0,9))
        if pos not in bombs:
            bombs.append(pos)
    return bombs
    
win = Fl_Window(500, 500, "Minesweeper")  
win.begin()

#Making group for buttons to resize
g1 = Fl_Group(0, 0, 500, 500)
g1.begin()

firstClick = True
#make buttons with alternating colours with 2D list 
buttons = []
for row in range(10):
    button_row = []
    color = (row % 2 == 0)
    for col in range(10):
        if color:
            button = Fl_Button(col * 50, row * 50, 50, 50)
            button.box(FL_FLAT_BOX) 
            button.color(fl_rgb_color(179, 214, 101))
            color = False
        else:
            button = Fl_Button(col * 50, row * 50, 50, 50)
            button.box(FL_FLAT_BOX)
            button.color(fl_rgb_color(172, 208, 94))
            color = True
        button_row.append(button)
        button_row[-1].callback(but_cb,(row,col))
    buttons.append(button_row)

#make bombs  
bombs = bomb_maker()

#make 2d list for bomb as well as numbers
board = []
for row in range(10):
    board_row = []
    for col in range(10):
        board_row.append(0) #shows number of bombs around and if it is a bomb we will change it to string "bomb"
    board.append(board_row)

for bomb in bombs:
    board[bomb[0]][bomb[1]]= "bomb"

#marking board with numbers
for i in range(10):
    for j in range(10):
        if board[i][j] == "bomb":
            continue
        #corner edge cases
        if i == 0 and j == 0:
            if board[i][j+1] == "bomb":
                board[i][j] += 1
            if board[i+1][j] == "bomb":
                board[i][j] += 1
            if board[i+1][j+1] == "bomb":
                board[i][j] += 1


print(board)
g1.end()
win.end()
win.resizable(g1)
win.show()
Fl.run()