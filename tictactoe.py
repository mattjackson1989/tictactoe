#       Tic Tac Toe
#       Mathew Jackson
#       copyright(c) 2017
#       This Tic Tac Toe game demonstrates the
#       use of Artificial intelligence.
#

import random

# WINNING MOVES
# 1 = PLAYER, 2 = COMPUTER
# rows
# if board[0] + board[1] + board[2] == 3 -> player wins
# if board[3] + board[4] + board[5] == 3 -> player wins
# if board[6] + board[7] + board[8] == 3 -> player wins
# columns
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
        print("You are X's")
        printBoard()
        move = input("What is your move? ")
        occupiedSpots[int(move)] = 5
        board[int(move)] = 1
        first = True
    else:
        print("Computer goes first")
        print("You are O's")
        placeMiddle(occupiedSpots)
        first = False
    # must make game rules, must make AI
    while True:
        print("press [h] for controls")
        printBoard()
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
            board[int(userInput)] = 1
            if checkIfWinner(occupiedSpots):
                break
        else:
            # player goes first within the loop
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = 5
            board[int(userInput)] = 1
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
        print(board[x], end="")
        if x == 2 or x == 5:
            print()
    print()

# TODO: Work on integrating column logic
# A.I. Rule 1 - Defense/Victory
def defenseVictory(oc_board):
    print()
    # FOR ROWS:
    # DEFENSE SECTION
    # possible top-row loss
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 10:
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = 2
            return True
        if oc_board[1] == 0:
            oc_board[1] = 2
            board[1] = 2
            return True
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = 2
            return True
    # Possible middle-row loss
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 10:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = 2
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = 2
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = 2
            return True
    # Possible bottom-row loss
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 10:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = 2
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = 2
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = 2
            return True
    # VICTORY SECTION
    # possible top-row Victory
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 4 or int(oc_board[0]) + int(oc_board[1]) + int(
            oc_board[2]) == 2:
        if oc_board[0] == 0:
            oc_board[0] = 2
            board[0] = 2
            return True
        if oc_board[1] == 0:
            oc_board[1] = 2
            board[1] = 2
            return True
        if oc_board[2] == 0:
            oc_board[2] = 2
            board[2] = 2
            return True
    # Possible middle-row Victory
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 4 or int(oc_board[3]) + int(oc_board[4]) + int(
            oc_board[5]) == 2:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = 2
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = 2
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = 2
            return True
    # Possible bottom-row Victory
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 4 or int(oc_board[3]) + int(oc_board[4]) + int(
            oc_board[5]) == 2:
        if oc_board[3] == 0:
            oc_board[3] = 2
            board[3] = 2
            return True
        if oc_board[4] == 0:
            oc_board[4] = 2
            board[4] = 2
            return True
        if oc_board[5] == 0:
            oc_board[5] = 2
            board[5] = 2
            return True

    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == 4 or int(oc_board[6]) + int(oc_board[7]) + int(
            oc_board[8]) == 2:
        if oc_board[6] == 0:
            oc_board[6] = 2
            board[6] = 2
            # 6
            return True
        if oc_board[7] == 0:
            oc_board[7] = 2
            board[7] = 2
            return True
        if oc_board[8] == 0:
            oc_board[8] = 2
            board[8] = 2
            return True



# A.I. Rule 2 - Offense
def offense(List):
    print("Offense is taking place")
    randomMethod(List)


def randomMethod(List):
    choice = random.randrange(0, 9)
    # check to make sure the spot is available
    while True:
        if List[choice] == 0:
            List[choice] = 2
            board[choice] = 2
            break
        else:
            choice = random.randrange(0, 9)
    print(choice)


def placeMiddle(List):
    if board[4] == 0:
        board[4] = 2
        List[4] = 2
        print("Placed in Center")


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
        if board[x] == 1 or board[x] == 2:
            n += 1
    if n == 9:
        printBoard()
        print("Tie Game")
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
