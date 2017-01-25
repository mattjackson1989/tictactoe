#                                           Tic Tac Toe
#                                           Mathew Jackson
#                                           copyright(c) 2017
#
#       DESCRIPTION:
#       This Tic Tac Toe game demonstrates the use of Artificial intelligence.
#            WINNING MOVES TOTAL: 8
#           X = PLAYER, O = COMPUTER
#
#       TO RUN: Stand alone .py file. Run as normal for your system with .py files.
#
#       BUGS:
#           INPUT CONTROL STILL NEEDS IMPLEMENTED.
#
#####################################################################################################

import random

# The game board that will store the visual symbols for output
board = ["-","-","-","-","-","-","-","-","-"]


# check board -- checks sum of target rows -- returns 3 if player wins or is about to win, 6 if computer for computer
def checkboard(oc_board):
    # Check Player
    # rows
    if ((oc_board[0] == 5 and oc_board[1] == 5 and oc_board[2] == 5) or (
                        oc_board[3] == 5 and oc_board[4] == 5 and oc_board[5] == 5) or
            (oc_board[6] == 5 and oc_board[7] == 5 and oc_board[8] == 5)):
        return 3
    # columns
    if ((oc_board[0] == 5 and oc_board[3] == 5 and oc_board[6] == 5) or (
                        oc_board[1] == 5 and oc_board[4] == 5 and oc_board[7] == 5) or
            (oc_board[2] == 5 and oc_board[5] == 5 and oc_board[8] == 5)):
        return 3
    # # diagnals
    if ((oc_board[0] == 5 and oc_board[4] == 5 and oc_board[8] == 5) or (
                        oc_board[2] == 5 and oc_board[4] == 5 and oc_board[6] == 5)):
        return 3

    # Check Computer
    if ((oc_board[0] == 2 and oc_board[1] == 2 and oc_board[2] == 2) or (
                        oc_board[3] == 2 and oc_board[4] == 2 and oc_board[5] == 2) or
            (oc_board[6] == 2 and oc_board[7] == 2 and oc_board[8] == 2)):
        return 6
    # columns
    if ((oc_board[0] == 2 and oc_board[3] == 2 and oc_board[6] == 2) or (
                        oc_board[1] == 2 and oc_board[4] == 2 and oc_board[7] == 2) or
            (oc_board[2] == 2 and oc_board[5] == 2 and oc_board[8] == 2)):
        return 6
    # # diagnals
    if ((oc_board[0] == 2 and oc_board[4] == 2 and oc_board[8] == 2) or (
                        oc_board[2] == 2 and oc_board[4] == 2 and oc_board[6] == 2)):
        return 6


# variable is X's or O's
def gameLoop(xOrO):
    print("Numbers 0-8 are acceptable postions.\n0-2 is the first row\n3-5 is the second row\n6-8 is the third row")
    # Occupied spots
    occupiedSpots = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # first 3 indices is the top row, second 3 indices is the middle row, third indices is the last row
    if xOrO == "yes":
        print("You are First")
        printBoard()
        # User input validation
        while True:
            move = input("What is your move? ")
            if(move.isdigit()):
                if(int(move) >= 0 and int(move) <= 8):
                    occupiedSpots[int(move)] = 5
                    board[int(move)] = "x"
                    first = True
                    break
                else:
                    print("Input is out of bounds")
            else:
                print("Not a digit")
    else:
        print("Computer goes first")
        placeMiddle(occupiedSpots)
        printBoard()
        first = False
    # REAL game loop
    while True:
        # first check if a winner is among us!

        if first:
            # computer goes first within loop
            if defenseVictory(occupiedSpots):
                print("Completed defenseVictory f(x)")
            else:
                offense(occupiedSpots)
                print("Completed offense f(x)")
            if checkIfWinner(occupiedSpots):
                break
            printBoard()
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = 5
            board[int(userInput)] = "x"
            if checkIfWinner(occupiedSpots):
                break
        else:
            # player goes first within the loop
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = 5
            board[int(userInput)] = "x"
            if checkIfWinner(occupiedSpots):
                break
            printBoard()
            if defenseVictory(occupiedSpots):
                print("Completed defenseVictory f(x)")
            else:
                offense(occupiedSpots)
                print("Completed offense f(x)")
            if checkIfWinner(occupiedSpots):
                break
            printBoard()

        # emergency abort
        if userInput == "quit":
            break
    return


# Print board
def printBoard():
    for x in range(0, 9):
        print(board[x], end=" ")
        if x == 2 or x == 5:
            print()
    print()


# GAME LOGIC SECTION


# A.I. Rule 1 - Defense/Victory
def defenseVictory(oc_board):
    print()
    # FOR ROWS:
    # DEFENSE SECTION
    # possible left-column loss
    if(int(oc_board[0]) + int(oc_board[3]) + int(oc_board[6]) == 10):
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = "o"
            return True
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = "o"
            return True
        if oc_board[6] == 0:
            oc_board[6] = 2
            board[6] = "o"
            return True
    # possible middle-column loss
    if(int(oc_board[1]) + int(oc_board[4]) + int(oc_board[7]) == 10):
        if oc_board[1] == 0:
            oc_board[1] = 2
            board[1] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[7] == 0:
            oc_board[7] = 2
            board[7] = "o"
            return True
    # possible right-column loss
    if (int(oc_board[2]) + int(oc_board[5]) + int(oc_board[8]) == 10):
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = "o"
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = "o"
            return True
        if oc_board[8] == 0:
            oc_board[8] = 2
            board[8] = "o"
            return True
    # possible top-row loss or possible left-column loss
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 10:
        print("TOP ROW")
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = "o"
            return True
        if oc_board[1] == 0:
            oc_board[1] = 2
            board[1] = "o"
            return True
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = "o"
            return True
    # Possible middle-row loss
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 10:
        print("Middle row")
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = "o"
            return True
    # Possible bottom-row loss
    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == 10:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = "o"
            return True
    # Possible diagnal loss: ascend
    if int(oc_board[6]) + int(oc_board[4]) + int(oc_board[2]) == 10:
        if oc_board[6] == 0:
            oc_board[6] = 2
            board[6] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = "o"
            return True
    # Possible diagnal loss: descend
    if int(oc_board[0]) + int(oc_board[4]) + int(oc_board[8]) == 10:
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[8] == 0:
            oc_board[8] = 2
            board[8] = "o"
            return True
    # VICTORY SECTION
    # possible top-row Victory
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 4 or int(oc_board[0]) + int(oc_board[1]) + int(
            oc_board[2]) == 2:
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = "o"
            return True
        if oc_board[1] == 0:
            oc_board[1] = 2
            board[1] = "o"
            return True
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = "o"
            return True
    # Possible middle-row Victory
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 4 or int(oc_board[3]) + int(oc_board[4]) + int(
            oc_board[5]) == 2:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = "o"
            return True
    # Possible bottom-row Victory
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 4 or int(oc_board[3]) + int(oc_board[4]) + int(
            oc_board[5]) == 2:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = "o"
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = "o"
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = "o"
            return True
    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == 4 or int(oc_board[6]) + int(oc_board[7]) + int(
            oc_board[8]) == 2:
        if oc_board[6] == 0:
            oc_board[6] = 2
            board[6] = "o"
            # 6
            return True
        if oc_board[7] == 0:
            oc_board[7] = 2
            board[7] = "o"
            return True
        if oc_board[8] == 0:
            oc_board[8] = 2
            board[8] = "o"
            return True



# A.I. Rule 2 - Offense - useful when no rules apply
def offense(List):
    print("Offense is taking place")
    randomMethod(List)

# choose a random location on the board that is not occupied
def randomMethod(List):
    choice = random.randrange(0, 9)
    # check to make sure the spot is available
    while True:
        if List[choice] == 0:
            List[choice] = 2
            board[choice] = "o"
            break
        else:
            choice = random.randrange(0, 9)
    print(choice)

# definitive best move, cancels 4 possible victory paths for opponent, use if PC goes first
def placeMiddle(List):
    if board[4] == "-":
        board[4] = "o"
        List[4] = 2
        print("Placed in Center")

# END GAME LOGIC

# Traverse list of rules to see if there is a winner
def checkIfWinner(oc_board):
    if checkboard(oc_board) == 3:
        printBoard()
        print("Player wins")
        return True
    if checkboard(oc_board) == 6:
        printBoard()
        print("Computer Wins")
        return True
    n = 0
    for x in range(0, 9):
        if board[x] == "x" or board[x] == "o":
            n += 1
    if n == 9:
        printBoard()
        print("Tie Game")
        return True

# Welcome screen and decision to go first or not
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
