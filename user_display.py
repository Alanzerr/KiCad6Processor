#  ===================================================================
#  Source File Name : user_display.py
#  Purpose          : Common display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
# import tkinter as tk
# import os

from kiutils.footprint import *
from kiutils.items.common import *
from kiutils.items.zones import *
from kiutils.items.fpitems import *


# ==================================================================================================================
def user_input():
    reply: str = enterbox(msg="Enter the name of the footprint to be created",
                          title="KiCad Footprint Creator",
                          default="Default",
                          strip=True)

    # If user presses cancel, then we set the reply to "Default" which is the same as pressing OK with no text!
    if reply is None:
        reply = "Default"

    return reply


# ==================================================================================================================
def user_selection(msg, selection):
    if not selection:
        # There is nothing to select (except exit). Need to do this as choicebox does not operate with 1 entry!
        display_msg = "Exit (and save output)? \n\r \n\rNOTE: Select \"Cancel\" to quit (without saving)."
        display_title = msg + " action(s)"

        # Swapped Cancel/OK round to make it consistent with choicebox
        choice = ccbox(msg=display_msg,
                       title=display_title,
                       choices=("Cancel", "Ok"))

        # if choice is None then selected cancel (which is effectively quit)
        if not choice:
            # Finished selecting tasks.
            return "Exit"
        else:
            # Do nothing.
            return "Quit"

    else:
        # There are thing to select!
        display_msg = "What " + msg + " related task do you want to perform? \n\r \n\rNOTE: Select \"Cancel\" to quit (" \
                                      "without saving)."
        display_title = msg + " action(s)"

        display_selection = selection.copy()

        position = 0

        for entry in display_selection:
            display_selection[position] = "Task " + str(position + 1) + ": " + entry
            position += 1

        display_selection.append("Task " + str(position + 1) + ": Exit")

        choice = choicebox(display_msg, display_title, display_selection)

        # if choice is None then selected cancel (which is effectively quit)
        if choice is None:
            # Do nothing.
            return "Quit"

        # Last entry
        elif choice[5:choice.find(":")] == str(len(display_selection)):
            # Finished selecting tasks.
            return "Exit"
        else:
            # Return User selection
            return choice[0:choice.find(":")]


# ==================================================================================================================
def merge_data(optional, newline, prefix, data):
    if isinstance(data, int):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == 0):
            return ""
        else:
            if newline:
                return prefix + str(data)
            else:
                return "\n" + prefix + str(data)

    elif isinstance(data, float):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == 0.0):
            return ""
        else:
            if newline:
                return prefix + str(data)
            else:
                return "\n" + prefix + str(data)

    elif isinstance(data, str):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == ""):
            return ""
        else:
            if newline:
                if len(data) > 40:
                    return prefix + data[0:39] + "..."
                else:
                    return prefix + data
            else:
                if len(data) > 40:
                    return "\n" + prefix + data[0:39] + "..."
                else:
                    return "\n" + prefix + data

    elif isinstance(data, Position):
        if newline:
            if data.angle is None:
                return prefix + str(data.X) + "," + str(data.Y) + " 0 " +  str(data.unlocked)
            else:
                return prefix + str(data.X) + "," + str(data.Y) + " " + str(data.angle) + " " + str(data.unlocked)
        else:
            if data.angle is None:
                return "\n" + prefix + str(data.X) + "," + str(data.Y) + " 0 " + str(data.unlocked)
            else:
                return "\n" + prefix + str(data.X) + "," + str(data.Y) + " " + str(data.angle) + " " + str(data.unlocked)

    elif isinstance(data, Zone):
        return "\n" + prefix + "Zone"

    elif isinstance(data, Group):
        return "\n" + prefix + "Group"

    elif isinstance(data, Model):
        return "\n" + prefix + "Model"

    elif isinstance(data, Dict):
        return "\n" + prefix + "Dict"

    elif isinstance(data, Coordinate):
        if newline:
            return prefix + str(data.X) + "," + str(data.Y) + "," + str(data.Z)
        else:
            return "\n" + prefix + str(data.X) + "," + str(data.Y) + "," + str(data.Z)

    elif data is None:
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data is None):
            return ""
        else:
            if newline:
                return prefix + str(data)
            else:
                return "\n" + prefix + str(data)

    else:
        return "\n" + prefix + str(type(data))


# ==================================================================================================================
def print_properties(properties, printout=False):
    output_text: list[str] = []

    loop = 0

    for propertie in properties:
        output_text.append(merge_data(False, False, " properties/key   : ", propertie.key))
        output_text.append(merge_data(False, False, " properties/value : ", propertie.value))
        loop += 1

    if printout:
        textbox("Details for Properties ", output_text, False)
        return None
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_attributes(attributes, printout=False):
    output_text: list[str] = [merge_data(False, False, " attr/type        : ", attributes.type),
                              merge_data(False, False, " attr/boardOnly   : ", attributes.boardOnly),
                              merge_data(False, False, " attr/exclPosFiles: ", attributes.excludeFromPosFiles),
                              merge_data(False, False, " attr/exclFromBom : ", attributes.excludeFromBom)]

    if printout:
        textbox("Details for Attributes ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fptext(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/text/type  : ", graphicitem.type),
                              merge_data(False, False, " gitem/text/text  : ", graphicitem.text),
                              merge_data(False, False, " gitem/text/pos   : ", graphicitem.position),
                              merge_data(False, False, " gitem/text/layer : ", graphicitem.layer),
                              merge_data(False, False, " gitem/text/hide  : ", graphicitem.hide),
                              merge_data(False, False, " gitem/text/effect: ", graphicitem.effects),
                              merge_data(True,  False, "*gitem/text/tstamp: ", graphicitem.tstamp)]

    if printout:
        textbox("Details for Footprint Text ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fpline(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/line/start : ", graphicitem.start),
                              merge_data(False, False, " gitem/line/end   : ", graphicitem.end),
                              merge_data(False, False, " gitem/line/layer : ", graphicitem.layer),
                              merge_data(True,  False, "*gitem/line/width : ", graphicitem.width),
                              merge_data(True,  False, "*gitem/line/stroke: ", graphicitem.stroke),
                              merge_data(False, False, " gitem/line/locked: ", graphicitem.locked),
                              merge_data(True,  False, "*gitem/line/tstamp: ", graphicitem.tstamp)]

    if printout:
        textbox("Details for Footprint Line ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fprect(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/rect/start : ", graphicitem.start),
                              merge_data(False, False, " gitem/rect/end   : ", graphicitem.end),
                              merge_data(False, False, " gitem/rect/layer : ", graphicitem.layer),
                              merge_data(True,  False, "*gitem/rect/width : ", graphicitem.width),
                              merge_data(True,  False, "*gitem/rect/stroke: ", graphicitem.stroke),
                              merge_data(True,  False, "*gitem/rect/fill  : ", graphicitem.fill),
                              merge_data(False, False, " gitem/rect/locked: ", graphicitem.locked),
                              merge_data(True,  False, "*gitem/rect/tstamp: ", graphicitem.tstamp)]

    if printout:
        textbox("Details for Footprint Rectangle ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fptextbox(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/tbox/locked: ", graphicitem.locked),
                              merge_data(False, False, " gitem/tbox/text  : ", graphicitem.text),
                              merge_data(False, False, " gitem/tbox/start : ", graphicitem.start),
                              merge_data(False, False, " gitem/tbox/end   : ", graphicitem.end)]

    for pts in graphicitem.pts:
        output_text.append(merge_data(False, False, " gitem/tbox/points : ", pts))

    output_text.append(merge_data(False, False, " gitem/tbox/angle : ", graphicitem.angle))
    output_text.append(merge_data(False, False, " gitem/tbox/layer : ", graphicitem.layer))
    output_text.append(merge_data(False, False, " gitem/tbox/tstamp: ", graphicitem.tstamp))
    output_text.append(merge_data(False, False, " gitem/tbox/effect: ", graphicitem.effects))
    output_text.append(merge_data(False, False, " gitem/tbox/stroke: ", graphicitem.stroke))
    output_text.append(merge_data(True,  False, "*gitem/tbox/rCache: ", graphicitem.renderCache))

    if printout:
        textbox("Details for Footprint Textbox ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fpcircle(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/circ/centre: ", graphicitem.center),
                              merge_data(False, False, " gitem/circ/end   : ", graphicitem.end),
                              merge_data(False, False, " gitem/circ/layer : ", graphicitem.layer),
                              merge_data(True,  False, "*gitem/circ/width : ", graphicitem.width),
                              merge_data(True,  False, "*gitem/circ/stroke: ", graphicitem.stroke),
                              merge_data(True,  False, "*gitem/circ/fill  : ", graphicitem.fill),
                              merge_data(False, False, " gitem/circ/locked: ", graphicitem.locked),
                              merge_data(True,  False, "*gitem/circ/tstamp: ", graphicitem.tstamp)]

    if printout:
        textbox("Details for Footprint Circle ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fparc(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/arc/start  : ", graphicitem.start),
                              merge_data(False, False, " gitem/arc/mid    : ", graphicitem.mid),
                              merge_data(False, False, " gitem/arc/end    : ", graphicitem.end),
                              merge_data(False, False, " gitem/arc/layer  : ", graphicitem.layer),
                              merge_data(True,  False, "*gitem/arc/width  : ", graphicitem.width),
                              merge_data(True,  False, "*gitem/arc/stroke : ", graphicitem.stroke),
                              merge_data(False, False, " gitem/arc/locked : ", graphicitem.locked),
                              merge_data(True,  False, "*gitem/arc/tstamp : ", graphicitem.tstamp)]

    if printout:
        textbox("Details for Footprint Arc ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fppoly(graphicitem, printout=False):
    output_text: list[str] = [merge_data(False, False, " gitem/poly/type  : ", graphicitem.layer)]

    for coord in graphicitem.coordinates:
        output_text.append(merge_data(False, False, " gitem/poly/type  : ", coord))

    output_text.append(merge_data(True,  False, "*gitem/poly/type  : ", graphicitem.width))
    output_text.append(merge_data(True,  False, "*gitem/poly/type  : ", graphicitem.stroke))
    output_text.append(merge_data(True,  False, "*gitem/poly/type  : ", graphicitem.fill))
    output_text.append(merge_data(False, False, " gitem/poly/type  : ", graphicitem.locked))
    output_text.append(merge_data(True,  False, "*gitem/poly/type  : ", graphicitem.tstamp))

    if printout:
        textbox("Details for Footprint Polygon", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_fpcurve(graphicitem, printout=False):
    output_text: list[str] = []

    for coord in graphicitem.coordinates:
        output_text.append(merge_data(False, False, " gitem/poly/type  : ", coord))

    output_text.append(merge_data(False, False, " gitem/curv/layer : ", graphicitem.layer))
    output_text.append(merge_data(True,  False, "*gitem/curv/width : ", graphicitem.width))
    output_text.append(merge_data(True,  False, "*gitem/curv/stroke: ", graphicitem.stroke))
    output_text.append(merge_data(True,  False, " gitem/curv/locked: ", graphicitem.locked))
    output_text.append(merge_data(True,  False, "*gitem/curv/tstamp: ", graphicitem.tstamp))

    if printout:
        textbox("Details for Footprint Curve ", output_text, False)
        return None
    else:
        return output_text


# ==================================================================================================================
def print_graphicitems(graphicitems, printout=False):
    output_text: list[str] = []

    loop = 0

    for graphicitem in graphicitems:
        if isinstance(graphicitem, FpText):
            print_fptext(graphicitem)

        elif isinstance(graphicitem, FpLine):
            print_fpline(graphicitem)

        elif isinstance(graphicitem, FpRect):
            print_fprect(graphicitem)

        elif isinstance(graphicitem, FpTextBox):
            print_fptextbox(graphicitem)

        elif isinstance(graphicitem, FpCircle):
            print_fpcircle(graphicitem)

        elif isinstance(graphicitem, FpArc):
            print_fparc(graphicitem)

        elif isinstance(graphicitem, FpPoly):
            print_fppoly(graphicitem)

        elif isinstance(graphicitem, FpCurve):
            print_fpcurve(graphicitem)
        loop += 1

    if printout:
        textbox("Details for Graphic Items ", output_text, False)
        return None
    else:
        if loop == 0:
            return "\n No Graphic Items."
        else:
            return output_text


# ==================================================================================================================
def print_pads(pads, printout=False):
    output_text: list[str] = []

    loop = 0

    for pad in pads:
        output_text.append("\n pad              : " + str(loop + 1))
        output_text.append(merge_data(False, False, " pad/number       : ", pad.number))
        output_text.append(merge_data(False, False, " pad/type         : ", pad.type))
        output_text.append(merge_data(False, False, " pad/shape        : ", pad.shape))
        output_text.append(merge_data(False, False, " pad/Position     : ", pad.position))
        output_text.append(merge_data(False, False, " pad/locked       : ", pad.locked))
        output_text.append(merge_data(True,  False, "*pad/size         : ", pad.size))

        if not(pad.drill is None):
            output_text.append(merge_data(True,  False, "*pad/drill/oval   : ", pad.drill.oval))
            output_text.append(merge_data(True,  False, "*pad/drill/dia    : ", pad.drill.diameter))
            output_text.append(merge_data(True,  False, "*pad/drill/width  : ", pad.drill.width))
            output_text.append(merge_data(True,  False, "*pad/drill/offset : ", pad.drill.offset))

        loop2 = 1

        for layer in pad.layers:
            output_text.append(merge_data(False, False, " pad/layers  " + format(loop2, ' 4d') + " : ", layer))
            loop2 += 1

        output_text.append(merge_data(True,  False, "*pad/property     : ", pad.property))
        output_text.append(merge_data(False, False, " pad/remUnuseLayer: ", pad.removeUnusedLayers))
        output_text.append(merge_data(False, False, " pad/keepEndLayer : ", pad.keepEndLayers))
        output_text.append(merge_data(True,  False, "*pad/rndrectRatio : ", pad.roundrectRatio))
        output_text.append(merge_data(True,  False, "*pad/chamferRatio : ", pad.chamferRatio))

        loop2 = 1

        for chamfer in pad.chamfer:
            output_text.append(merge_data(False, False, " pad/chamfer " + format(loop2, ' 4d') + " : ", chamfer))
            loop2 += 1

        if not (pad.net is None):
            output_text.append(merge_data(True, False, "*pad/net/number   : ", pad.net.number))
            output_text.append(merge_data(True, False, "*pad/net/name     : ", pad.net.name))

        output_text.append(merge_data(True, False, "*pad/tstamp       : ", pad.tstamp))
        output_text.append(merge_data(True, False, "*pad/pinFunction  : ", pad.pinFunction))
        output_text.append(merge_data(True, False, "*pad/pinType      : ", pad.pinType))
        output_text.append(merge_data(True, False, "*pad/dieLength    : ", pad.dieLength))
        output_text.append(merge_data(True, False, "*pad/sldrMskMargin: ", pad.solderMaskMargin))
        output_text.append(merge_data(True, False, "*pad/sldrPstMargin: ", pad.solderPasteMargin))
        output_text.append(merge_data(True, False, "*pad/sldrPstMargRa: ", pad.solderPasteMarginRatio))
        output_text.append(merge_data(True, False, "*pad/clearance    : ", pad.clearance))
        output_text.append(merge_data(True, False, "*pad/zoneConnect  : ", pad.zoneConnect))
        output_text.append(merge_data(True, False, "*pad/thermalWidth : ", pad.thermalWidth))
        output_text.append(merge_data(True, False, "*pad/thermalGap   : ", pad.thermalGap))

        if not (pad.customPadOptions is None):
            output_text.append(merge_data(True, False, "pad/custPad/clear : ", pad.customPadOptions.clear))
            output_text.append(merge_data(True, False, "pad/custPad/anchor: ", pad.customPadOptions.anchor))

        loop2 = 1

        for customPadPrimitive in pad.customPadPrimitives:
            output_text.append(merge_data(False, False, " pad/Prims   " + format(loop2, ' 4d') + " : ", customPadPrimitive))
            loop2 += 1

        loop += 1

    if printout:
        textbox("Details for Pads ", output_text, False)
        return None
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
# noinspection PyArgumentList
def print_zones(zones, printout=False):
    output_text: list[str] = []

    loop = 0

    for zone in zones:
        output_text.append(merge_data(False, False, " zones/locked      : " + zones.locked))
        output_text.append(merge_data(False, False, " zones/net         : " + zones.net))
        output_text.append(merge_data(False, False, " zones/netName     : " + zones.netname))

        loop2 = 1

        for layer in zone.layers:
            output_text.append(merge_data(False, False, " zone/layers " + format(loop2, ' 4d') + " : ", layer))
            loop2 += 1

        output_text.append(merge_data(True,  False, "*zone/tstamp       : " + zones.tstamp))
        output_text.append(merge_data(True,  False, "*zone/name         : " + zones.name))
        output_text.append(merge_data(False, False, " zone/hatch/style  : " + zones.hatch.style))
        output_text.append(merge_data(False, False, " zone/hatch/width  : " + zones.hatch.width))
        output_text.append(merge_data(True,  False, "*zone/priority     : " + zone.priority))
        output_text.append(merge_data(True,  False, "*zone/connectPads  : " + zone.connectPads))
        output_text.append(merge_data(False, False, " zone/clearance    : " + zone.clearance))
        output_text.append(merge_data(False, False, " zone/minThick     : " + zone.minThickness))
        output_text.append(merge_data(True,  False, "*zone/fillAreaThick: " + zone.filledAreasThickness))

        if not (zone.keepoutSettings is None):
            output_text.append(merge_data(False, False, " zones/keep/trk: " + zone.keepoutSettings.tracks))
            output_text.append(merge_data(False, False, " zones/keep/via: " + zone.keepoutSettings.vias))
            output_text.append(merge_data(False, False, " zones/keep/pad: " + zone.keepoutSettings.pads))
            output_text.append(merge_data(False, False, " zones/keep/cpr: " + zone.keepoutSettings.copperpour))
            output_text.append(merge_data(False, False, " zones/keep/fpr: " + zone.keepoutSettings.footprints))

        if not (zone.fillSettings is None):
            output_text.append(merge_data(False, False, "*zones/fill/yes: " + zone.fillSettings.yes))
            output_text.append(merge_data(True,  False, "*zones/fill/mde: " + zone.fillSettings.mode))
            output_text.append(merge_data(True,  False, "*zones/fill/tgp: " + zone.fillSettings.thermalGap))
            output_text.append(merge_data(True,  False, "*zones/fill/tBW: " + zone.fillSettings.thermalBridgeWidth))
            output_text.append(merge_data(True,  False, "*zones/fill/sS : " + zone.fillSettings.smoothingStyle))
            output_text.append(merge_data(True,  False, "*zones/fill/sR : " + zone.fillSettings.smoothingRadius))
            output_text.append(merge_data(True,  False, "*zones/fill/iRM: " + zone.fillSettings.islandRemovalMode))
            output_text.append(merge_data(True,  False, "*zones/fill/iAM: " + zone.fillSettings.islandAreaMin))
            output_text.append(merge_data(True,  False, "*zones/fill/hT : " + zone.fillSettings.hatchThickness))
            output_text.append(merge_data(True,  False, "*zones/fill/hG : " + zone.fillSettings.hatchGap))
            output_text.append(merge_data(True,  False, "*zones/fill/hO : " + zone.fillSettings.hatchOrientation))
            output_text.append(merge_data(True,  False, "*zones/fill/hSL: " + zone.fillSettings.hatchSmoothingLevel))
            output_text.append(merge_data(True,  False, "*zones/fill/hSV: " + zone.fillSettings.hatchSmoothingValue))
            output_text.append(merge_data(True,  False, "*zones/fill/hBA: " + zone.fillSettings.hatchBorderAlgorithm))
            output_text.append(merge_data(True,  False, "*zones/fill/hMH: " + zone.fillSettings.hatchMinHoleArea))

        for zpoly in zone.polygons:
            output_text.append(merge_data(False, False, " zones/polygons: " + zpoly.polygons))
        #    coordinates: List[Position] = field(default_factory=list)

        for fpoly in zone.filledPolygons:
            output_text.append(merge_data(False, False, " zones/fPoly/layer: " + fpoly.layer))
        #    layer: str = "F.Cu"
        #    island: bool = False
        #    coordinates: List[Position] = field(default_factory=list)

        if not (zone.fillSegments is None):
            output_text.append(merge_data(True, False, " zones/fillS/lay: " + zone.fillSegments.layer))
        #     coordinates: List[Position] = field(default_factory=list)

        loop += 1

    if printout:
        textbox("Details for Zones ", output_text, False)
        return None
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_groups(groups, printout=False):
    output_text: list[str] = []

    loop = 0

    for group in groups:
        output_text.append(merge_data(False, False, " groups           : ", group))
        loop += 1

    if printout:
        textbox("Details for Groups ", output_text, False)
        return None
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
        output_text.append(merge_data(False, False, " models/path      : ", model.path))
        output_text.append(merge_data(False, False, " models/pos       : ", model.pos))
        output_text.append(merge_data(False, False, " models/scale     : ", model.scale))
        output_text.append(merge_data(False, False, " models/rotate    : ", model.rotate))

        loop += 1

    if printout:
        textbox("Details for Models ", output_text, False)
        return None
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_footprint(footprintname, footprint, printout=False):
    output_text: list[str] = [merge_data(False, True, " LibraryLink      : ", footprint.libraryLink),
                              merge_data(True, False, "*version          : ", footprint.version),
                              merge_data(True, False, "*generator        : ", footprint.generator),
                              merge_data(False, False, " locked           : ", footprint.locked),
                              merge_data(False, False, " placed           : ", footprint.placed),
                              merge_data(False, False, " layer            : ", footprint.layer),
                              merge_data(False, False, " tedit            : ", footprint.tedit),
                              merge_data(True, False, "*tstamp           : ", footprint.tstamp),
                              merge_data(True, False, "*position         : ", footprint.position),
                              merge_data(True, False, "*description      : ", footprint.description),
                              merge_data(True, False, " tags             : ", footprint.tags)]

    output_text.extend(print_properties(footprint.properties))

    output_text.append(merge_data(True, False, "*path             : ", footprint.path))
    output_text.append(merge_data(True, False, "*autoplaceCost90  : ", footprint.autoplaceCost90))
    output_text.append(merge_data(True, False, "*autoplaceCost180 : ", footprint.autoplaceCost180))
    output_text.append(merge_data(True, False, "*solderMaskMargin : ", footprint.solderMaskMargin))
    output_text.append(merge_data(True, False, "*solderPasteMargin: ", footprint.solderPasteMargin))
    output_text.append(merge_data(True, False, "*solderPasteRatio : ", footprint.solderPasteRatio))
    output_text.append(merge_data(True, False, "*clearance        : ", footprint.clearance))
    output_text.append(merge_data(True, False, "*zoneConnect      : ", footprint.zoneConnect))
    output_text.append(merge_data(True, False, "*thermalWidth     : ", footprint.thermalWidth))
    output_text.append(merge_data(True, False, "*thermalGap       : ", footprint.thermalGap))

    output_text.extend(print_attributes(footprint.attributes))
    output_text.extend(print_graphicitems(footprint.graphicItems))
    output_text.extend(print_pads(footprint.pads))
    output_text.extend(print_zones(footprint.zones))
    output_text.extend(print_groups(footprint.groups))
    output_text.extend(print_models(footprint.models))

    output_text.extend(merge_data(True, False, "*filePath         ; ", footprint.filePath))

    if printout:
        textbox("Details for Footprint " + footprintname, "Footprint", output_text, False)
        return None
    else:
        return output_text
