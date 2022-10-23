#  ===================================================================
#  Source File Name : user_display_footprint.py
#  Purpose          : Footprint specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_schematic(symbolname, symbol, printout=False):
    output_text: list[str] = ["Symbol name is " + symbolname, "Symbol is " + symbol]

    if printout:
        textbox("Details for Symbol " + symbolname, "Symbol", output_text, False)
        return None
    else:
        return output_text
