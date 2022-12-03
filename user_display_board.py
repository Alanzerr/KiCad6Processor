#  ===================================================================
#  Source File Name : user_display_board.py
#  Purpose          : Board specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

# from user_display import *

from kiutils.items.gritems import *
from kiutils.items.brditems import *

from user_display_footprint import *


# ==================================================================================================================
def print_nets(nets, printout=False):
    output_text: list[str] = []

    for net in nets:
        output_text.extend(print_data("Brd/net/number   : ", net.number))
        output_text.extend(print_data("Brd/net/name     : ", net.name))

    if printout:
        textbox("Details for Nets ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_footprints(footprints, printout=False):
    output_text: list[str] = []

    for footprint in footprints:
        if len(footprint.libraryLink) > 40:
            output_text.extend("\n---- Footprint ---- " + footprint.libraryLink[0:39] + "...\n")
        else:
            output_text.extend("\n---- Footprint ---- " + footprint.libraryLink + "\n")

        output_text.extend(print_footprint(footprint.libraryLink, footprint))

    if printout:
        textbox("Details for Board Footprints ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_segment(traceitem, printout=False):
    output_text: list[str] = [print_data("Brd/Tra/seg/start: ", traceitem.start),
                              print_data("Brd/Tra/seg/end  : ", traceitem.end),
                              print_data("Brd/Tra/seg/width: ", traceitem.width),
                              print_data("Brd/Tra/seg/layer: ", traceitem.layer),
                              print_data("Brd/Tra/seg/lock : ", traceitem.locked),
                              print_data("Brd/Tra/seg/net  : ", traceitem.net),
                              print_data("Brd/Tra/seg/tstmp: ", traceitem.tstamp)]

    if printout:
        textbox("Details for Board Segment ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_via(traceitem, printout=False):
    output_text: list[str] = [print_data("Brd/Tra/via/type : ", traceitem.type, True),
                              print_data("Brd/Tra/via/lock : ", traceitem.locked),
                              print_data("Brd/Tra/via/pos  : ", traceitem.position),
                              print_data("Brd/Tra/via/size : ", traceitem.size),
                              print_data("Brd/Tra/via/drill: ", traceitem.drill)]

    for layer in traceitem.layers:
        output_text.extend(print_data("Brd/Tra/via/layer: ", layer))

    output_text.extend(print_data("Brd/Tra/via/rUnLa: ", traceitem.removeUnusedLayers))
    output_text.extend(print_data("Brd/Tra/via/kEnLa: ", traceitem.keepEndLayers))
    output_text.extend(print_data("Brd/Tra/via/free : ", traceitem.free))
    output_text.extend(print_data("Brd/Tra/via/net  : ", traceitem.net))
    output_text.extend(print_data("Brd/Tra/via/tstmp: ", traceitem.tstamp, True))

    if printout:
        textbox("Details for Board Via ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_arc(traceitem, printout=False):
    output_text: list[str] = [print_data("Brd/Tra/arc/start: ", traceitem.start),
                              print_data("Brd/Tra/arc/mid  : ", traceitem.mid),
                              print_data("Brd/Tra/arc/end  : ", traceitem.end),
                              print_data("Brd/Tra/arc/width: ", traceitem.width),
                              print_data("Brd/Tra/arc/layer: ", traceitem.layer),
                              print_data("Brd/Tra/arc/lock : ", traceitem.locked),
                              print_data("Brd/Tra/arc/net  : ", traceitem.net),
                              print_data("Brd/Tra/arc/tstmp: ", traceitem.tstamp, True)]

    if printout:
        textbox("Details for Board Arc ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_traceitems(traceitems, printout=False):
    output_text: list[str] = []

    loop = 0

    for traceitem in traceitems:
        if isinstance(traceitem, Segment):
            output_text.extend(print_segment(traceitem))

        elif isinstance(traceitem, Via):
            output_text.extend(print_via(traceitem))

        elif isinstance(traceitem, Arc):
            output_text.extend(print_arc(traceitem))

        loop += 1

    if printout:
        textbox("Details for Board Trace Items ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_gr_text(prefix, graphicitem, printout=False):
    output_text: list[str] = [print_data(prefix + "/text/text  : ", graphicitem.text),
                              print_data(prefix + "/text/pos   : ", graphicitem.position),
                              print_data(prefix + "/text/layer : ", graphicitem.layer)]

    output_text.extend(print_effects("" + prefix + "/text", graphicitem.effects))

    output_text.extend(print_data(prefix + "/text/tstamp: ", graphicitem.tstamp, True))
    output_text.extend(print_data(prefix + "/text/locked: ", graphicitem.locked))

    if printout:
        textbox("Details for Board Text (" + prefix + ")", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_textbox(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/tbox/locked: ", graphicitem.locked),
                              print_data("BItem/tbox/text  : ", graphicitem.text),
                              print_data("BItem/tbox/start : ", graphicitem.start),
                              print_data("BItem/tbox/end   : ", graphicitem.end)]

    for pts in graphicitem.pts:
        output_text.extend(print_data("BItem/tbox/points : ", pts))

    output_text.extend(print_data("BItem/tbox/angle : ", graphicitem.angle))
    output_text.extend(print_data("BItem/tbox/layer : ", graphicitem.layer))
    output_text.extend(print_data("BItem/tbox/tstamp: ", graphicitem.tstamp))

    output_text.extend(print_effects("BItem/tbox", graphicitem.effects))

    output_text.extend(print_stroke("BItem/tbox", graphicitem.stroke))

    output_text.extend(print_data("BItem/tbox/rCache: ", graphicitem.renderCache, True))

    if printout:
        textbox("Details for Board Textbox ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_line(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/line/start : ", graphicitem.start),
                              print_data("BItem/line/end   : ", graphicitem.end),
                              print_data("BItem/line/angle : ", graphicitem.angle, True),
                              print_data("BItem/line/layer : ", graphicitem.layer),
                              print_data("BItem/line/width : ", graphicitem.width, True),
                              print_data("BItem/line/tstamp: ", graphicitem.tstamp, True),
                              print_data("BItem/line/locked: ", graphicitem.locked)]

    if printout:
        textbox("Details for Board Line ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_rect(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/rect/start : ", graphicitem.start),
                              print_data("BItem/rect/end   : ", graphicitem.end),
                              print_data("BItem/rect/layer : ", graphicitem.layer, True),
                              print_data("BItem/rect/width : ", graphicitem.width, True),
                              print_data("BItem/rect/fill  : ", graphicitem.fill, True),
                              print_data("BItem/rect/locked: ", graphicitem.locked),
                              print_data("BItem/rect/tstamp: ", graphicitem.tstamp, True),
                              print_data("BItem/rect/locked: ", graphicitem.locked)]

    if printout:
        textbox("Details for Board Rectangle ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_circle(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/circ/centre: ", graphicitem.center),
                              print_data("BItem/circ/end   : ", graphicitem.end),
                              print_data("BItem/circ/layer : ", graphicitem.layer, True),
                              print_data("BItem/circ/width : ", graphicitem.width, True),
                              print_data("BItem/circ/fill  : ", graphicitem.fill, True),
                              print_data("BItem/circ/tstamp: ", graphicitem.tstamp, True),
                              print_data("BItem/circ/locked: ", graphicitem.locked)]

    if printout:
        textbox("Details for Board Circle ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_arc(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/arc/start  : ", graphicitem.start),
                              print_data("BItem/arc/mid    : ", graphicitem.mid),
                              print_data("BItem/arc/end    : ", graphicitem.end),
                              print_data("BItem/arc/layer  : ", graphicitem.layer, True),
                              print_data("BItem/arc/width  : ", graphicitem.width, True),
                              print_data("BItem/arc/tstamp : ", graphicitem.tstamp, True),
                              print_data("BItem/arc/locked : ", graphicitem.locked)]

    if printout:
        textbox("Details for Board Arc ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_poly(graphicitem, printout=False):
    output_text: list[str] = [print_data("BItem/poly/type  : ", graphicitem.layer)]

    loop = 1

    for coord in graphicitem.coordinates:
        output_text.extend(print_data("BItem/poly/co " + format(loop, '3d') + ": ", coord))
        loop += 1

    output_text.extend(print_data("BItem/poly/width : ", graphicitem.width, True))

    output_text.extend(print_stroke("BItem/poly", graphicitem.stroke))

    output_text.extend(print_data("BItem/poly/fill  : ", graphicitem.fill, True))
    output_text.extend(print_data("BItem/poly/locked: ", graphicitem.locked))
    output_text.extend(print_data("BItem/poly/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Board Polygon ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_gr_curve(graphicitem, printout=False):
    output_text: list[str] = []

    for coord in graphicitem.coordinates:
        output_text.extend(print_data("BItem/curv/type  : ", coord))

    output_text.extend(print_data("BItem/curv/layer : ", graphicitem.layer))
    output_text.extend(print_data("BItem/curv/width : ", graphicitem.width, True))

    output_text.extend(print_stroke("BItem/curv", graphicitem.stroke))

    output_text.extend(print_data("BItem/curv/locked: ", graphicitem.locked, True))
    output_text.extend(print_data("BItem/curv/tstamp: ", graphicitem.tstamp, True))

    if printout:
        textbox("Details for Board Curve ", output_text, False)
        return ""
    else:
        return output_text


# =================================================================================================================
def print_dimensions(dimensions, printout=False):
    output_text: list[str] = []

    loop = 1

    for dimension in dimensions:
        output_text.extend(print_data("Brd/Dim/lock " + format(loop, '3d') +  " : ", dimension.locked))
        output_text.extend(print_data("Brd/Dim/type     : ", dimension.type))
        output_text.extend(print_data("Brd/Dim/layer    : ", dimension.layer))
        output_text.extend(print_data("Brd/Dim/tstamp   : ", dimension.tstamp, True))

        loop2 = 1

        for point in dimension.pts:
            output_text.extend(print_data("Brd/Dim/pts " + format(loop2, '4d') + " : ", point))
            loop2 += 1

        output_text.extend(print_data("Brd/Dim/height   : ", dimension.height, True))
        output_text.extend(print_data("Brd/Dim/orient   : ", dimension.orientation, True))
        output_text.extend(print_data("Brd/Dim/leaderlen: ", dimension.leaderLength, True))

        if dimension.grText is not None:
            output_text.extend(print_gr_text("DItem", dimension.grText))

        if dimension.format is not None:
            output_text.extend(print_data("Brd/Dim/frm/pre  : ", dimension.format.prefix, True))
            output_text.extend(print_data("Brd/Dim/frm/suf  : ", dimension.format.suffix, True))
            output_text.extend(print_data("Brd/Dim/frm/units: ", dimension.format.units))
            output_text.extend(print_data("Brd/Dim/frm/unitF: ", dimension.format.unitsFormat))
            output_text.extend(print_data("Brd/Dim/frm/prec : ", dimension.format.precision))
            output_text.extend(print_data("Brd/Dim/frm/over : ", dimension.format.overrideValue, True))
            output_text.extend(print_data("Brd/Dim/frm/supp : ", dimension.format.suppressZeroes))

        output_text.extend(print_data("Brd/Dim/sty/thick: ", dimension.style.thickness))
        output_text.extend(print_data("Brd/Dim/sty/arrLe: ", dimension.style.arrowLength))
        output_text.extend(print_data("Brd/Dim/sty/txtPo: ", dimension.style.textPositionMode))
        output_text.extend(print_data("Brd/Dim/sty/extHe: ", dimension.style.extensionHeight))
        output_text.extend(print_data("Brd/Dim/sty/txtFr: ", dimension.style.textFrame, True))
        output_text.extend(print_data("Brd/Dim/sty/extOf: ", dimension.style.extensionOffset, True))
        output_text.extend(print_data("Brd/Dim/sty/TxtAl: ", dimension.style.keepTextAligned))

    if printout:
        textbox("Details for Dimensions ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_targets(targets, printout=False):
    output_text: list[str] = []

    loop = 1

    for target in targets:
        output_text.extend(print_data("Brd/Target/type " + format(loop, '2d') + ": ", target.type))
        output_text.extend(print_data("Brd/Target/pos    : ", target.position))
        output_text.extend(print_data("Brd/Target/size   : ", target.size))
        output_text.extend(print_data("Brd/Target/width  : ", target.width))
        output_text.extend(print_data("Brd/Target/layer  : ", target.layer))
        output_text.extend(print_data("Brd/Target/tstamp : ", target.tstamp, True))

        loop += 1

    if printout:
        textbox("Details for Targets ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_plotsettings(plotsettings, printout=False):
    output_text: list[str] = []

    if plotsettings is not None:
        output_text.extend(print_data("Brd/Plot/layersel: ", plotsettings.layerSelection))
        output_text.extend(print_data("Brd/Plot/disAper : ", plotsettings.disableApertMacros))
        output_text.extend(print_data("Brd/Plot/GerExt  : ", plotsettings.useGerberExtensions))
        output_text.extend(print_data("Brd/Plot/GerAttr : ", plotsettings.useGerberAttributes))
        output_text.extend(print_data("Brd/Plot/GetAdvAt: ", plotsettings.useGerberAdvancedAttributes))
        output_text.extend(print_data("Brd/Plot/GerJobFi: ", plotsettings.createGerberJobFile))
        output_text.extend(print_data("Brd/Plot/svgUseIn: ", plotsettings.svgUseInch))
        output_text.extend(print_data("Brd/Plot/svgPrec : ", plotsettings.svgPrecision))
        output_text.extend(print_data("Brd/Plot/excEdge : ", plotsettings.excludeEdgeLayer))
        output_text.extend(print_data("Brd/Plot/plotFame: ", plotsettings.plotFameRef))
        output_text.extend(print_data("Brd/Plot/viaOnMsk: ", plotsettings.viasOnMask))
        output_text.extend(print_data("Brd/Plot/mode    : ", plotsettings.mode))
        output_text.extend(print_data("Brd/Plot/AuxOrig : ", plotsettings.useAuxOrigin))
        output_text.extend(print_data("Brd/Plot/hpglPenN: ", plotsettings.hpglPenNumber))
        output_text.extend(print_data("Brd/Plot/hpglPenS: ", plotsettings.hpglPenSpeed))
        output_text.extend(print_data("Brd/Plot/hpglPenD: ", plotsettings.hpglPenDiameter))
        output_text.extend(print_data("Brd/Plot/dxdPolyM: ", plotsettings.dxfPolygonMode))
        output_text.extend(print_data("Brd/Plot/dxfImper: ", plotsettings.dxfImperialUnits))
        output_text.extend(print_data("Brd/Plot/dxfUsePF: ", plotsettings.dxfUsePcbnewFont))
        output_text.extend(print_data("Brd/Plot/psNegatv: ", plotsettings.psNegative))
        output_text.extend(print_data("Brd/Plot/psA4Out : ", plotsettings.psA4Output))
        output_text.extend(print_data("Brd/Plot/plotRef : ", plotsettings.plotReference))
        output_text.extend(print_data("Brd/Plot/plotVal : ", plotsettings.plotValue))
        output_text.extend(print_data("Brd/Plot/plotInvT: ", plotsettings.plotInvisibleText))
        output_text.extend(print_data("Brd/Plot/sktPadOn: ", plotsettings.sketchPadsOnFab))
        output_text.extend(print_data("Brd/Plot/subMskSi: ", plotsettings.subtractMaskFromSilk))
        output_text.extend(print_data("Brd/Plot/outputF : ", plotsettings.outputFormat))
        output_text.extend(print_data("Brd/Plot/mirror  : ", plotsettings.mirror))
        output_text.extend(print_data("Brd/Plot/drillShp: ", plotsettings.drillShape))
        output_text.extend(print_data("Brd/Plot/scalesSe: ", plotsettings.scaleSelection))
        output_text.extend(print_data("Brd/Plot/outputDi: ", plotsettings.outputDirectory))

    if printout:
        textbox("Details for Plot Settings ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_stackup(stackup, printout=False):
    output_text: list[str] = []

    # Stackup in SetupData
    if stackup is not None:

        # Layers in Stackup
        for layer in stackup.layers:
            output_text.extend(print_data("Brd/stack/Lay/Nam: ", layer.name))
            # output_text.extend(print_data("Brd/stack/Lay/Num : ", layer.number)) Appears in documentation but not the actual file - see brditems.py
            output_text.extend(print_data("Brd/stack/Lay/Typ: ", layer.type))
            output_text.extend(print_data("Brd/stack/Lay/Col: ", layer.color, True))
            output_text.extend(print_data("Brd/stack/Lay/Thi: ", layer.thickness, True))
            output_text.extend(print_data("Brd/stack/Lay/Mat: ", layer.material, True))
            output_text.extend(print_data("Brd/stack/Lay/epi: ", layer.epsilonR, True))
            output_text.extend(print_data("Brd/stack/Lay/los: ", layer.lossTangent, True))

            for subLayer in layer.subLayers:
                output_text.extend(print_data("Brd/stack/Ll/Thic: ", subLayer.thickness))
                output_text.extend(print_data("Brd/stack/Ll/Mat : ", subLayer.material, True))
                output_text.extend(print_data("Brd/stack/L1/epiR: ", subLayer.epsilonR, True))
                output_text.extend(print_data("Brd/stack/Ll/losT: ", subLayer.lossTangent, True))

        # Rest of Stackup
        output_text.extend(print_data("Brd/stack/copFin : ", stackup.copperFinish, True))
        output_text.extend(print_data("Brd/stack/dielec : ", stackup.dielectricContraints, True))
        output_text.extend(print_data("Brd/stack/edgeCon: ", stackup.edgeConnector, True))
        output_text.extend(print_data("Brd/stack/castePa: ", stackup.castellatedPads))
        output_text.extend(print_data("Brd/stack/edgePla: ", stackup.edgePlating))

    if printout:
        textbox("Details for Plot Settings ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_bgraphicitems(graphicitems, printout=False):
    output_text: list[str] = []

    loop = 0

    for graphicitem in graphicitems:
        if isinstance(graphicitem, GrText):
            output_text.extend(print_gr_text("BItem", graphicitem))

        elif isinstance(graphicitem, GrLine):
            output_text.extend(print_gr_line(graphicitem))

        elif isinstance(graphicitem, GrRect):
            output_text.extend(print_gr_rect(graphicitem))

        elif isinstance(graphicitem, GrTextBox):
            output_text.extend(print_gr_textbox(graphicitem))

        elif isinstance(graphicitem, GrCircle):
            output_text.extend(print_gr_circle(graphicitem))

        elif isinstance(graphicitem, GrArc):
            output_text.extend(print_gr_arc(graphicitem))

        elif isinstance(graphicitem, GrPoly):
            output_text.extend(print_gr_poly(graphicitem))

        elif isinstance(graphicitem, GrCurve):
            output_text.extend(print_gr_curve(graphicitem))

        loop += 1

    if printout:
        textbox("Details for Graphic Items", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_board(boardname, board, printout=False):
    output_text: list[str] = [print_data("Brd/version      : ", board.version),
                              print_data("Brd/generator    : ", board.generator),
                              print_data("Brd/general/thick: ", board.general.thickness),
                              print_data("Brd/paper        : ", board.paper)]

    if board.titleBlock is not None:
        output_text.extend(print_data("Brd/titleB/title : ", board.titleBlock.title))
        output_text.extend(print_data("Brd/titleB/date  : ", board.titleBlock.date))
        output_text.extend(print_data("Brd/titleB/rev   : ", board.titleBlock.revision))
        output_text.extend(print_data("Brd/titleB/compan: ", board.titleBlock.company))

        for key, value in board.titleBlock.comments.items():
            output_text.extend(print_data("Brd/titleB/comVal: ", value))
            output_text.extend(print_data("Brd/titleB/comKey: ", key))

    # Layers list in board
    for layer in board.layers:
        output_text.extend(print_data("Brd/layers/ordina: ", layer.ordinal))
        output_text.extend(print_data("Brd/layers/name  : ", layer.name))
        output_text.extend(print_data("Brd/layers/type  : ", layer.type))
        output_text.extend(print_data("Brd/layers/uName : ", layer.userName))

    # Setup Data in board
    output_text.extend(print_stackup(board.setup.stackup))

    output_text.extend(print_data("Brd/setup/pad2Msk: ", board.setup.packToMaskClearance))
    output_text.extend(print_data("Brd/setup/SoldMsk: ", board.setup.solderMaskMinWidth))
    output_text.extend(print_data("Brd/setup/pa2Past: ", board.setup.padToPasteClearance))
    output_text.extend(print_data("Brd/setup/pa2PasR: ", board.setup.padToPasteClearanceRatio))
    output_text.extend(print_data("Brd/setup/auxAxis: ", board.setup.auxAxisOrigin))
    output_text.extend(print_data("Brd/setup/gridOri: ", board.setup.gridOrigin))

    output_text.extend(print_plotsettings(board.setup.plotSettings))

    # Rest of board
    output_text.extend(print_properties("BProp", board.properties))
    output_text.extend(print_nets(board.nets))
    output_text.extend(print_footprints(board.footprints))
    output_text.extend(print_bgraphicitems(board.graphicalItems))
    output_text.extend(print_traceitems(board.traceItems))
    output_text.extend(print_zones("BZone", board.zones))
    output_text.extend(print_dimensions(board.dimensions))
    output_text.extend(print_targets(board.targets))
    output_text.extend(print_groups("BGroup", board.groups))

    output_text.extend(print_data("Brd/filePath     : ", board.filePath))

    if printout:
        textbox("Details for Board " + boardname, "Board", output_text, False)
        return ""
    else:
        return output_text
