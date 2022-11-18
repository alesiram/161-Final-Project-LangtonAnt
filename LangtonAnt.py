# Name: Marisela Vasquez
# Date: 08/10/21
# Description: program is a simulation of a virtual "ant" that moves about a two-dimensional
#              square matrix, whose spaces can be designated white or black

# collects user input for the info needed to initialize the simulation
def main():
    """ function collects user input """
    print("Welcome to Langton’s ant simulation!")
    print("First, please enter a number no larger than 100 for the size of the square board:")
    board_size = int(input())
    print("Choose the ant’s starting location, please enter a number as the starting row number "
          "(where 0 is the first row from the top):")
    ant_strtn_row = int(input())
    print("Please enter a number as the starting column number (where 0 is the first column from the left):")
    ant_strtn_colum = int(input())
    print("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:")
    ant_strtn_direction = int(input())

    # initialize new ant object
    ant = Ant(board_size, ant_strtn_row, ant_strtn_colum, ant_strtn_direction)

    print("Please enter the number of steps for the simulation:")
    steps_to_make = int(input())

    ant.start_simulation(steps_to_make)

    ant.print_board()


class Ant:
    """class to stimulate Langton's Ant by initializing the Ant object"""

    def __init__(self, size, start_row, start_column, orientation):  # initializes data members, private
        self._board_size = size
        self._board = [['_' for _ in range(size)] for _ in range(size)]
        self._current_row = start_row
        self._current_column = start_column
        self._direction = orientation
        # put the ant on the board

    # this function will increment the step counter, use Ant object to store Ants current position/direction,
    # move Ant based on the movement rule, change the color of the space on the board the Ant just left
    def start_simulation(self, steps_to_make):
        """function will start the ant movement based on Langton's rules """
        for _ in range(steps_to_make):
            # Update ant direction
            self.update_direction()
            # Flip ant's current square color
            # Updating color first, because if ants moves forward first, we wont know old position
            self.update_square_color()
            # Move the ant forward one based on current direction
            self.move_ant_forward()

    def move_ant_forward(self):
        """ function that moves ant on board using mod operation and size of board"""
        # Using mod operator to wrap ant position to other side of board if current on an edge

        # ant direction up
        if self._direction == 0:
            self._current_row = (self._current_row - 1) % self._board_size
        # ant direction down
        elif self._direction == 2:
            self._current_row = (self._current_row + 1) % self._board_size
        # ant direction right
        elif self._direction == 1:
            self._current_column = (self._current_column + 1) % self._board_size
        # ant direction left
        elif self._direction == 3:
            self._current_column = (self._current_column - 1) % self._board_size

    def update_square_color(self):
        """ updates the square color before moving onto next square"""
        # if current square is white, make it black
        if self._board[self._current_row][self._current_column] == '_':
            self._board[self._current_row][self._current_column] = '#'
        # since square is black, make it white
        else:
            self._board[self._current_row][self._current_column] = '_'

    def update_direction(self):
        """ moves ant to next square"""
        # 0 - up
        # 1 - right
        # 2 - down
        # 3 - left

        # If the ant is on a white space, it will turn right 90 degrees
        if self._board[self._current_row][self._current_column] == '_':
            if self._direction == 0:
                self._direction = 1
            elif self._direction == 1:
                self._direction = 2
            elif self._direction == 2:
                self._direction = 3
            elif self._direction == 3:
                self._direction = 0

        # If the ant is on a black space, it will turn left 90 degrees
        if self._board[self._current_row][self._current_column] == '#':
            if self._direction == 0:
                self._direction = 3
            elif self._direction == 3:
                self._direction = 2
            elif self._direction == 2:
                self._direction = 1
            elif self._direction == 1:
                self._direction = 0

    # print board for user
    def print_board(self):
        """ function runs after simulation finishes, displays the board"""
        # adding ant to board for printing once all moves are done
        # otherwise logic for checking square color will break
        self._board[self._current_row][self._current_column] = '8'

        for col in range(self._board_size):
            for row in range(self._board_size):
                print(self._board[col][row], end="")
            print()


main()
