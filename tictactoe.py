#                                                Tic Tac Toe
#                                          Written and Documented by
#                                                Mathew Jackson
#                                              copyright(c) 2017
#
#       DESCRIPTION:
#       This Tic Tac Toe game demonstrates the use of Artificial intelligence.
#       Main starts at the very bottom and the code works itself up towards the top
#       with some minor jumps. Should be very self explainitory once you start at main
#       and work your way up.
#       FEATURES:
#           PLAYER VS COMPUTER(EASY, HARD), PLAYER VS PLAYER, EASTER EGG B-)
#                                   WINNING MOVES TOTAL: 8
#       FOR PLAYER VS COMPUTER:
#            X = PLAYER, O = COMPUTER if player is first and O = PLAYER, X = COMPUTER if
#            computer goes first.
#       FOR PLAYER VS PLAYER:
#            PLAYER 1 = X, PLAYER 2 = O -- no reason to switch
#       TO RUN: Stand alone .py file. Run as normal for your system with .py files.
#               <user>$python tictactoe.py
#       BUGS:
#           NONE A.T.M B-)
#####################################################################################################
# libraries
import random
# global variables
# The game board that will store the visual symbols for output
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
# end global variables
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
            if move.isdigit():
                if int(move) >= 0 and int(move) <= 8:
                    if occupiedSpots[int(move)] == 0:
                        occupiedSpots[int(move)] = 5
                        board[int(move)] = "x"
                        first = True
                        break
                    else:
                        print("Move is already occupied. Choose another.\n")
                else:
                    print("Input is out of bounds")
            else:
                print("Not a digit")
    else:
        print("Computer goes first")
        placeMiddle(occupiedSpots)
        printBoard()
        first = False
    # REAL game loop #
    while True:
        # Player will go after computer in loop
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
            while True:
                userInput = input("What is your move? ")
                if occupiedSpots[int(userInput)] == 0:
                    occupiedSpots[int(userInput)] = 5
                    board[int(userInput)] = "x"
                    break
                else:
                    print("That spot is already occupied. Try another.\n")
            if checkIfWinner(occupiedSpots):
                break
        else:
            # Player goes first within the loop
            while True:
                userInput = input("What is your move? ")
                if occupiedSpots[int(userInput)] == 0:
                    occupiedSpots[int(userInput)] = 5
                    board[int(userInput)] = "x"
                    break
                else:
                    print("That spot is already occupied. Try another.\n")
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
################################################# GAME LOGIC SECTION ###################################################
# OC_BOARD == occupied board. Which spots are currently occupied by player or computer
# A.I. Rule 1 - Defense/Victory
def defenseVictory(oc_board):
    print()
    # FOR ROWS:
    # DEFENSE SECTION --  NEED to implement VICTORY first
    # possible left-column victory
    if int(oc_board[0]) + int(oc_board[3]) + int(oc_board[6]) == 4:
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
    # possible middle-column victory
    if int(oc_board[1]) + int(oc_board[4]) + int(oc_board[7]) == 4:
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
    # possible right-column victory
    if int(oc_board[2]) + int(oc_board[5]) + int(oc_board[8]) == 4:
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
    # possible top-row victory
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 4:
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
    # possible middle-row victory
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 4:
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
    # possible bottom-row victory
    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == 4:
        if oc_board[6] == 0:
            oc_board[6] = 2
            board[6] = "o"
            return True
        if oc_board[7] == 0:
            oc_board[7] = 2
            board[7] = "o"
            return True
        if oc_board[8] == 0:
            oc_board[8] = 2
            board[8] = "o"
            return True
    ####################################### -End VICTORY section- ##########################################
    # possible left-column loss
    if int(oc_board[0]) + int(oc_board[3]) + int(oc_board[6]) == 10:
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
    if (int(oc_board[1]) + int(oc_board[4]) + int(oc_board[7]) == 10 or int(oc_board[1]) + int(oc_board[4]) + int(
            oc_board[7]) == 4):
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
    if (int(oc_board[2]) + int(oc_board[5]) + int(oc_board[8]) == 10 or int(oc_board[2]) + int(oc_board[5]) + int(
            oc_board[8]) == 4):
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
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == 10 or int(oc_board[0]) + int(oc_board[1]) + int(
            oc_board[2]) == 4:
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
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == 10 or int(oc_board[3]) + int(oc_board[4]) + int(
            oc_board[5]) == 4:
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
    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == 10 or int(oc_board[6]) + int(oc_board[7]) + int(
            oc_board[8]) == 4:
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
    if int(oc_board[6]) + int(oc_board[4]) + int(oc_board[2]) == 10 or int(oc_board[6]) + int(oc_board[4]) + int(
            oc_board[2]) == 4:
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
    if int(oc_board[0]) + int(oc_board[4]) + int(oc_board[8]) == 10 or int(oc_board[0]) + int(oc_board[4]) + int(
            oc_board[8]) == 4:
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
#################################################### END GAME LOGIC ####################################################
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
# Options
def userOptions():
    print("*****-----User Options-----*****\n")
    print("1.) Computer VS Player")
    print("2.) Player VS Player")
    print("3.) EXIT\n")
    while 1:
        answer = input("Please enter a selectable digit: ")
        if answer.isdigit():
            if int(answer) > 0 and int(answer) < 5:
                return answer
# CHECK_BOARD_PVP -- This function will return whither the players move is valid or not,
# #             requires the board and the players move. 1 means valid, 2 means invalid
PVPMOVELIST = [False, False, False, False, False, False, False, False, False]
def checkIfWinnerPVP(oc_board, player):
    if player == 1:
        playerValue = 33
    else:
        playerValue = 60
    # rows check
    if int(oc_board[0]) + int(oc_board[1]) + int(oc_board[2]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    if int(oc_board[3]) + int(oc_board[4]) + int(oc_board[5]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    if int(oc_board[6]) + int(oc_board[7]) + int(oc_board[8]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    # columns
    if int(oc_board[0]) + int(oc_board[3]) + int(oc_board[6]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    if int(oc_board[1]) + int(oc_board[4]) + int(oc_board[7]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    if int(oc_board[2]) + int(oc_board[5]) + int(oc_board[8]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    # diagnal
    if int(oc_board[0]) + int(oc_board[4]) + int(oc_board[8]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    if int(oc_board[2]) + int(oc_board[4]) + int(oc_board[6]) == playerValue:
        print("Player " + str(player) + " Wins")
        return 1
    # if all spots are occupied and no winner is among us
    n = 0
    for x in range(0, 9):
        if(PVPMOVELIST[x] == True):
            n += 1
    if n == 9:
        print("TIE GAME!")
        return 1
    # end tie_check
def checkTheBoard(occupiedSpots, move):
    if int(occupiedSpots[move]) == 11 or int(occupiedSpots[move]) == 20:
        return 2
    else:
        return 1
# GAMELOOP FOR PVP
def gameLoopPVP():
    print("Numbers 0-8 are acceptable postions.\n0-2 is the first row\n3-5 is the second row\n6-8 is the third row")
    occupiedSpots = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    printBoard()
    # GAME LOOP
    while True:
        # PLAYER 1 input validation -- Player 1 is X's and is represented by the number 11
        while True:
            move = input("PLAYER 1: What is your move? ")
            if move.isdigit():
                if int(move) >= 0 and int(move) <= 8:
                    if checkTheBoard(occupiedSpots, int(move)) == 1:
                        occupiedSpots[int(move)] = 11
                        PVPMOVELIST[int(move)] = True
                        board[int(move)] = "x"
                        break
                    else:
                        print("That move is already occupied")
                else:
                    print("Input is out of bounds")
            else:
                print("Not a digit")
        printBoard()
        # check is winner
        if checkIfWinnerPVP(occupiedSpots, 1) == 1:
            return
        # PLAYER 2 input validation -- Player 2 is O's and is represented by the number 20
        while True:
            move = input("PLAYER 2: What is your move? ")
            if move.isdigit():
                if int(move) >= 0 and int(move) <= 8:
                    if checkTheBoard(occupiedSpots, int(move)) == 1:
                        occupiedSpots[int(move)] = 20
                        PVPMOVELIST[int(move)] = True
                        board[int(move)] = "o"
                        break
                    else:
                        print("That move is already occupied")
                else:
                    print("Input is out of bounds")
            else:
                print("Not a digit")
        printBoard()
        # check is winner
        if checkIfWinnerPVP(occupiedSpots, 2) == 1:
            return
# "EASY MODE" -- uses the AI rule #2 to pick spots randomly, check if occupied, and place. No logic for decision making
def playEasyMode(xOrO):
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
            if move.isdigit():
                if int(move) >= 0 and int(move) <= 8:
                    if occupiedSpots[int(move)] == 0:
                        occupiedSpots[int(move)] = 5
                        board[int(move)] = "x"
                        first = True
                        break
                    else:
                        print("Move is already occupied. Choose another.\n")
                else:
                    print("Input is out of bounds")
            else:
                print("Not a digit")
    else:
        print("Computer goes first")
        offense(occupiedSpots)
        printBoard()
        first = False
    # REAL game loop #
    while True:
        # Player will go after computer in loop
        if first:
            # computer goes first within loop
            offense(occupiedSpots)
            if checkIfWinner(occupiedSpots):
                break
            printBoard()
            while True:
                userInput = input("What is your move? ")
                if occupiedSpots[int(userInput)] == 0:
                    occupiedSpots[int(userInput)] = 5
                    board[int(userInput)] = "x"
                    break
                else:
                    print("That spot is already occupied. Try another.\n")
            if checkIfWinner(occupiedSpots):
                break
        else:
            # Player goes first within the loop
            while True:
                userInput = input("What is your move? ")
                if occupiedSpots[int(userInput)] == 0:
                    occupiedSpots[int(userInput)] = 5
                    board[int(userInput)] = "x"
                    break
                else:
                    print("That spot is already occupied. Try another.\n")
            if checkIfWinner(occupiedSpots):
                break
            printBoard()
            offense(occupiedSpots)
            print("Completed offense f(x)")
            if checkIfWinner(occupiedSpots):
                break
            printBoard()
        # emergency abort
        if userInput == "quit":
            break
    return
# player vs player initializer
def playerVsPlayer():
    print("\n\n\n*****-----Welcome to Player VS Player!-----*****")
    print("Player 1: X's\nPlayer 2: O's\n")
    gameLoopPVP()
# player vs computer initializer
def playerVsComputer():
    print("\n\n\n*****-----Welcome to Player VS Computer!-----*****\n")
    print("MODE: EASY or HARD (easy, hard)")
    while True:
        answer = input("easy or hard: ")
        if answer == "easy" or answer == "hard":
            if answer == "easy":
                print("**************Entering \"Easy Mode\" ******************")
                print("Would you like to go first? (yes, no)")
                while True:
                    answer = input()
                    if answer == "yes" or answer == "no":
                        print("Start game")
                        playEasyMode(answer)
                        return
                    else:
                        print("Incorrect input, try again")
                return
            else:
                print("\nBrace yourself.....\n\n(Skynet enters the mainframe)\n\"Hello, I am Skynet: Master of tic Tac Toe!\"\n")
                break;
        else:
            print("Incorrect input.\nPlease type 'easy' or 'hard'")
    print("Would you like to go first? (yes, no)")
    answer = input()
    if answer == "yes" or answer == "no":
        print("Start game")
        gameLoop(answer)  # start game
        return
    else:
        print("Incorrect input, try again")
# interface for main to different game modes
def main2ModeInterface(userInputer):
    if int(userInputer) == 1:
        print("Starting PVC.function!")
        playerVsComputer()
        return
    if int(userInputer) == 2:
        print("Starting PVP.function!")
        playerVsPlayer()
        return
    if int(userInputer) == 3:
        print("\n\nExiting Program\n\nGOODBYE")
        return
    if int(userInputer) == 4:
        print("\n\n\n\nEASTER EGGGGGGGGGGGGGGGGGGGGGGGGGG")
# Welcome screen and decision to go first or not
def main():
    print("Welcome to Tic Tac Toe: AI Edition\nWritten and Documented by\nMathew Jackson\n2017(c)\n")
    # Ask what the user would like to do: PVE, PVP, 4x4, EXIT
    userInputer = userOptions()
    # send to game mode
    main2ModeInterface(userInputer)
# Start Program
main()
