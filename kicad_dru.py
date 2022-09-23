#  ===================================================================
#  Source File Name : kicad_dru.py
#  Purpose          : Process KiCad6 Design Rules (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.dru import DesignRules


# ==================================================================================================================
def process_kicad_dru(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + "\\" + sub_folder + "\\" + fname + fext

    print("KiCad Design Rule filename is %s." % filename)

    designrules = DesignRules().from_file(filename)
    # Do stuff ...
    designrules.to_file(new_filename)
