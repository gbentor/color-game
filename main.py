from Board import Board, COLORS, get_full_color_name
import copy
import os
import time

BOARD_SIZE = 18
ALLOWED_STEPS = 21

open_message = f"{len(COLORS)} colors are available: {[get_full_color_name(x) for x in COLORS]}.\nEach time you select a color it will be applied to the leftmost upper corner of the board,\n" \
               f"and to all tiles that are the same color as the corner tile, and which are directly connected to it " \
               f"(diagonal doesn't count).\nThe goal of the game is to color the entire board with a single color."

board = Board(BOARD_SIZE)
all_board = [copy.deepcopy(board)]
while board.get_steps() < ALLOWED_STEPS:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(open_message)
    board.print_board()
    in_color = input(f"\nYou have {ALLOWED_STEPS-board.get_steps()} steps left!\nEnter desired color: ")
    if in_color not in COLORS:
        print(f"Invalid input!! Should be in {COLORS}")
        continue

    board.apply_color(in_color)
    board.print_board()
    board.increment_steps()
    all_board.append(copy.deepcopy(board))

    if not board.is_ongoing():
        for board_copy in all_board:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Congratulations! You have won the game!!!")
            board_copy.print_board()
            time.sleep(0.5)
        break
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    board.print_board()
    print(f"Oh no! You didn't finish the game in {ALLOWED_STEPS} steps... You lose!")