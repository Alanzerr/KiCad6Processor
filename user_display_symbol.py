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
def print_alternatepin(alternatepin, printout=False):
    output_text: list[str] = []

    for pin in alternatepin:
        output_text.append(merge_data(False, False, " syms/sym/Apin/Nam: ", pin.pinName))
        output_text.append(merge_data(False, False, " syms/sym/Apin/ele: ", pin.electricalType))
        output_text.append(merge_data(False, False, " syms/sym/Apin/gra: ", pin.graphicalStyle))

        for unit in pin.units:
            output_text.append(merge_data(False, False, " syms/sym/Apin/uni: ", unit))

    if printout:
        textbox("Details for Alternate Pin ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_symbolpin(symbolpin, printout=False):
    output_text: list[str] = [merge_data(False, False, " syms/sym/pin/elec: ", symbolpin.electricalType),
                              merge_data(False, False, " syms/sym/pin/grap: ", symbolpin.graphicalStyle),
                              merge_data(False, False, " syms/sym/pin/pos : ", symbolpin.position),
                              merge_data(False, False, " syms/sym/pin/len : ", symbolpin.length),
                              merge_data(False, False, " syms/sym/pin/nam : ", symbolpin.name),
                              merge_data(False, False, " syms/sym/pin/namE: ", symbolpin.nameEffects),
                              merge_data(False, False, " syms/sym/pin/num : ", symbolpin.number),
                              merge_data(False, False, " syms/sym/pin/numE: ", symbolpin.numberEffects),
                              merge_data(False, False, " syms/sym/pin/hide: ", symbolpin.hide)]

    output_text.extend(print_alternatepin(symbolpin.alternatePins))

    if printout:
        textbox("Details for Symbol Pin ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_symbol(symbols, printout=False):
    output_text: list[str] = []

    for symbol in symbols:
        output_text.append(merge_data(False, False, " syms/sym/id      : ", symbol.id))
        output_text.append(merge_data(True,  False, "*syms/sym/extends : ", symbol.extends))
        output_text.append(merge_data(False, False, " syms/sym/hidPinNo: ", symbol.hidePinNumbers))
        output_text.append(merge_data(False, False, " syms/sym/pinNames: ", symbol.pinNames))
        output_text.append(merge_data(False, False, " syms/sym/pinNaHid: ", symbol.pinNamesHide))
        output_text.append(merge_data(True,  False, "*syms/sym/pinNaOff: ", symbol.pinNamesOffset))
        output_text.append(merge_data(True,  False, "*syms/sym/inBom   : ", symbol.inBom))
        output_text.append(merge_data(True,  False, "*syms/sym/onBoard : ", symbol.onBoard))
        output_text.append(merge_data(False, False, " syms/sym/isPower : ", symbol.isPower))

    #    properties: List[Property] = field(default_factory=list)

    #    graphicItems: List = field(default_factory=list)

        output_text.extend(print_alternatepin(symbol.pins))

    if printout:
        textbox("Details for Symbol ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_symbols(symbolname, symbols, printout=False):
    output_text: list[str] = [merge_data(True, False, "*syms/version     : ", symbols.version),
                              merge_data(True, False, "*syms/generator   : ", symbols.generator)]

    output_text.extend(print_symbol(symbols.symbols))

    output_text.append(merge_data(True,  False, "*syms/filePath    : ", symbols.filePath))

    if printout:
        textbox("Details for Symbols " + symbolname, "Symbols", output_text, False)
        return None
    else:
        return output_text
