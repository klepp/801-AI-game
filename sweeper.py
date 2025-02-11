import random
#look into pygame for gui
# board the user cannot see
board = [[0,0,0,0,0,0,0,0,0,0], #0 = no bomb, 
        [0,0,0,0,0,0,0,0,0,0],  #1 = bomb
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],]
# board user can see
boardDisplay=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], #-1 is unknown
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        ]

TotalRows=len(boardDisplay)
TotalCols=len(boardDisplay[0])
numMines = 15

def checkMinesAround (row,col):
    totalAroundSpot=0
    r=row-1
    while r<= row+1:
        if r>=0 and r<TotalRows:
            c=col-1
            while c<=col+1:
                if c>=0 and c<TotalCols:
                    totalAroundSpot=totalAroundSpot+board[r][c]
                c=c+1
        r=r+1
    return totalAroundSpot

#add mines

num=0 #num active mines
while num < numMines:
    row = random.randint(0,TotalRows-1)
    col = random.randint(0,TotalCols-1)

    if board[row][col] == 0:
        board[row][col]=1 #addmine
    num+=1


def displaySol():
    for row in range(0,TotalRows):
        for col in range(0,TotalCols):
            print(board[row][col],end=" ")
        print("")



def displayBoard():
    print("-"*25)
    for row in range(0,TotalRows):
        print(" ", end = " | ")
        for col in range(0,TotalCols):
            if boardDisplay[row][col]==-1:
                print(" ", end = " | ")
            else:
                print(boardDisplay[row][col],end=" | ")
        print("")
        print("-"*25)
# displaySol() #for debugging
displayBoard() #for debugging

guess = 0
while guess < (TotalRows*TotalCols-numMines):
    row=int(input("guess a row(1," +str(TotalRows)+"): "))-1
    col=int(input("guess a col(1,"+str(TotalCols)+"): "))-1
    if board[row][col]==1:
        print("boom you died")
        displaySol()
        break
    else:
        boardDisplay[row][col]=checkMinesAround(row,col)
        displayBoard()
