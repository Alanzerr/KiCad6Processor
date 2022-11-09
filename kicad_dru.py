#  ===================================================================
#  Source File Name : kicad_dru.py
#  Purpose          : Process KiCad6 Design Rules (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.dru import Constraint
from kiutils.dru import DesignRules
from kiutils.dru import Rule

from debug_print import *
from user_display_dru import *


# ==================================================================================================================
def process_kicad_dru(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Design Rule filename is %s." % filename)

    designrules = DesignRules().from_file(filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Design Rule(s)"

        choices = list()
        choices.append("Print Contents of Design Rules")    # Task 1
        choices.append("Save Modified Design Rules")        # Task 2

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                print_designrules(fname, designrules, True)

            case "Task 2":
                debug_print("User selected %s." % choice)

                designrules.to_file(new_filename)

                msgbox(msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                       title="KiCad Design Rules file",
                       ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
