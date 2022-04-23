"""
Filename: tictactoe.py
Author: Amanda Parker

CSE 210-

Purpose: Design a Tic-Tac-Toe game

"""

# identify global variables
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
currentPlayer = "X"
winner = ""
gameRunning = True


# design and display board
def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


# request player input, and validate input
def playerInput(board):
    playerSelect = int(
        input(f"{currentPlayer}'s turn to choose a square (1-9):"))
    if playerSelect >= 1 and playerSelect <= 9 and board[playerSelect-1] != "X" and board[playerSelect-1] != "O":
        board[playerSelect-1] = currentPlayer
    else:
        print("\n  Oops, please select a different square.")


# identify winner horizontally
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True


# identify winner vertically
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True


# identify winner diagonally
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        return True


# consolidate check for winner
def checkWin(board):
    global gameRunning
    if checkRow(board) or checkColumn(board) or checkDiagonal(board):
        printBoard(board)
        print(
            f"\n *****The WINNER is {winner}! Congratulations {winner}!*****\n")
        gameRunning = False


# check to see if the game is a draw
def checkDraw(board):
    global gameRunning
    moves = 0
    for a in range(0, 9):
        if board[a] == "X" or board[a] == "O":
            moves += 1
    if moves == 9:
        print("\n *****The game ended in a draw!*****\n")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# ask to play again, and reset all global variables if "Y"
def askPlayAgain():
    global gameRunning
    global board
    global currentPlayer
    global winner
    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain.upper() == "Y":
        board = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]
        if winner == "X" or winner == "0":
            currentPlayer = winner
            print(f"{winner} goes first!")
        else:
            currentPlayer = "X"
            print("X goes first!")
        winner = ""
        gameRunning = True
    else:
        gameRunning = False


# define playing the game
def main():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin(board)
        checkDraw(board)
        switchPlayer()

        # When the game is done, ask if they want to play again
        if gameRunning == False:
            askPlayAgain()


# execute the game
if __name__ == "__main__":
    main()
