#  ===================================================================
#  Source File Name : kicad_wks.py
#  Purpose          : Process KiCad6 Worksheets (for PCB and Schematics).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from debug_print import *
from user_display_wks import *


# ==================================================================================================================
def process_kicad_wks(fdir, fname, fext, odir):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Worksheet filename is %s." % filename)

    worksheet = WorkSheet().from_file(filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Worksheet"

        choices = list()
        choices.append("Print Contents of WorkSheet")    # Task 1
        choices.append("Save Modified WorkSheet")        # Task 2

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                print_worksheet(fname, worksheet, True)

            case "Task 2":
                debug_print("User selected %s." % choice)

                worksheet.to_file(new_filename)

                msgbox(msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                       title="KiCad Worksheet file",
                       ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
