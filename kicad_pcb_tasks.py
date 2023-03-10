#  ===================================================================
#  Source File Name : kicad_pcb_tasks.py
#  Purpose          : Tasks for kicad_pcb
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================
from kiutils.symbol import *

# import os
# import math
# import datetime
# from Supplemental_Classes import *
from footprint_generator import *

# from kiutils.board import *
# from kiutils.footprint import *
# from kiutils.libraries import *

from debug_print import *
from symbol_generator import *
from user_display_board import *
from user_display_libtable import *
from user_display_footprint import *


# ==================================================================================================================
def pcb_task1(user_choice, filename, board):
    debug_print("User selected %s." % user_choice)

    print_board(filename, board, True)


# ==================================================================================================================
def pcb_task2(user_choice, filename, pcb_lib_table):

    debug_print("User selected %s." % user_choice)

    if pcb_lib_table is not None:
        print_libtable(filename, pcb_lib_table, True)


# ==================================================================================================================
def pcb_task3(filename, board, odir):
    # analyse the input directory, file name and get the board name
    idir                     = filename[0:filename.rfind("\\")]

    boardname                = filename[0:filename.find(".kicad_pcb")]
    boardname                = boardname[boardname.rfind("\\") + 1:len(boardname)]

    user_selected_components = Components()

    if boardname is None:
        # Get name for new footprint
        footprintname = user_input(boardname)
    else:
        footprintname = boardname

    # Returns None is user cancels input selection.
    if footprintname is not None:
        # Depending on how the board was designed, there may be a need to flip it to get everything the right way up.
        user_selects_flip = ynbox(msg="Do you want to flip the board around?")

        # Multiplying the y coordinate by -1 flips it otherwise multiple by 1; this save having to have conditional code.
        if user_selects_flip:
            flip = True

            footprintname = footprintname + "_flipped"
        else:
            flip = False

        # set the basic attributes
        footprint = init_footprint(footprintname)

        # if odir is known then use it
        if odir is None:
            # Need to get the location to save the output files.
            savedirectory = diropenbox(msg     = "Project Location",
                                       title   = "KiCad Output",
                                       default = odir)  # os.getcwd())
        else:
            savedirectory = odir

        data_input = open(os.getcwd() + "\\" + "MyGen_" + boardname + ".kicad_input", "w")
        data_input.write(filename + "\n")
        data_input.write(odir)
        data_input.close()

        # Want to determine the offset so that we can draw the outline centered on 0,0
        outline_data = find_centroid(board.graphicalItems)

        # copy board outline to footprint outline
        outline = create_outline(board.graphicalItems, outline_data, flip)

        # Prep the data before we use it
        graphicsdata = []

        # commented this out as a temporary measure.
        # growdata1 = grow_items(outline.board_edge, 1.27, "F.SilkS")  # Outline
        # growdata2 = grow_items(outline.board_edge, 2.54, "F.CrtYd")  # Courtyard

        graphicsdata.extend(outline.board_edge)  # Outline
        # commented this out as a temporary measure.
        # graphicsdata.extend(growdata1)           # Silkscreen
        # graphicsdata.extend(growdata2)           # Courtyard

        # We want the non-edge data on another layer so change it and then add it
        # This is not exactly useful in most cases but could all drill holes and slots to be easily added (by hand)
        for item in outline.non_board_edge:
            item.layer = "Margin"

            graphicsdata.append(item)

        footprint.graphicItems = graphicsdata

        # And add the text primitives - need to add these here as create_outline initialises footprint.graphicItems!
        myfont = Font(thickness=0.15)

        myjustify = Justify()

        myeffect = Effects(font    = myfont,
                           justify = myjustify)

        reference = FpText(type     = "reference",
                           text     = "R**",
                           layer    = "F.SilkS",
                           effects  = myeffect,
                           position = Position(X = 0,
                                               Y = 0))

        footprint.graphicItems.append(reference)

        value = FpText(type     = "value",
                       text     = footprintname,
                       layer    = "F.Fab",
                       effects  = myeffect,
                       position = Position(X = 0,
                                           Y = 1))

        footprint.graphicItems.append(value)

        user = FpText(type     = "user",
                      text     = "${REFERENCE}",
                      layer    = "F.Fab",
                      effects  = myeffect,
                      position = Position(X = 0,
                                          Y = -1))

        footprint.graphicItems.append(user)

        # request the connectors to use as IO
        user_selected_components.menu_data = select_connectors(board.footprints, flip)

        if user_selected_components.menu_data is not None:
            # Need to do some housekeeping in terms of possible output directories
            manage_layout_lib_dir(savedirectory)

            # Now figure out the required parameters related to the selected components
            user_selected_components.component_data = add_component_data(board.footprints, user_selected_components.menu_data, outline_data.centroid, flip)

            footprint.pads         = user_selected_components.component_data.pads
            footprint.models       = user_selected_components.component_data.models

            # need to extend the graphics items as we're created the outline previously.
            footprint.graphicItems.extend(user_selected_components.component_data.graphicitems)

            # So we have the original data converted, just need to add the model of the original board.
            # first look to see if we can fine the step file as KiCad puts it in a known default position
            if path.exists(idir + "\\" + boardname + ".step"):
                board_file = idir + "\\" + boardname + ".step"

            elif path.exists(idir + "\\" + boardname + ".stp"):
                board_file = idir + "\\" + boardname + ".stp"

            else:
                # Import the file to be processed - only shows KiCad files.
                board_file = fileopenbox(msg       = "Open file",
                                         title     = "KiCad 3D Model File",
                                         default   = odir + "\\*.*",
                                         filetypes = [["*.step", "KiCad 3D Board file"],
                                                      ["*.stp",  "KiCad 3D Board file"]],
                                         multiple  = False)

            # This should get the model of the original board in approximately the right place.
            if board_file is not None:
                if flip:
                    new_model = Model(path  = board_file,
                                      pos   = Coordinate(X = 0.0,
                                                         Y = 0.0,
                                                         Z = 12.50),
                                      scale = Coordinate(X = 1.0,
                                                         Y = 1.0,
                                                         Z = 1.0),
                                      rotate= Coordinate(X = 0.0,
                                                         Y = 180.0,
                                                         Z = -180.0))
                else:
                    new_model = Model(path  = board_file,
                                      pos   = Coordinate(X = 0.0,
                                                         Y = 0.0,
                                                         Z = 10.50),
                                      scale = Coordinate(X = 1.0,
                                                         Y = 1.0,
                                                         Z = 1.0),
                                      rotate= Coordinate(X = 0.0,
                                                         Y = 0.0,
                                                         Z = 0.0))

                footprint.models.append(new_model)

            # print_footprint(footprintname, footprint, True)

            # Now save the output file
            modfilename = savedirectory + "MyGen.Pretty" + "\\" + footprintname + ".kicad_mod"
            footprint.to_file(modfilename)

            # Done the layout part so now do the schematic part - first up is to create/manage the sym-lib-table to include the library
            manage_schematic_lib_dir(savedirectory, footprintname)

            symbol = generate_symbol(footprintname, user_selected_components)

            generate_symbolfile(savedirectory, footprintname, symbol)

            msgbox(msg      = "KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed files are " + modfilename + " and " + savedirectory
                              + footprintname + ".kicad_sym.",
                   title    = "KiCad Footprint file",
                   ok_button= "Continue")

        else:
            msgbox(msg      = "KiCad Input file " + filename + " has not been processed.\n\r \n\rNo components were selected!",
                   title    = "KiCad Footprint file",
                   ok_button= "Continue")


# ==================================================================================================================
def pcb_task4(user_choice, board, board_filename, new_board_filename, lib_table, new_lib_table_filename):
    debug_print("User selected %s." % user_choice)

    board.to_file(new_board_filename)
    if lib_table is not None:
        lib_table.to_file(new_lib_table_filename)

    msgbox(msg="KiCad Input file " + board_filename + " (and its library table) have been processed.\n\r \n\rProcessed files are "
               + new_board_filename + " and " + new_lib_table_filename + ".",
           title="KiCad PCB file (and Library Table)",
           ok_button="Exit function")
