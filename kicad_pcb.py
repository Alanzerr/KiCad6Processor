#  ===================================================================
#  Source File Name : kicad_pcb.py
#  Purpose          : Process KiCad6 PCB (and library table)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
import os

from kiutils.board import Board
from kiutils.libraries import LibTable

from debug_print import *


# ==================================================================================================================
def process_kicad_pcb(fdir, fname, fext):
    filename = fdir + fname + fext
    lib_table_filename = fdir + "fp-lib-table"

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + "\\" + sub_folder + "\\" + fname + fext
    new_lib_table_filename = fdir + "\\" + sub_folder + "\\" + "fp-lib-table"

    debug_print("KiCad PCB filename is %s." % filename)
    debug_print("KiCad PCB Library filename is %s." % lib_table_filename)

    pcb_lib_table = LibTable().from_file(lib_table_filename)
    board = Board().from_file(filename)
    # Do stuff ...
    board.to_file(new_filename)
    pcb_lib_table.to_file(new_lib_table_filename)

    msgbox(msg="KiCad Input file " + filename
               + " (and its library table) have been processed.\n\r \n\rProcessed files are "
               + new_filename + " and " + new_lib_table_filename + ".",
           title="KiCad PCB file (and Library Table)",
           ok_button="Program will now close")
