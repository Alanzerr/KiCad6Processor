from easygui import *
from kiutils.board import Board

Filename = fileopenbox(msg="Open file", title="KiCad Input File", filetypes="*.kicad_pcb", multiple=False)

if Filename is None:
    msgbox(msg="No KiCad Inout file was selected!", title="Open file", ok_button="Program will now close")
else:
   board = Board().from_file(Filename)

   # Do stuff ...

   board.to_file(Filename)

