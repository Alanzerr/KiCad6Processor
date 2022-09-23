#  ===================================================================
#  Source File Name : kicad_mod.py
#  Purpose          : Process KiCad6 Footprints (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.footprint import Footprint

# ==================================================================================================================
def process_kicad_mod(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + "\\" + sub_folder + "\\" + fname + fext

    print("KiCad Footprint filename is %s." % filename)

    footprint = Footprint().from_file(filename)
    # Do stuff ...
    footprint.to_file(new_filename)
