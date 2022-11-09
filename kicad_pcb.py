#  ===================================================================
#  Source File Name : kicad_pcb.py
#  Purpose          : Process KiCad6 PCB (and library table)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os
from datetime import datetime

from kiutils.board import Board
from kiutils.footprint import *
from kiutils.libraries import LibTable

from debug_print import *
from user_display_board import *
from user_display_libtable import *
from user_display_footprint import *


# ==================================================================================================================
def init_footprint(name):
    footprint = Footprint()

    # Update to reflect Base Information
    # current date and time
    date = datetime.now()

    footprint.LibraryLink = name
    footprint.version     = date.strftime("%Y") + date.strftime("%m") + date.strftime("%d")
    footprint.generator   = "pcbnew"
    footprint.locked      = False
    footprint.placed      = False
    footprint.layer       = "F.Cu"
    footprint.placed      = False
    footprint.tedit       = 0

    return footprint


# ==================================================================================================================
def process_kicad_pcb(fdir, fname, fext):
    filename = fdir + fname + fext
    lib_table_filename = fdir + "fp-lib-table"

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext
    new_lib_table_filename = fdir + sub_folder + "\\" + "fp-lib-table"

    debug_print("KiCad PCB filename is %s." % filename)
    debug_print("KiCad PCB Library filename is %s." % lib_table_filename)

    pcb_lib_table = LibTable().from_file(lib_table_filename)
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
                debug_print("User selected %s." % choice)

                print_board(fname, board, True)

            case "Task 2":
                debug_print("User selected %s." % choice)

                print_libtable(fname, pcb_lib_table, True)

            case "Task 3":
                # Get name for new footprint
                footprintname = user_input()

                # set the basic attributes
                footprint = init_footprint(footprintname)

                print_footprint("Module", footprintname, footprint)

                modfilename = fdir + sub_folder + "\\" + footprintname + ".kicad_mod"
                footprint.to_file(modfilename)

                msgbox(msg="KiCad Input file " + filename
                           + " have been processed.\n\r \n\rProcessed files are "
                           + modfilename + ".",
                       title="KiCad Footprint file)",
                       ok_button="Exit function")

            case "Task 4":
                debug_print("User selected %s." % choice)

                board.to_file(new_filename)
                pcb_lib_table.to_file(new_lib_table_filename)

                msgbox(msg="KiCad Input file " + filename + " (and its library table) have been processed.\n\r \n\rProcessed files are "
                           + new_filename + " and " + new_lib_table_filename + ".",
                       title="KiCad PCB file (and Library Table)",
                       ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
