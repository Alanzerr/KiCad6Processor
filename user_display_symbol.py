#  ===================================================================
#  Source File Name : user_display_footprint.py
#  Purpose          : Footprint specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_symbolpin(symbolpin, printout=False):
    output_text: list[str] = [print_data("syms/sym/pin/elec: ", symbolpin.electricalType),
                              print_data("syms/sym/pin/grap: ", symbolpin.graphicalStyle),
                              print_data("syms/sym/pin/pos : ", symbolpin.position),
                              print_data("syms/sym/pin/len : ", symbolpin.length),
                              print_data("syms/sym/pin/nam : ", symbolpin.name),
                              print_data("syms/sym/pin/namE: ", symbolpin.nameEffects),
                              print_data("syms/sym/pin/num : ", symbolpin.number),
                              print_data("syms/sym/pin/numE: ", symbolpin.numberEffects),
                              print_data("syms/sym/pin/hide: ", symbolpin.hide)]

    output_text.extend(print_alternatepin(symbolpin.alternatePins))

    if printout:
        textbox("Details for Symbol Pin ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_symbols(symbolname, symbols, printout=False):
    output_text: list[str] = [print_data("syms/version     : ", symbols.version, True),
                              print_data("syms/generator   : ", symbols.generator, True)]

    output_text.extend(print_symbol(symbols.symbols))

    output_text.extend(print_data("syms/filePath    : ", symbols.filePath, True))

    if printout:
        textbox("Details for Symbols " + symbolname, "Symbols", output_text, False)
        return ""
    else:
        return output_text
