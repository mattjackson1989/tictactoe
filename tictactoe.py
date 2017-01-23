#       Tic Tac Toe
#       Mathew Jackson
#       copyright(c) 2017
#       This Tic Tac Toe game demonstrates the
#       use of Artificial intelligence.
#
#


def gameLoop(xOrO): # variable is X's or O's
    # first 3 indices is the top row, second 3 indices is the middle row, third indices is the last row
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if xOrO == "yes":
        move = input("What is your move?")
    else:
        print("Computer goes first")
# must make game rules, must make AI
    while True:
        print("This is the game loop: ")
        userInput = input("What is your move?")
        if userInput == "quit":
            break
    return


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

# Initialize program
main()

