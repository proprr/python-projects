import sys

board = [["#", '#', '#'], ["#", '#', '#'], ["#", '#', '#']]

p1Won = False
p2Won = False

for row in board: print(row)

def boardSet():
    for row in board: print(row)

def p1Turn():
    column = int(input("What column? "))
    row = int(input("What row? "))
    board[column-1][row-1] = '1'
    boardSet()
    winner()

def p2Turn():
    column = int(input("What column? "))
    row = int(input("What row? "))
    board[column-1][row-1] = '2'
    boardSet()
    winner()

def winner():
    if board[0][0] == '1' and board[0][1] == '1' and board[0][2] == '1' or board[1][0] == '1' and board[1][1] == '1' and board[1][2] == '1' or board[2][0] == '1' and board[2][1] == '1' and board[2][2] == '1':
        print("Player 1 Wins")
        sys.exit()
    if board[0][0] == '1' and board[1][0] == '1' and board[2][0] == '1' or board[0][1] == '1' and board[1][1] == '1' and board[2][1] == '1' or board[0][2] == '1' and board[1][2] == '1' and board[2][2] == '1':
        print("Player 1 Wins")
        sys.exit()
    if board[0][0] == '1' and board[1][1] == '1' and board[2][2] == '1' or board[0][2] == '1' and board[1][1] == '1' and board[2][0] == '1':
        print("Player 1 Wins")
        sys.exit()
    
    if board[0][0] == '2' and board[0][1] == '2' and board[0][2] == '2' or board[1][0] == '2' and board[1][1] == '2' and board[1][2] == '2' or board[2][0] == '2' and board[2][1] == '2' and board[2][2] == '2':
        print("Player 2 Wins")
        sys.exit()
    if board[0][0] == '2' and board[1][0] == '2' and board[2][0] == '2' or board[0][1] == '2' and board[1][1] == '2' and board[2][1] == '2' or board[0][2] == '2' and board[1][2] == '2' and board[2][2] == '2':
        print("Player 2 Wins")
        sys.exit()
    if board[0][0] == '2' and board[1][1] == '2' and board[2][2] == '2' or board[0][2] == '2' and board[1][1] == '2' and board[2][0] == '2':
        print("Player 2 Wins")
        sys.exit()

while p1Won == False or p2Won == False:
    p1Turn()
    p2Turn()