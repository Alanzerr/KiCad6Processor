from easygui import *
from kiutils.board import Board
from kiutils.schematic import Schematic
from kiutils.symbol import Symbol
from kiutils.footprint import Footprint
from kiutils.wks import WorkSheet
from kiutils.dru import DesignRules

# ==================================================================================================================
def process_kicad_pcb(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad PCB filename is %s." % filename)

    board = Board().from_file(filename)
    # Do stuff ...
    board.to_file(filename)

# ==================================================================================================================
def process_kicad_sch(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Schematics filename is %s." % filename)

    schematic = Schematic().from_file(filename)
    # Do stuff ...
    schematic.to_file(filename)

# ==================================================================================================================
def process_kicad_mod(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Footprint filename is %s." % filename)

    footprint = Footprint().from_file(fdir + filename)
    # Do stuff ...
    footprint.to_file(fdir + fname + fext)

# ==================================================================================================================
def process_kicad_sym(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Symbol filename is %s." % filename)

    symbol = Symbol().from_file(filename)
    # Do stuff ...
    symbol.to_file(filename)

# ==================================================================================================================
def process_kicad_wks(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Worksheet filename is %s." % filename)

    worksheet = WorkSheet().from_file(filename)
    # Do stuff ...
    worksheet.to_file(filename)

# ==================================================================================================================
def process_kicad_dru(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Design Rule filename is %s." % filename)

    designrules = DesignRules().from_file(filename)
    # Do stuff ...
    designrules.to_file(filename)

# ==================================================================================================================
def process_kicad_pro(fdir, fname, fext):
    filename = fdir + fname + fext
    print("KiCad Project filename is %s." % filename)

    # This is a special case as this is not supported by kiutils.

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

if Input_Filename is None:
    msgbox(msg="No KiCad Input file was selected!",
           title="Open file",
           ok_button="Program will now close")
else:
    # Direction is to the last "/"
    # Filename is from the last "/" to the last "."
    # Extension is from the last "." to the end of the string

    print("=== Input Filename is %s." % Input_Filename)

    Input_Directory = Input_Filename[0:Input_Filename.rfind("\\") + 1]
    Input_Filename_Extension = Input_Filename[Input_Filename.rfind("."):len(Input_Filename)]

    #print("Start is %i." % Input_Filename.rfind("\\"))
    #print("Mid is %i." % Input_Filename.rfind("."))
    #print("Length is %i." % len(Input_Filename))
    print("=== Input Directory is |%s|." % Input_Directory)
    print("=== Input Filename Extensions is |%s|." % Input_Filename_Extension)

    Input_Filename = Input_Filename[Input_Filename.rfind("\\") + 1:Input_Filename.rfind(".")]
    print("=== Input Filename is |%s|." % Input_Filename)

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
        case other:
            msgbox(msg="KiCad Input file extension was not recognised!",
                   title="Open file",
                   ok_button="Program will now close")
