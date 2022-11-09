#  ===================================================================
#  Source File Name : user_display.py
#  Purpose          : Common display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================
import string

from easygui import *
# import os

# from kiutils.footprint import *
from kiutils.items.common import *
# from kiutils.items.zones import *
from kiutils.items.fpitems import *

from kiutils.wks import *


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
        display_msg = "What " + msg + " related task do you want to perform? \n\r \n\rNOTE: Select \"Cancel\" to quit (without saving)."
        display_title = msg + " action(s)"

        display_selection = selection.copy()

        position = 0

        for entry in display_selection:
            display_selection[position] = "Task " + str(position + 1) + ": " + entry
            position += 1

        choice = choicebox(display_msg, display_title, display_selection)

        # if choice is None then selected cancel (which is effectively quit)
        if choice is None:
            # Do nothing.
            return "Quit"

        else:
            # Return User selection
            return choice[0:choice.find(":")]


# ==================================================================================================================
def print_data(prefix: string, data, optional = False, newline = False):

    # Add a * in front of text if data is optional, otherwise a space to keep alignment.
    if optional:
        newprefix = "*" + prefix
    else:
        newprefix = " " + prefix

    if isinstance(data, int):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == 0):
            return ""
        else:
            if newline:
                return newprefix + str(data)
            else:
                return "\n" + newprefix + str(data)

    elif isinstance(data, float):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == 0.0):
            return ""
        else:
            if newline:
                return newprefix + str(data)
            else:
                return "\n" + newprefix + str(data)

    elif isinstance(data, str):
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data == ""):
            return ""
        else:
            if newline:
                if len(data) > 40:
                    return newprefix + data[0:39] + "..."
                else:
                    return newprefix + data
            else:
                if len(data) > 40:
                    return "\n" + newprefix + data[0:39] + "..."
                else:
                    return "\n" + newprefix + data

    elif isinstance(data, Position):
        if newline:
            if data.angle is None:
                return newprefix + str(data.X) + "," + str(data.Y) + " 0 " +  str(data.unlocked)
            else:
                return newprefix + str(data.X) + "," + str(data.Y) + " " + str(data.angle) + " " + str(data.unlocked)
        else:
            if data.angle is None:
                return "\n" + newprefix + str(data.X) + "," + str(data.Y) + " 0 " + str(data.unlocked)
            else:
                return "\n" + newprefix + str(data.X) + "," + str(data.Y) + " " + str(data.angle) + " " + str(data.unlocked)

    elif isinstance(data, Coordinate):
        if newline:
            return newprefix + str(data.X) + "," + str(data.Y) + "," + str(data.Z)
        else:
            return "\n" + newprefix + str(data.X) + "," + str(data.Y) + "," + str(data.Z)

    elif isinstance(data, WksPosition):
        if newline:
            return newprefix + str(data.X) + "/" + str(data.Y) + " " + str(data.corner)
        else:
            return "\n" + newprefix + str(data.X) + "/" + str(data.Y) + " " + str(data.corner)

    elif isinstance(data, TextSize):
        if newline:
            return newprefix + str(data.width) + "/" + str(data.height)
        else:
            return "\n" + newprefix + str(data.width) + "/" + str(data.height)

    elif isinstance(data, PageSettings):
        if newline:
            return newprefix + data.paperSize + " " + str(data.portrait) + " (" + str(data.width) + " by " + str(data.height) + ")"
        else:
            return "\n" + newprefix + data.paperSize + " " + str(data.portrait) + " (" + str(data.width) + " by " + str(data.height) + ")"

    elif data is None:
        # if Options and is None, then nothing is defined so don't need to print
        if optional and (data is None):
            return ""
        else:
            if newline:
                return newprefix + "None"
            else:
                return "\n" + newprefix + "None"

    else:
        return "\n" + newprefix + str(type(data))


# ==================================================================================================================
def print_effects(prefix, effects, printout=False):
    output_text: list[str] = []

    if not (effects is None):
        if not (effects.font is None):
            output_text.extend(print_data(prefix + "/fnt/fa: ", effects.font.face))
            output_text.extend(print_data(prefix + "/fnt/he: ", effects.font.height))
            output_text.extend(print_data(prefix + "/fnt/wi: ", effects.font.width))
            output_text.extend(print_data(prefix + "/fnt/th: ", effects.font.thickness, True))
            output_text.extend(print_data(prefix + "/fnt/bo: ", effects.font.bold))
            output_text.extend(print_data(prefix + "/fnt/it: ", effects.font.italic))
            output_text.extend(print_data(prefix + "/fnt/lS: ", effects.font.lineSpacing, True))

        if not (effects.justify is None):
            output_text.extend(print_data(prefix + "/jst/ho: ", effects.justify.horizontally, True))
            output_text.extend(print_data(prefix + "/jst/ve: ", effects.justify.vertically, True))
            output_text.extend(print_data(prefix + "/jst/mi: ", effects.justify.mirror))

    if printout:
        textbox("Details for Effects (" + prefix + ")", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_stroke(prefix, stroke, printout=False):
    output_text: list[str] = []

    if not (stroke is None):
        output_text.extend(print_data(prefix + "/str/wi: ", stroke.width))
        output_text.extend(print_data(prefix + "/str/ty: ", stroke.type))
        output_text.extend(print_data(prefix + "/str/co: ", stroke.color))

    if printout:
        textbox("Details for Stroke ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_properties(prefix, properties, printout=False):
    output_text: list[str] = []

    loop = 0

    if len(properties) > 0:
        for propertie in properties:
            output_text.extend(print_property(prefix + "", propertie))
            loop += 1

    if printout:
        textbox("Details for Properties (" + prefix + ")", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_fp_text(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/text/type  : ", graphicitem.type),
                              print_data("FItem/text/text  : ", graphicitem.text),
                              print_data("FItem/text/pos   : ", graphicitem.position),
                              print_data("FItem/text/layer : ", graphicitem.layer),
                              print_data("FItem/text/hide  : ", graphicitem.hide)]

    output_text.extend(print_effects("FItem/text", graphicitem.effects))

    output_text.extend(print_data("FItem/text/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Footprint Text (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_line(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/line/start : ", graphicitem.start),
                              print_data("FItem/line/end   : ", graphicitem.end),
                              print_data("FItem/line/layer : ", graphicitem.layer),
                              print_data("FItem/line/width : ", graphicitem.width, True)]

    output_text.extend(print_stroke("FItem/line", graphicitem.stroke))

    output_text.extend(print_data("FItem/line/locked: ", graphicitem.locked))
    output_text.extend(print_data("FItem/line/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Footprint Line (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_rect(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/rect/start : ", graphicitem.start),
                              print_data("FItem/rect/end   : ", graphicitem.end),
                              print_data("FItem/rect/layer : ", graphicitem.layer),
                              print_data("FItem/rect/width : ", graphicitem.width, True)]

    output_text.extend(print_stroke("FItem/rect", graphicitem.stroke))

    output_text.extend(print_data("FItem/rect/fill  : ", graphicitem.fill, True))
    output_text.extend(print_data("FItem/rect/locked: ", graphicitem.locked))
    output_text.extend(print_data("FItem/rect/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Footprint Rectangle (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_textbox(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/tbox/locked: ", graphicitem.locked),
                              print_data("FItem/tbox/text  : ", graphicitem.text),
                              print_data("FItem/tbox/start : ", graphicitem.start),
                              print_data("FItem/tbox/end   : ", graphicitem.end)]

    for pts in graphicitem.pts:
        output_text.extend(print_data("FItem/tbox/points : ", pts))

    output_text.extend(print_data("FItem/tbox/angle : ", graphicitem.angle))
    output_text.extend(print_data("FItem/tbox/layer : ", graphicitem.layer))
    output_text.extend(print_data("FItem/tbox/tstamp: ", graphicitem.tstamp))

    output_text.extend(print_effects("FItem/tbox", graphicitem.effects))

    output_text.extend(print_data("FItem/tbox/stroke: ", graphicitem.stroke))
    output_text.extend(print_data("FItem/tbox/rCache: ", graphicitem.renderCache, True))

    if printout:
        textbox("Details for Footprint Textbox (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_circle(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/circ/centre: ", graphicitem.center),
                              print_data("FItem/circ/end   : ", graphicitem.end),
                              print_data("FItem/circ/layer : ", graphicitem.layer),
                              print_data("FItem/circ/width : ", graphicitem.width, True)]

    output_text.extend(print_stroke("FItem/circ", graphicitem.stroke))

    output_text.extend(print_data("FItem/circ/fill  : ", graphicitem.fill, True))
    output_text.extend(print_data("FItem/circ/locked: ", graphicitem.locked))
    output_text.extend(print_data("FItem/circ/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Footprint Circle (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_arc(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/arc/start  : ", graphicitem.start),
                              print_data("FItem/arc/mid    : ", graphicitem.mid),
                              print_data("FItem/arc/end    : ", graphicitem.end),
                              print_data("FItem/arc/layer  : ", graphicitem.layer),
                              print_data("FItem/arc/width  : ", graphicitem.width, True)]

    output_text.extend(print_stroke("FItem/arc", graphicitem.stroke))

    output_text.extend(print_data("FItem/arc/locked : ", graphicitem.locked))
    output_text.extend(print_data("FItem/arc/tstamp : ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Footprint Arc (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_poly(graphicitem, printout=False):
    output_text: list[str] = [print_data("FItem/poly/type  : ", graphicitem.layer)]

    loop = 1

    for coord in graphicitem.coordinates:
        output_text.extend(print_data("FItem/poly/co " + format(loop, '3d') + ": ", coord))
        loop += 1

    output_text.extend(print_data("FItem/poly/width : ", graphicitem.width))

    output_text.extend(print_stroke("*Item/poly", graphicitem.stroke))

    output_text.extend(print_data("FItem/poly/fill  : ", graphicitem.fill))
    output_text.extend(print_data("FItem/poly/locked: ", graphicitem.locked))
    output_text.extend(print_data("FItem/poly/tstamp: ", graphicitem.tstamp))

    if printout:
        textbox("Details for Footprint Polygon (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fp_curve(graphicitem, printout=False):
    output_text: list[str] = []

    for coord in graphicitem.coordinates:
        output_text.extend(print_data("FItem/curv/type  : ", coord))

    output_text.extend(print_data("FItem/curv/layer : ", graphicitem.layer))
    output_text.extend(print_data("FItem/curv/width : ", graphicitem.width))

    output_text.extend(print_stroke("FItem/curv", graphicitem.stroke))

    output_text.extend(print_data("FItem/curv/locked: ", graphicitem.locked))
    output_text.extend(print_data("FItem/curv/tstamp: ", graphicitem.tstamp))

    if printout:
        textbox("Details for Footprint Curve (FItem)", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_fgraphicitems(graphicitems, printout=False):
    output_text: list[str] = []

    loop = 0

    for graphicitem in graphicitems:
        if isinstance(graphicitem, FpText):
            output_text.extend(print_fp_text(graphicitem))

        elif isinstance(graphicitem, FpLine):
            output_text.extend(print_fp_line(graphicitem))

        elif isinstance(graphicitem, FpRect):
            output_text.extend(print_fp_rect(graphicitem))

        elif isinstance(graphicitem, FpTextBox):
            output_text.extend(print_fp_textbox(graphicitem))

        elif isinstance(graphicitem, FpCircle):
            output_text.extend(print_fp_circle(graphicitem))

        elif isinstance(graphicitem, FpArc):
            output_text.extend(print_fp_arc(graphicitem))

        elif isinstance(graphicitem, FpPoly):
            output_text.extend(print_fp_poly(graphicitem))

        elif isinstance(graphicitem, FpCurve):
            output_text.extend(print_fp_curve(graphicitem))

        loop += 1

    if printout:
        textbox("Details for Graphic Items ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_sgraphicitems(graphicitems, printout=False):
    output_text: list[str] = []

    loop = 0

    for graphicitem in graphicitems:
        if isinstance(graphicitem, FpText):
            output_text.extend(print_fp_text(graphicitem))

        elif isinstance(graphicitem, FpLine):
            output_text.extend(print_fp_line(graphicitem))

        elif isinstance(graphicitem, FpRect):
            output_text.extend(print_fp_rect(graphicitem))

        elif isinstance(graphicitem, FpTextBox):
            output_text.extend(print_fp_textbox(graphicitem))

        elif isinstance(graphicitem, FpCircle):
            output_text.extend(print_fp_circle(graphicitem))

        elif isinstance(graphicitem, FpArc):
            output_text.extend(print_fp_arc(graphicitem))

        elif isinstance(graphicitem, FpPoly):
            output_text.extend(print_fp_poly(graphicitem))

        elif isinstance(graphicitem, FpCurve):
            output_text.extend(print_fp_curve(graphicitem))

        loop += 1

    if printout:
        textbox("Details for Graphic Items ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
# noinspection PyArgumentList
def print_zones(prefix, zones, printout=False):
    output_text: list[str] = []

    loop = 0

    for zone in zones:
        output_text.extend(print_data(prefix[0] + "Item/locked     : ", zone.locked))
        output_text.extend(print_data(prefix[0] + "Item/net        : ", zone.net))
        output_text.extend(print_data(prefix[0] + "Item/netName    : ", zone.netName))

        loop2 = 1

        for layer in zone.layers:
            output_text.extend(print_data(prefix[0] + "Item/layers" + format(loop2, ' 4d') + " : ", layer))
            loop2 += 1

        output_text.extend(print_data(prefix[0] + "Item/tstamp     : ", zone.tstamp))
        output_text.extend(print_data(prefix[0] + "Item/name       : ", zone.name))
        output_text.extend(print_data(prefix[0] + "Item/hatch/style: ", zone.hatch.style))
        output_text.extend(print_data(prefix[0] + "Item/hatch/pitch: ", zone.hatch.pitch))
        output_text.extend(print_data(prefix[0] + "Item/priority   : ", zone.priority))
        output_text.extend(print_data(prefix[0] + "Item/connectPads: ", zone.connectPads))
        output_text.extend(print_data(prefix[0] + "Item/clearance  : ", zone.clearance))
        output_text.extend(print_data(prefix[0] + "Item/minThick   : ", zone.minThickness))
        output_text.extend(print_data(prefix[0] + "Item/fillAreaThi: ", zone.filledAreasThickness))

        if not (zone.keepoutSettings is None):
            output_text.extend(print_data(prefix[0] + "Item/keep/tracks: ", zone.keepoutSettings.tracks))
            output_text.extend(print_data(prefix[0] + "Item/keep/vias  : ", zone.keepoutSettings.vias))
            output_text.extend(print_data(prefix[0] + "Item/keep/pads  : ", zone.keepoutSettings.pads))
            output_text.extend(print_data(prefix[0] + "Item/keep/cprpur: ", zone.keepoutSettings.copperpour))
            output_text.extend(print_data(prefix[0] + "Item/keep/footpr: ", zone.keepoutSettings.footprints))

        if not (zone.fillSettings is None):
            output_text.extend(print_data(prefix[0] + "Item/fill/yes   : ", zone.fillSettings.yes))
            output_text.extend(print_data(prefix[0] + "Item/fill/mode  : ", zone.fillSettings.mode))
            output_text.extend(print_data(prefix[0] + "Item/fill/thergp: ", zone.fillSettings.thermalGap))
            output_text.extend(print_data(prefix[0] + "Item/fill/therBW: ", zone.fillSettings.thermalBridgeWidth))
            output_text.extend(print_data(prefix[0] + "Item/fill/smoSty: ", zone.fillSettings.smoothingStyle))
            output_text.extend(print_data(prefix[0] + "Item/fill/smoRad: ", zone.fillSettings.smoothingRadius))
            output_text.extend(print_data(prefix[0] + "Item/fill/islRM : ", zone.fillSettings.islandRemovalMode))
            output_text.extend(print_data(prefix[0] + "Item/fill/islAM : ", zone.fillSettings.islandAreaMin))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatThi: ", zone.fillSettings.hatchThickness))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatGap: ", zone.fillSettings.hatchGap))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatOri: ", zone.fillSettings.hatchOrientation))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatSmL: ", zone.fillSettings.hatchSmoothingLevel))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatSmV: ", zone.fillSettings.hatchSmoothingValue))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatBoA: ", zone.fillSettings.hatchBorderAlgorithm))
            output_text.extend(print_data(prefix[0] + "Item/fill/hatMHA: ", zone.fillSettings.hatchMinHoleArea))

        for poly in zone.polygons:

            looper = 1

            for coord in poly.coordinates:
                if looper < 1000:
                    output_text.extend(print_data(prefix[0] + "Item/poly/co " + format(looper, '3d') + ": ", coord))

                looper += 1

        for fpoly in zone.filledPolygons:
            output_text.extend(print_data(prefix[0] + "Item/fPoly/layer: ", fpoly.layer))
            output_text.extend(print_data(prefix[0] + "Item/fPoly/islnd: ", fpoly.island))

            looper = 1

            for coord in fpoly.coordinates:
                if looper < 1000:
                    output_text.extend(print_data(prefix[0] + "Item/fPoly/co" + format(looper, '3d') + ": ", coord))

                looper += 1

        if not (zone.fillSegments is None):
            output_text.extend(print_data(prefix[0] + "Item/fillS/lay: ", zone.fillSegments.layer))

            for coord in zone.fillSegments.coordinates:
                output_text.extend(print_data(prefix[0] + "Item/fillS/cor: ", coord))

        loop += 1

    if printout:
        textbox("Details for " + prefix, output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_groups(prefix, groups, printout=False):
    output_text: list[str] = []

    loop = 0

    for group in groups:
        output_text.extend(print_data(prefix[0] + "group           : ", group))
        loop += 1

    if printout:
        textbox("Details for Groups ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_alternatepin(alternatepin, printout=False):
    output_text: list[str] = []

    for pin in alternatepin:
        output_text.extend(print_data("syms/sym/Apin/Nam: ", pin.pinName))
        output_text.extend(print_data("syms/sym/Apin/ele: ", pin.electricalType))
        output_text.extend(print_data("syms/sym/Apin/gra: ", pin.graphicalStyle))

        for unit in pin.units:
            output_text.extend(print_data("syms/sym/Apin/uni: ", unit))

    if printout:
        textbox("Details for Alternate Pin ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_symbol(symbols, printout=False):
    output_text: list[str] = []

    for symbol in symbols:
        output_text.extend(print_data("syms/sym/id      : ", symbol.id))
        output_text.extend(print_data("syms/sym/extends : ", symbol.extends))
        output_text.extend(print_data("syms/sym/hidPinNo: ", symbol.hidePinNumbers))
        output_text.extend(print_data("syms/sym/pinNames: ", symbol.pinNames))
        output_text.extend(print_data("syms/sym/pinNaHid: ", symbol.pinNamesHide))
        output_text.extend(print_data("syms/sym/pinNaOff: ", symbol.pinNamesOffset))
        output_text.extend(print_data("syms/sym/inBom   : ", symbol.inBom))
        output_text.extend(print_data("syms/sym/onBoard : ", symbol.onBoard))
        output_text.extend(print_data("syms/sym/isPower : ", symbol.isPower))

        output_text.extend(print_properties("syms/symbl", symbol.properties))

        output_text.extend(print_sgraphicitems("syms/symbl", symbol.graphicItems))

        output_text.extend(print_alternatepin(symbol.pins))

    if printout:
        textbox("Details for Symbol ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_property(prefix, propertie, printout=False):
    output_text: list[str] = []

    if not (propertie is None):
        if isinstance(propertie, Property):
            output_text.extend(print_data(prefix + "/pr/key: ", propertie.key))
            output_text.extend(print_data(prefix + "/pr/val: ", propertie.value))
            output_text.extend(print_data(prefix + "/pr/id : ", propertie.id))
            output_text.extend(print_data(prefix + "/pr/pos: ", propertie.position))
            output_text.extend(print_effects(prefix, propertie.effects))

        elif isinstance(propertie, str):
            output_text.extend(print_data(prefix + "/Value  : ", propertie))

        # Not sure if this is required so commented out.
        # elif isinstance(propertie, Dict):
        #    for key, value in propertie.item():
        #        output_text.extend(print_data(prefix + "/pr/key: ", key))
        #        output_text.extend(print_data(prefix + "/pr/val: ", value))

        else:
            print("-----> Error in property! <-----")
            for key, value in propertie.item():
                output_text.extend(print_data(prefix + "/prop/key: ", key))
                output_text.extend(print_data(prefix + "/prop/val: ", value))

    if printout:
        textbox("Details for Property ", output_text, False)
        return ""
    else:
        return output_text
