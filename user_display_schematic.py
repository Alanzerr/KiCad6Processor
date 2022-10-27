#  ===================================================================
#  Source File Name : user_display_schematic.py
#  Purpose          : Schematic specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_schematic(schematicname, schematic, printout=False):
    output_text: list[str] = ["Schematic name is " + schematicname, "\nSchematic is " + str(schematic)]

    if printout:
        textbox("Details for Schematic " + schematicname, "Schematic", output_text, False)
        return None
    else:
        return output_text
