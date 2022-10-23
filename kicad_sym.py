#  ===================================================================
#  Source File Name : kicad_sym.py
#  Purpose          : Process KiCad6 Symbol(s) (for Schematics).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.symbol import SymbolLib

from debug_print import *
from user_display_symbol import *


# ==================================================================================================================
def process_kicad_sym(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Symbol filename is %s." % filename)

    symbollib = SymbolLib().from_file(filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Symbol(s)"

        choices = list()
        choices.append("TestBed")  # Task 1

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                for item in SymbolLib:
                    print(f"{item}\"")

                symbollib.to_file(new_filename)

                msgbox(
                    msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                    title="KiCad Symbol file",
                    ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")

            case "Exit":
                debug_print("User selected Exit.")
