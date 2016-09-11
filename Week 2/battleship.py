import os
from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4
#initializing board
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)
def print_board(board):
    for row in board:
        print (" ".join(row))
#start the game and printing the board

#define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)

guesses = 0;
guessQueue = [];

while guesses < NR_GUESSES:
    os.system('clear');
    print("Let's play Battleship!");
    print(str(ship_row) + ", " + str(ship_col));
    print_board(board);
    guess = input("Make a guess (x, y)").split(',');
    x = int(guess[0]);
    y = int(guess[1]);
    for attempt in guessQueue:
        if attempt == guess:
            print("You already guessed that one, try again!");
            continue;

    if(x == ship_row and y == ship_col):
        print("You sunk the enemies ship, congratulations!");
        break;

    else:
        guessQueue.append(guess);
        print("Miss!")
        board[y - 1][x - 1] = "X";
        guesses = guesses + 1;

print("You ran out of guesses!");

