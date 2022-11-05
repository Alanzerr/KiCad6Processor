#  ===================================================================
#  Source File Name : user_display_footprint.py
#  Purpose          : Footprint specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import tkinter as tk
# import os

from user_display import *


# ==================================================================================================================
def print_attributes(attributes, printout=False):
    output_text: list[str] = [print_data("attr/type        : ", attributes.type),
                              print_data("attr/boardOnly   : ", attributes.boardOnly),
                              print_data("attr/exclPosFiles: ", attributes.excludeFromPosFiles),
                              print_data("attr/exclFromBom : ", attributes.excludeFromBom)]

    if printout:
        textbox("Details for Attributes ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_pads(pads, printout=False):
    output_text: list[str] = []

    loop = 0

    for pad in pads:
        output_text.extend("\n pad              : " + str(loop + 1))
        output_text.extend(print_data("pad/number       : ", pad.number))
        output_text.extend(print_data("pad/type         : ", pad.type))
        output_text.extend(print_data("pad/shape        : ", pad.shape))
        output_text.extend(print_data("pad/Position     : ", pad.position))
        output_text.extend(print_data("pad/locked       : ", pad.locked))
        output_text.extend(print_data("pad/size         : ", pad.size, True))

        if not(pad.drill is None):
            output_text.extend(print_data("pad/drill/oval   : ", pad.drill.oval, True))
            output_text.extend(print_data("pad/drill/dia    : ", pad.drill.diameter, True))
            output_text.extend(print_data("pad/drill/width  : ", pad.drill.width, True))
            output_text.extend(print_data("pad/drill/offset : ", pad.drill.offset, True))

        loop2 = 1

        for layer in pad.layers:
            output_text.extend(print_data("pad/layers    " + format(loop2, ' 4d') + " : ", layer))
            loop2 += 1

        output_text.extend(print_property("pad/prope", pad.property))
        output_text.extend(print_data("pad/remUnuseLayer: ", pad.removeUnusedLayers))
        output_text.extend(print_data("pad/keepEndLayer : ", pad.keepEndLayers))
        output_text.extend(print_data("pad/rndrectRatio : ", pad.roundrectRatio, True))
        output_text.extend(print_data("pad/chamferRatio : ", pad.chamferRatio, True))

        loop2 = 1

        for chamfer in pad.chamfer:
            output_text.extend(print_data("pad/chamfer " + format(loop2, ' 4d') + " : ", chamfer))
            loop2 += 1

        if not (pad.net is None):
            output_text.extend(print_data("pad/net/number   : ", pad.net.number))
            output_text.extend(print_data("pad/net/name     : ", pad.net.name))

        output_text.extend(print_data("pad/tstamp       : ", pad.tstamp, True))
        output_text.extend(print_data("pad/pinFunction  : ", pad.pinFunction, True))
        output_text.extend(print_data("pad/pinType      : ", pad.pinType, True))
        output_text.extend(print_data("pad/dieLength    : ", pad.dieLength, True))
        output_text.extend(print_data("pad/sldrMskMargin: ", pad.solderMaskMargin, True))
        output_text.extend(print_data("pad/sldrPstMargin: ", pad.solderPasteMargin, True))
        output_text.extend(print_data("pad/sldrPstMargRa: ", pad.solderPasteMarginRatio, True))
        output_text.extend(print_data("pad/clearance    : ", pad.clearance, True))
        output_text.extend(print_data("pad/zoneConnect  : ", pad.zoneConnect, True))
        output_text.extend(print_data("pad/thermalWidth : ", pad.thermalWidth, True))
        output_text.extend(print_data("pad/thermalGap   : ", pad.thermalGap, True))

        if not (pad.customPadOptions is None):
            output_text.extend(print_data("pad/custPad/clear : ", pad.customPadOptions.clearance, True))
            output_text.extend(print_data("pad/custPad/anchor: ", pad.customPadOptions.anchor, True))

        loop2 = 1

        for customPadPrimitive in pad.customPadPrimitives:
            output_text.extend(print_data("pad/Prims   " + format(loop2, ' 4d') + " : ", customPadPrimitive))
            loop2 += 1

        loop += 1

    if printout:
        textbox("Details for Pads ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_models(models, printout=False):
    output_text: list[str] = []

    loop = 0

    for model in models:
        output_text.extend(print_data("models/path      : ", model.path))
        output_text.extend(print_data("models/pos       : ", model.pos))
        output_text.extend(print_data("models/scale     : ", model.scale))
        output_text.extend(print_data("models/rotate    : ", model.rotate))

        loop += 1

    if printout:
        textbox("Details for Models ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_footprint(footprintname, footprint, printout=False):
    output_text: list[str] = [print_data("LibraryLink      : ", footprint.libraryLink, False, True),
                              print_data("version          : ", footprint.version, True),
                              print_data("generator        : ", footprint.generator, True),
                              print_data("locked           : ", footprint.locked),
                              print_data("placed           : ", footprint.placed),
                              print_data("layer            : ", footprint.layer),
                              print_data("tedit            : ", footprint.tedit),
                              print_data("tstamp           : ", footprint.tstamp, True),
                              print_data("position         : ", footprint.position, True),
                              print_data("description      : ", footprint.description, True),
                              print_data("tags             : ", footprint.tags, True)]

    output_text.extend(print_properties("FProp", footprint.properties))

    output_text.extend(print_data("path             : ", footprint.path, True))
    output_text.extend(print_data("autoplaceCost90  : ", footprint.autoplaceCost90, True))
    output_text.extend(print_data("autoplaceCost180 : ", footprint.autoplaceCost180, True))
    output_text.extend(print_data("solderMaskMargin : ", footprint.solderMaskMargin, True))
    output_text.extend(print_data("solderPasteMargin: ", footprint.solderPasteMargin, True))
    output_text.extend(print_data("solderPasteRatio : ", footprint.solderPasteRatio, True))
    output_text.extend(print_data("clearance        : ", footprint.clearance, True))
    output_text.extend(print_data("zoneConnect      : ", footprint.zoneConnect, True))
    output_text.extend(print_data("thermalWidth     : ", footprint.thermalWidth, True))
    output_text.extend(print_data("thermalGap       : ", footprint.thermalGap, True))

    output_text.extend(print_attributes(footprint.attributes))
    output_text.extend(print_fgraphicitems(footprint.graphicItems))
    output_text.extend(print_pads(footprint.pads))
    output_text.extend(print_zones("FZone", footprint.zones))
    output_text.extend(print_groups("FGroup", footprint.groups))
    output_text.extend(print_models(footprint.models))

    output_text.extend(print_data("filePath         ; ", footprint.filePath, True))

    if printout:
        textbox("Details for Footprint " + footprintname, "Footprint", output_text, False)
        return ""
    else:
        return output_text
