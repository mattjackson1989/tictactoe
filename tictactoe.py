#       Tic Tac Toe
#       Mathew Jackson
#       copyright(c) 2017
#       This Tic Tac Toe game demonstrates the
#       use of Artificial intelligence.
#
#
import random
# WINNING MOVES
# 1 = PLAYER, 2 = COMPUTER
# rows
# if board[0] + board[1] + board[2] == 3 -> player wins
# if board[3] + board[4] + board[5] == 3 -> player wins
# if board[6] + board[7] + board[8] == 3 -> player wins
#columns
# if board[0] + board[3] + board[6] == 3 -> player wins
# if board[1] + board[4] + board[7] == 3 -> player wins
# if board[2] + board[5] + board[8] == 3 -> player wins
# diagnal
# if board[0] + board[4] + board[8] == 3 -> player wins
# if board[2] + board[4] + board[6] == 3 -> player wins

# Currently:
# NEED to make a "visual" board to track progress


board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# check board -- checks sum of target rows -- returns 3 if player wins or is about to win, 6 if computer for computer
def checkboard(targetSum, oc_board):
    #Check Player
    # rows
    if ((oc_board[0] == True and oc_board[1] == True and oc_board[2] == True) or (oc_board[3] == True and oc_board[4] == True and oc_board[5] == True) or
        (oc_board[6] == True and oc_board[7] == True and oc_board[8] == True)):
        return 3
    # columns
    if ((oc_board[0] == True and oc_board[3] == True and oc_board[6] == True) or (oc_board[1] == True and oc_board[4] == True and oc_board[7] == True) or
        (oc_board[2] == True and oc_board[5] == True and oc_board[8] == True)):
        return 3
    #     # diagnals
    if ((oc_board[0] == True and oc_board[4] == True and oc_board[8] == True) or (oc_board[2] == True and oc_board[4] == True and oc_board[6] == True)):
        return 3
    return 0
    #
    # # Check Computer
    # if (board[0] + board[1] + board[2] == targetSum) or (board[3] + board[4] + board[5] == targetSum) or (
    #         board[6] + board[7] + board[8] == targetSum):
    #     return 6
    # # columns
    # if (board[0] + board[3] + board[6] == targetSum) or (board[1] + board[4] + board[7] == targetSum) or (
    #                     board[2] + board[5] + board[8] == targetSum):
    #     return 6
    #     # diagnals
    # if (board[0] + board[4] + board[8] == targetSum) or (board[2] + board[4] + board[6] == targetSum):
    #     return 6


# variable is X's or O's
def gameLoop(xOrO):
    # Occupied spots
    occupiedSpots = [0,0,0,0,0,0,0,0,0]
    # first 3 indices is the top row, second 3 indices is the middle row, third indices is the last row
    if xOrO == "yes":
        print("You are X's")
        printBoard()
        move = input("What is your move? ")
        occupiedSpots[int(move)] = True
        board[int(move)] = 1
        first = True
    else:
        print("Computer goes first")
        print("You are O's")
        offense(occupiedSpots)
        first = False
    # must make game rules, must make AI
    while True:
        print("This is the game loop: ")
        printBoard()
        # first check if a winner is among us!
        if checkIfWinner(occupiedSpots) == True:
            break
        if first == True:
        # computer goes first within loop
            defenseVictory()
            offense(occupiedSpots)
            printBoard()
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = True
            board[int(userInput)] = 1
        else:
            # player goes first within the loop
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = True
            board[int(userInput)] = 1
            printBoard()
            defenseVictory()
            offense(occupiedSpots)
            printBoard()
        # emergency abort
        if userInput == "quit":
            break
    return

# Print board
def printBoard():
    for x in range(0, 9):
        print(board[x], end="")
        if(x == 2 or x == 5):
            print()
    print()

# A.I. Rule 1 - Defense/Victory
def defenseVictory():
    print ("Hit defence/victory function")


# A.I. Rule 2 - Offense
def offense(list):
    print("Offense is taking place")
    choice = random.randrange(0, 9)
    # check to make sure the spot is available
    while True:
        if list[choice] == 0:
            list[choice] = False
            board[choice] = 2
            break
        else:
            choice = random.randrange(0, 9)
    print(choice)


def checkIfWinner(oc_board):
    if checkboard(3, oc_board) == 3:
        print("Player wins")
        return True
    if(checkboard(6, oc_board) == 6):
        print("Computer Wins")
        return True


def main():
    while True:
        print("Welcome to Tic Tac Toe: AI Edition")
        print("Would you like to go first? (yes, no)")
        answer = input()
        if answer == "yes" or answer == "no":
            print("Start game")
            gameLoop(answer)
            break
        else:
            print("Incorrect input, try again")
    return


# Start Program
main()

