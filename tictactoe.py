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
def checkboard(targetSum):
    #Check Player
    # rows
    if (board[0] + board[1] + board[2] == targetSum) or (board[3] + board[4] + board[5] == targetSum) or (
                        board[6] + board[7] + board[8] == targetSum):
        return 3
    # columns
    if (board[0] + board[3] + board[6] == targetSum) or (board[1] + board[4] + board[7] == targetSum) or (
                        board[2] + board[5] + board[8] == targetSum):
        return 3
        # diagnals
    if (board[0] + board[4] + board[8] == targetSum) or (board[2] + board[4] + board[6] == targetSum):
        return 3

    # Check Computer
    if (board[0] + board[1] + board[2] == targetSum) or (board[3] + board[4] + board[5] == targetSum) or (
                        board[6] + board[7] + board[8] == targetSum):
        return 6
    # columns
    if (board[0] + board[3] + board[6] == targetSum) or (board[1] + board[4] + board[7] == targetSum) or (
                        board[2] + board[5] + board[8] == targetSum):
        return 6
        # diagnals
    if (board[0] + board[4] + board[8] == targetSum) or (board[2] + board[4] + board[6] == targetSum):
        return 6


# variable is X's or O's
def gameLoop(xOrO):
    # Occupied spots
    occupiedSpots = [False, False, False, False, False, False, False, False, False]
    # first 3 indices is the top row, second 3 indices is the middle row, third indices is the last row
    if xOrO == "yes":
        print("You are X's")
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
        # first check if a winner is among us!
        if checkIfWinner() == True:
            break
        if first == True:
        # computer goes first within loop
            defenseVictory()
            offense(occupiedSpots)
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = True
            board[int(userInput)] = 1;
        else:
            # player goes first within the loop
            userInput = input("What is your move? ")
            occupiedSpots[int(userInput)] = True
            board[int(userInput)] = 1;
            defenseVictory()
            offense(occupiedSpots)
        # emergency abort
        if userInput == "quit":
            break
    return

# A.I. Rule 1 - Defense/Victory
def defenseVictory():
    print("Hit defence/victory function")


# A.I. Rule 2 - Offense
def offense(list):
    print("Offense is taking place")
    choice = random.randrange(0, 9)
    # check to make sure the spot is available
    while True:
        if list[choice] == False:
            list[choice] = True
            board[choice] = 2
            break
        else:
            choice = random.randrange(0, 9)
    print(choice)


def checkIfWinner():
    if checkboard(3) == 3:
        print("Player wins")
        return True
    if(checkboard(6) == 6):
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

