import numpy as np;

##############
# exercise 6 #
##############
print("\n")
print("exercise 6: \n\n")


NONE = '.'
RED = 'R'
YELLOW = 'Y'
FOUR = 4

class Game:
    """
    test vor documentatie
    """
    def _init_ (self, cols = 7, rows = 6):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.board = np.array([[NONE] * rows for _ in range(cols)])
        self.four_red = [RED] * FOUR
        self.four_yellow = [YELLOW] * FOUR
        print(self.board)
        print(self.four_red)
        print(self.four_yellow)


    def insert (self, column, color):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != NONE:
            raise Exception
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color


    def print_board (self):
        """Print the board."""
        print(' '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print(' '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()

    def get_winner(self):
        #mirrir_board = [list(r[::1)]
        transposed_board = self.board.transpose()
        cols = self.board.tolist()
        rows = transposed_board.tolist()
        posdiag = [list(np.diagonal(self.board, i)) for i in range(-2, 3)]
        print(posdiag, '\n')
        negdiag = [list(np.diagonal(self.board.fliplr, i)) for i in range(-2, 3)]
        print(negdiag, '\n')
        all = (cols, rows, posdiag, negdiag)
        for lst in chain(*all): # for every list in the chain
            red_counter = 0
            yellow_counter = 0
            for i in lst:
                if i == 'R':
                    yellow_counter = 0
                    red_counter += 1
                if i == 'Y':
                    red_counter = 0
                    yellow_counter +=1
                if red_counter == 4:
                    return 'R'
                if yellow_counter == 4:
                    return 'Y'