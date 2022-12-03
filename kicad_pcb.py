#  ===================================================================
#  Source File Name : kicad_pcb.py
#  Purpose          : Process KiCad6 PCB (and library table)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os
# import math
# import datetime
from kicad_pcb_tasks import *

from kiutils.board import *
# from kiutils.footprint import *
from kiutils.libraries import *

from debug_print import *
# from user_display_board import *
# from user_display_libtable import *
from user_display_footprint import *


# ==================================================================================================================
def process_kicad_pcb(idir, fname, fext, odir):
    filename = idir + fname + fext
    lib_table_filename = idir + "fp-lib-table"

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not path.exists(path.join(idir, sub_folder)):
        os.mkdir(path.join(idir, sub_folder))

    new_filename = idir + sub_folder + "\\" + fname + fext
    new_lib_table_filename = idir + sub_folder + "\\" + "fp-lib-table"

    debug_print("KiCad PCB filename is %s." % filename)
    debug_print("KiCad PCB Library filename is %s." % lib_table_filename)

    # On new projects this file make not exist
    lib_table_exists = path.exists(path.join(lib_table_filename))

    if lib_table_exists:
        pcb_lib_table = LibTable().from_file(lib_table_filename)
    else:
        pcb_lib_table = None

    board = Board().from_file(filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "PCB"

        choices: list[str] = list()
        choices.append("Print Contents of Board")          # Task 1
        choices.append("Print Contents of Board Library")  # Task 2
        choices.append("Generate Footprint from Board")    # Task 3
        choices.append("Save Modified Board + Library")    # Task 4

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                pcb_task1(choice, fname, board)

            case "Task 2":
                pcb_task2(choice, fname, pcb_lib_table)

            case "Task 3":
                pcb_task3(filename, board, odir)

            case "Task 4":
                pcb_task4(choice, board, filename, new_filename, pcb_lib_table, new_lib_table_filename)

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
