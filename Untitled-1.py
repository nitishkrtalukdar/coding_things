import numpy as np

from time import sleep

def create_board():
    return(np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]))

def possibilities(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                l.append((i,j))
    return(l)


def player_input(board,player):
    selection=possibilities(board)
    row,col=input("Player {player}: Enter your move:")
    row=int(row)
    col=int(col)
    board[row][col]=player
    return(board)

def row_win(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[x,y]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)

def col_win(board,player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
            if board[y,x]!=player:
                win=False
                continue
        if win==True:
            return(win)
    return(win)

def dig_win(board,player):
   win=True
   y=0

   #first diagonal
   for x in range(len(board)):
    if board[x,x]!=player:
        win=False
   if win:
    return win

   #second diagonal
   win=True
   if win:
    for x in range(len(board)):
        y=len(board)-1-x
        if board[x,y]!=player:
            win=False
   return win 

def evaluate(board):
    winner=0
    for player in[1,2]:
        if(row_win(board,player)or col_win(board,player)or dig_win(board,player)):
            winner=player
    if np.all(board!=0)and winner==0:
        winner=-1
    return winner



#driver function
def play_game():
   
    board=create_board()
    winner=0
    counter=1
    print(board)
    sleep(2)

    while winner==0:
        for player in[1,2]:
            board=player_input(board,player)
            print("board after"+str(counter)+"move")
            print(board)
            sleep(2)
            counter+=1
            winner=evaluate(board)
            if winner!=0:
                break
    return(winner)

print("Winner is:"+str(play_game()))

