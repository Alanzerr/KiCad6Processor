#  ===================================================================
#  Source File Name : kicad_wks.py
#  Purpose          : Process KiCad6 Worksheets (for PCB and Schematics).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.wks import WorkSheet

from debug_print import *
from user_display import *


# ==================================================================================================================
def process_kicad_wks(fdir, fname, fext):
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
        choices.append("TestBed")    # Task 1

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                print("Version   \"%s.\"" % worksheet.version)
                print("Generator \"%s.\"" % worksheet.generator)
                print("Setup     \"%s.\"" % worksheet.setup)

                for item in worksheet.drawingObjects:
                    print("Object    \"%s.\"" % item)

                print("Filepath  \"%s.\"" % worksheet.filePath)

                worksheet.to_file(new_filename)

                msgbox(
                    msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                    title="KiCad Worksheet file",
                    ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")

            case "Exit":
                debug_print("User selected Exit.")
