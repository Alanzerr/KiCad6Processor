#  ===================================================================
#  Source File Name : user_display_dru.py
#  Purpose          : Design Rules specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_schematic(druname, dru, printout=False):
    output_text: list[str] = ["Design Rules name is " + druname, "Design Rules is " + dru]

    if printout:
        textbox("Details for Design Rules " + druname, "Design Rules", output_text, False)
        return None
    else:
        return output_text
