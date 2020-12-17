from random import randint
from termcolor import colored

COLORS = ['r', 'y', 'g', 'b', 'm']  # list of used colors


# convert color initial to full name
def get_full_color_name(initial: str) -> str:
    if initial == 'r':
        return "red"
    elif initial == 'y':
        return "yellow"
    elif initial == 'g':
        return "green"
    elif initial == 'b':
        return "blue"
    elif initial == 'm':
        return "magenta"
    else:
        raise Exception("Unknown color!")


# each cell has its color
class Cell:
    def __init__(self, color_idx: int):
        self.color = COLORS[color_idx]


# the main board of the game.
# holds all of the cell and other relevant data
class Board:
    def __init__(self, size: int):
        self.__board_size = size
        self.__board = [[Cell(randint(0, len(COLORS) - 1)) for _ in range(size)] for _ in range(size)]  # init cell with random colors
        self.__steps = 0

    # ============================== Public methods =======================================

    # Change the color of the corner tile to the requested color, and than recursively try to apply the color to
    # neighboring tiles
    def apply_color(self, new_color: str):
        orig_color = self.__board[0][0].color
        self.__board[0][0].color = new_color  # apply color the corner tile

        if orig_color == new_color:  # if new color is same is original color - nothing happens
            return

        # initiate recursion on neighboring tiles
        return self.__apply_color(new_color, orig_color, 1, 0), \
               self.__apply_color(new_color, orig_color, 0, 1)

    # print board into terminal
    def print_board(self):
        for row in range(self.__board_size):
            for col in range(self.__board_size):
                print(colored("  ", color=get_full_color_name(self.__board[row][col].color),
                              on_color="on_" + get_full_color_name(self.__board[row][col].color), attrs=['bold']),
                      end="")
            print()

    # increase steps by 1
    def increment_steps(self):
        self.__steps += 1

    # get number of steps
    def get_steps(self) -> int:
        return self.__steps

    # check if all tiles are same color
    def is_ongoing(self) -> bool:
        orig_color = self.__board[0][0].color
        for row in range(self.__board_size):
            for col in range(self.__board_size):
                if self.__board[row][col].color != orig_color:
                    return True

        return False

    # ============================== Private methods =======================================

    # apply new color to tile, and continue recursion
    def __apply_color(self, new_color: str, orig_color: str, row_idx: int, col_idx: int):
        # first we check that tile is within the board. if it is - if original color is same as tile color, paint it with
        # new color. otherwise, return.
        if row_idx < 0 or col_idx < 0 or row_idx >= self.__board_size or col_idx >= self.__board_size or \
                self.__board[row_idx][col_idx].color != orig_color or self.__board[row_idx][col_idx].color == new_color:
            return
        else:
            self.__board[row_idx][col_idx].color = new_color

        # apply recursion to neighboring tiles
        return self.__apply_color(new_color, orig_color, row_idx - 1, col_idx), \
               self.__apply_color(new_color, orig_color, row_idx, col_idx - 1), \
               self.__apply_color(new_color, orig_color, row_idx + 1, col_idx), \
               self.__apply_color(new_color, orig_color, row_idx, col_idx + 1)

