#  ===================================================================
#  Source File Name : kicad_pro.py
#  Purpose          : Processes KiCad6 Project file (well it would if
#                     kiutils actually supported it!
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
import os

from debug_print import *
from user_display import *


# ==================================================================================================================
def process_kicad_pro(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Project filename is %s." % filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Project"

        choices = list()
        # Currently nothing to do!

        choice = user_selection(msg, choices)

        match choice:
            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
            case "Exit":
                debug_print("User selected Exit.")

                # Currently nothing is done beyond copying the file as kiutils does not support this file type!
                os.system("copy " + filename + " " + new_filename)

                msgbox(
                    msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                    title="KiCad Project file",
                    ok_button="Program will now close")
            case other:
                debug_print("User selected illegal option (%s)!" % choice)
