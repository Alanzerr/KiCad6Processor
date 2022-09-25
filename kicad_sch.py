#  ===================================================================
#  Source File Name : kicad_sch.py
#  Purpose          : Process KiCad6 Schematics (and library table)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
import tkinter as tk
import os

from kiutils.schematic import Schematic
from kiutils.libraries import LibTable

from debug_print import *
from user_display import *


# ==================================================================================================================
def process_kicad_sch(fdir, fname, fext):
    filename = fdir + fname + fext
    lib_table_filename = fdir + "sym-lib-table"

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext
    new_lib_table_filename = fdir + sub_folder + "\\" + "sym-lib-table"

    debug_print("KiCad Schematics filename is %s." % filename)
    debug_print("KiCad Schematic Library filename is %s." % lib_table_filename)

    symbol_lib_table = LibTable().from_file(lib_table_filename)
    schematic = Schematic().from_file(filename)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Schematic"

        choices = list()

        choice = user_selection(msg, choices)

        match choice:
            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
            case "Exit":
                debug_print("User selected Exit.")

                schematic.to_file(new_filename)
                symbol_lib_table.to_file(new_lib_table_filename)

                msgbox(msg="KiCad Input file " + filename
                           + " (and its Library table) have been processed.\n\r \n\rProcessed files are "
                           + new_filename + " and " + new_lib_table_filename + ".",
                       title="KiCad Schematic file (and Library Table)",
                       ok_button="Program will now close")
            case other:
                debug_print("User selected illegal option (%s)!" % choice)
