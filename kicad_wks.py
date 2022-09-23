#  ===================================================================
#  Source File Name : kicad_wks.py
#  Purpose          : Process KiCad6 Worksheets (for PCB and Schematics).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.wks import WorkSheet


# ==================================================================================================================
def process_kicad_wks(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + "\\" + sub_folder + "\\" + fname + fext

    print("KiCad Worksheet filename is %s." % filename)

    worksheet = WorkSheet().from_file(filename)
    # Do stuff ...
    worksheet.to_file(new_filename)
