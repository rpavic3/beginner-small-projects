import random
import time


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

print(0 , " | " , 1 , " | " , 2)
print("-------------")
print(3 , " | " , 4 , " | " , 5)
print("-------------")
print(6 , " | " , 7 , " | " , 8)


currentPlayer = "X"
winner = None
gameRunning = True
count = 0

# game board
def printBoard(board):
    global gameRunning
    print(board[0] , " | " , board[1] , " | " , board[2])
    print("-------------")
    print(board[3] , " | " , board[4] , " | " , board[5])
    print("-------------")
    print(board[6] , " | " , board[7] , " | " , board[8])
    if checkIfWin(board) or checkIfTie(board):
        gameRunning = False


# take player input
def playerInput(board):
    global count
    inp = int(input("Select a spot 0-8: "))
    if board[inp] == "-":
        board[inp] = currentPlayer
        count = count + 1
    else:
        print("Oops player is already at that spot.")
        playerInput(board)


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):    
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):        
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):       
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    global count
    if count >= 5 and gameRunning:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
    else:
        gameRunning = True


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while currentPlayer == "O" and gameRunning:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



while gameRunning:
    checkIfWin(board)
    checkIfTie(board)
    playerInput(board)
    printBoard(board)
    print("\n\n")
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    time.sleep(1)
    printBoard(board)



