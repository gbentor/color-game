from Board import Board, COLORS
import copy
import os
import time

BOARD_SIZE = 18
ALLOWED_STEPS = 21

board = Board(BOARD_SIZE)
board.print_board()
all_board = [copy.deepcopy(board)]
while board.get_steps() < ALLOWED_STEPS:
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
            print("Congratulations! You have won the game!!!")
            board_copy.print_board()
            time.sleep(0.5)
            os.system('clear')
        break
else:
    print(f"Oh no! You didn't finish the game in {ALLOWED_STEPS} steps... You lose!")