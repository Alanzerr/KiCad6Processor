#  ===================================================================
#  Source File Name : user_display_wks.py
#  Purpose          : Worksheet specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_schematic(wksname, wks, printout=False):
    output_text: list[str] = ["Worksheet name is " + wksname, "Worksheet is " + wks]

    if printout:
        textbox("Details for Worksheet " + wksname, "Worksheet", output_text, False)
        return None
    else:
        return output_text
