#  ===================================================================
#  Source File Name : kicad_mod.py
#  Purpose          : Process KiCad6 Footprints (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.footprint import *

from debug_print import *
from user_display_footprint import *


# ==================================================================================================================
def process_kicad_mod(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Footprint filename is %s." % filename)

    footprint = Footprint().from_file(filename)

    print_footprint(fname, footprint, True)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = list

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Footprint"

        choices = list()
        choices.append("Print Contents of Footprint")    # Task 1

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                print_footprint("Module", fname, footprint)

                footprint.to_file(new_filename)

                msgbox(msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is "
                           + new_filename + ".",
                       title="KiCad Footprint file",
                       ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")

            case "Exit":
                debug_print("User selected Exit.")
