#  ===================================================================
#  Source File Name : *.py
#  Purpose          : t.b.a.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
# Could use tkinter however whilst it will be prettier, its much more complex!
import tkinter as tk
import os

from debug_print import *

# PCB related stuff
from kiutils.board import Board
from kiutils.footprint import Footprint

# Schematic related stuff
from kiutils.schematic import Schematic
from kiutils.symbol import SymbolLib

# PCB and Schmatic Libraries
from kiutils.libraries import LibTable

# Misc
from kiutils.wks import WorkSheet
from kiutils.dru import DesignRules

from kicad_pcb import *
from kicad_sch import *
from kicad_mod import *
from kicad_sym import *
from kicad_wks import *
from kicad_dru import *
from kicad_pro import *

# Import the file to be processed - only shows KiCad files.
Input_Filename = fileopenbox(msg="Open file",
                             title="KiCad Input File",
                             filetypes=[["*.kicad_pro", "KiCad Project file"],
                                        ["*.kicad_pcb", "KiCad Board file"],
                                        ["*.kicad_sch", "KiCad Schematic file"],
                                        ["*.kicad_mod", "KiCad Footprint file"],
                                        ["*.kicad_sym", "KiCad Symbol file"],
                                        ["*.kicad_wks", "KiCad Worksheet file"],
                                        ["*.kicad_dru", "KiCad Design Rules file"]],
                             multiple=False)

# Input_filename is none if "cancel is selected"!
if Input_Filename is None:
    msgbox(msg="No KiCad Input file was selected!",
           title="Open file",
           ok_button="Program will now close")
# Got a file so split it into bits.
else:
    # Direction is to the last "/"
    # Filename is from the last "/" to the last "."
    # Extension is from the last "." to the end of the string

    debug_print("Full Input Filename is |%s|." % Input_Filename)

    Input_Directory = Input_Filename[0:Input_Filename.rfind("\\") + 1]
    Input_Filename_Extension = Input_Filename[Input_Filename.rfind("."):len(Input_Filename)]

    debug_print("Input Directory is \"%s\"." % Input_Directory)
    debug_print("Input Filename Extensions is \"%s\"." % Input_Filename_Extension)

    Input_Filename = Input_Filename[Input_Filename.rfind("\\") + 1:Input_Filename.rfind(".")]
    debug_print("Input Filename is \"%s\"." % Input_Filename)

    # Process it based on it's extension/type.
    match Input_Filename_Extension:
        case ".kicad_pcb":
            process_kicad_pcb(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_sch":
            process_kicad_sch(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_mod":
            process_kicad_mod(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_sym":
            process_kicad_sym(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_wks":
            process_kicad_wks(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_dru":
            process_kicad_dru(Input_Directory, Input_Filename, Input_Filename_Extension)
        case ".kicad_pro":
            process_kicad_pro(Input_Directory, Input_Filename, Input_Filename_Extension)
        # Just in case the user selects a non-KiCad file
        case other:
            msgbox(msg="KiCad Input file extension was not recognised!",
                   title="Open file",
                   ok_button="Program will now close")
