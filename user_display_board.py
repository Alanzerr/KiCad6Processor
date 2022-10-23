#  ===================================================================
#  Source File Name : user_display_board.py
#  Purpose          : Board specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_board(boardname, board, printout=False):
    output_text: list[str] = ["Board name is " + boardname, "Board is " + board]

    if printout:
        textbox("Details for Board " + boardname, "Board", output_text, False)
        return None
    else:
        return output_text
