from easygui import *
from kiutils.board import Board
from kiutils.schematic import Schematic
from kiutils.symbol import Symbol
from kiutils.footprint import Footprint
from kiutils.wks import WorkSheet
from kiutils.dru import DesignRules
from kiutils.libraries import LibTable

# ==================================================================================================================
def process_kicad_pcb(fdir, fname, fext):
    Filename = fdir + fname + fext
    LibTable_Filename = fdir + "fp-lib-table"

    New_Filename = fdir + fname + "_Modified" + fext
    New_LibTable_Filename = fdir + "fp-lib-table" + "_Modified"

    print("KiCad PCB filename is %s." % Filename)
    print("KiCad PCB Library filename is %s." % LibTable_Filename)

    PCB_LibTable = LibTable().from_file(LibTable_Filename)
    board = Board().from_file(Filename)
    # Do stuff ...
    board.to_file(New_Filename)
    PCB_LibTable.to_file(New_LibTable_Filename)

# ==================================================================================================================
def process_kicad_sch(fdir, fname, fext):
    Filename = fdir + fname + fext
    LibTable_Filename = fdir + "sym-lib-table"

    New_Filename = fdir + fname + "_Modified" + fext
    New_LibTable_Filename = fdir + "sym-lib-table" + "_Modified"

    print("KiCad Schematics filename is %s." % Filename)
    print("KiCad Schematic Library filename is %s." % LibTable_Filename)

    Symbol_LibTable = LibTable().from_file(LibTable_Filename)
    schematic = Schematic().from_file(Filename)
    # Do stuff ...
    schematic.to_file(New_Filename)
    Symbol_LibTable.to_file(New_LibTable_Filename)

# ==================================================================================================================
def process_kicad_mod(fdir, fname, fext):
    Filename = fdir + fname + fext

    New_Filename = fdir + fname + "_Modified" + fext

    print("KiCad Footprint filename is %s." % Filename)

    footprint = Footprint().from_file(Filename)
    # Do stuff ...
    footprint.to_file(New_Filename)

# ==================================================================================================================
def process_kicad_sym(fdir, fname, fext):
    Filename = fdir + fname + fext

    New_Filename = fdir + fname + "_Modified" + fext

    print("KiCad Symbol filename is %s." % Filename)

    # This is a special case as this does not appear to be supported by kiutils.

# ==================================================================================================================
def process_kicad_wks(fdir, fname, fext):
    Filename = fdir + fname + fext

    New_Filename = fdir + fname + "_Modified" + fext

    print("KiCad Worksheet filename is %s." % Filename)

    worksheet = WorkSheet().from_file(Filename)
    # Do stuff ...
    worksheet.to_file(New_Filename)

# ==================================================================================================================
def process_kicad_dru(fdir, fname, fext):
    Filename = fdir + fname + fext

    New_Filename = fdir + fname + "_Modified" + fext

    print("KiCad Design Rule filename is %s." % Filename)

    designrules = DesignRules().from_file(Filename)
    # Do stuff ...
    designrules.to_file(New_Filename)

# ==================================================================================================================
def process_kicad_pro(fdir, fname, fext):
    Filename = fdir + fname + fext

    New_Filename = fdir + fname + "_Modified" + fext

    print("KiCad Project filename is %s." % Filename)

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
