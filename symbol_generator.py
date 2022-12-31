#  ===================================================================
#  Source File Name : symbol_generator.py
#  Purpose          : Does the hard work to generate the symbol (from a board)
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import math
from kiutils.items.syitems import SyRect, SyFill
# from kiutils.board import *
from kiutils.symbol import Symbol, SymbolPin

# from debug_print import *
# from user_display_footprint import *
# from Supplemental_Classes import *
from Data_Mover import *


# import datetime


# ==================================================================================================================
def init_symlibtable(odir, name):
    symbol_lib          = LibTable()

    symbol_lib.type     = "sym_lib_table"
    symbol_lib.libs     = []
    symbol_lib.filePath = ""

    symbol_lib.libs.append(Library(name        = "MyGen",
                                   type        = "KiCad",
                                   uri         = odir + name + ".kicad_sym",
                                   options     = "",
                                   description = "Created by MyGen"))

    return symbol_lib


# ==================================================================================================================
# Need to check that output library exist and if not create it.
def manage_schematic_lib_dir(odir, name):
    libtablename = odir + "sym-lib-table"

    if os.path.exists(libtablename):
        symlibtable = LibTable().from_file(libtablename)

        symlibtable_not_found = True

        # if there are any libraries then check if the one we are processing is there or not
        if len(symlibtable.libs) > 0:
            for loop, lib in enumerate(symlibtable.libs):
                if lib.name == name:
                    symlibtable_not_found = False

        if symlibtable_not_found:
            symlibtable.libs.append(Library(name        = name,
                                            type        = "KiCad",
                                            uri         = odir + name + ".kicad_sym",
                                            options     = "",
                                            description = "Created by MyGen"))

    else:  # no file, so create one
        symlibtable = init_symlibtable(odir, name)

    symlibtable.to_file(libtablename)


# ==================================================================================================================
# Generate the symbol from the previously selected components
def generate_symbol(name, components):
    symbol = Symbol()

    # Grid used to scale the symbol
    grid = 1.27

    # Som useful attribute information
    origin              = Position(X     = 0,
                                   Y     = 0,
                                   angle = 0)

    reference_position  = Position(X     = (grid * 2) * 3,
                                   Y     = 0,
                                   angle = 90)

    value_position      = Position(X     = (grid * 2) * 4,
                                   Y     = 0,
                                   angle = 90)

    myfont              = Font(height = grid,
                               width  = grid)

    myeffect            = Effects(font = myfont,
                                  hide = False)

    myeffect_hide       = Effects(font    = myfont,
                                  hide    = True)

    mycolor             = ColorRGBA(R = 0,
                                    G = 0,
                                    B = 0,
                                    A = 0)

    mystroke            = Stroke(width = 0.1524,
                                 type  = "default",
                                 color = mycolor)

    myfill = SyFill(type = "none")

    # Generate the basic symbol
    symbol.id             = name
    symbol.extends        = None
    symbol.hidePinNumbers = True  # Don't need to see these as the pin # and the pin name are the same.
    symbol.pinNames       = False
    symbol.pinNamesHide   = False
    symbol.pinNamesOffset = None
    symbol.inBom          = "no"
    symbol.onBoard        = "yes"
    symbol.isPower        = False
    symbol.properties     = []
    symbol.graphicItems   = []
    symbol.pins           = []
    symbol.units          = []

    # Create the basic information about the symbol
    symbol.properties.append(Property(key      = "Reference",
                                      value    = "Brd",
                                      id       = 0,
                                      position = reference_position,
                                      effects  = myeffect))

    symbol.properties.append(Property(key      = "Value",
                                      value    = name,
                                      id       = 1,
                                      position = value_position,
                                      effects  = myeffect))

    symbol.properties.append(Property(key      = "Footprint",
                                      value    = "MyGen:" + name,
                                      id       = 2,
                                      position = origin,
                                      effects  = myeffect_hide))

    symbol.properties.append(Property(key      = "DataSheet",
                                      value    = "",
                                      id       = 3,
                                      position = origin,
                                      effects  = myeffect_hide))

    symbol.properties.append(Property(key      = "ki_locked",
                                      value    = "",
                                      id       = 4,
                                      position = origin,
                                      effects  = myeffect))

    for loop, component in enumerate(components.component_data.components):
        # create one unit per selected component
        unit = Symbol(id           = name + "_" + str(loop + 1) + "_1",
                      graphicItems = [],
                      pins         = [])

        # menu data has the list of reference designators, but component_data.pads has the list of pads fo need to count the number that match
        # count occurrences of component in pads and collect the pin data.
        pin_data = []

        pin_count = 0

        for count, data in enumerate(components.component_data.pads):
            # Need to include the "-" in the match otherwise x1 finds x1 and x11, 12, etc.
            if data.number[0:len(component) + 1] == component + "-":
                pin_count = pin_count + 1

                pin_data.append(data.number)

        # Add a body based on the number of pins
        width     = (grid * 8) / 2
        pin_width = grid * 2
        height    = ((grid * (pin_count - 1) * 2) + (grid * 2)) / 2

        pin_origin = height - grid

        unit.graphicItems.append(SyRect(start  = WksPosition(X = 0 - width,
                                                             Y = 0 - height),
                                        end    = WksPosition(X = width,
                                                             Y = height),
                                        stroke = mystroke,
                                        fill   = myfill))

        # Now add the pin(s)
        for sequence, pin in enumerate(pin_data):
            unit.pins.append(SymbolPin(electricalType = "bidirectional",
                                       graphicalStyle = "line",
                                       position       = Position(X     = 0 - (width + pin_width),
                                                                 Y     = pin_origin - (sequence * (2 * grid)),
                                                                 angle = 0),
                                       length         = pin_width,
                                       name           = pin,
                                       nameEffects    = myeffect,
                                       number         = pin,
                                       numberEffects  = myeffect))

        symbol.units.append(unit)

    return symbol


# ==================================================================================================================
def generate_symbolfile(odir, name, symbol):
    symlib = SymbolLib()

    symlib.version   = "20211014"
    symlib.generator = "kicad_symbol_editor"
    symlib.symbols   = []
    symlib.symbols.append(symbol)
    symlib.filePath  = None

    symlib.to_file(odir + name + ".kicad_sym")

    return symbol
