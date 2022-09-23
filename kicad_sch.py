#  ===================================================================
#  Source File Name : kicad_sch.py
#  Purpose          : Process KiCad6 Schematics (and library table)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.schematic import Schematic
from kiutils.libraries import LibTable


# ==================================================================================================================
def process_kicad_sch(fdir, fname, fext):
    filename = fdir + fname + fext
    lib_table_filename = fdir + "sym-lib-table"

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + "\\" + sub_folder + "\\" + fname + fext
    new_lib_table_filename = fdir + "\\" + sub_folder + "\\" + "sym-lib-table"

    print("KiCad Schematics filename is %s." % filename)
    print("KiCad Schematic Library filename is %s." % lib_table_filename)

    symbol_lib_table = LibTable().from_file(lib_table_filename)
    schematic = Schematic().from_file(filename)
    # Do stuff ...
    schematic.to_file(new_filename)
    symbol_lib_table.to_file(new_lib_table_filename)
