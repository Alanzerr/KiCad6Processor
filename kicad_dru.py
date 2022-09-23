#  ===================================================================
#  Source File Name : kicad_dru.py
#  Purpose          : Process KiCad6 Design Rules (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
import os

from kiutils.dru import DesignRules

from debug_print import *


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
    # Do stuff ...
    designrules.to_file(new_filename)

    msgbox(msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
           title="KiCad Design Rules file",
           ok_button="Program will now close")
