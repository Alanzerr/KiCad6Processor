#  ===================================================================
#  Source File Name : user_display_schematic.py
#  Purpose          : Schematic specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_libsymbols(libsymbols, printout=False):
    output_text: list[str] = []

    output_text.extend(print_symbol(libsymbols, printout))

    if printout:
        textbox("Details for Models ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_schematicsymbols(schematicsymbols, printout = False):
    output_text: list[str] = []

    loop = 0

    for schematicsymbol in schematicsymbols:
        output_text.extend(print_data("sym/TB/sSy/libID : ", schematicsymbol.libraryIdentifier))
        output_text.extend(print_data("sym/TB/sSy/pos   : ", schematicsymbol.position))
        output_text.extend(print_data("sym/TB/sSy/unit  : ", schematicsymbol.unit, True))
        output_text.extend(print_data("sym/TB/sSy/inBom : ", schematicsymbol.inBom))
        output_text.extend(print_data("sym/TB/sSy/onBrd : ", schematicsymbol.onBoard))
        output_text.extend(print_data("sym/TB/sSy/FieAut: ", schematicsymbol.fieldsAutoplaced))
        output_text.extend(print_data("sym/TB/sSy/uuid  : ", schematicsymbol.uuid))

        output_text.extend(print_properties("sym/TB/sSy", schematicsymbol.properties))

        if len(schematicsymbol.pins) > 0:
            for key, value in schematicsymbol.pins.items():
                output_text.extend(print_data("sym/TB/sSy/pinval: ", value))
                output_text.extend(print_data("sym/TB/sSy/pinkey: ", key))

        output_text.extend(print_data("sym/TB/sSy/mirror: ", schematicsymbol.mirror, True))
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
def print_junctions(junctions, printout=False):
    output_text: list[str] = []

    loop = 0

    for junction in junctions:
        output_text.extend(print_data("sym/TB/junc/pos  : ", junction.position))
        output_text.extend(print_data("sym/TB/junc/dis  : ", junction.diameter))
        output_text.extend(print_data("sym/TB/junc/color: ", junction.color))
        output_text.extend(print_data("sym/TB/junc/uuid : ", junction.uuid))
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
def print_noconnects(noconnects, printout=False):
    output_text: list[str] = []

    loop = 0

    for noconnect in noconnects:
        output_text.extend(print_data("sym/TB/noc/pos   : ", noconnect.position))
        output_text.extend(print_data("sym/TB/noc/uuid  : ", noconnect.uuid))
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
def print_busentries(busentries, printout=False):
    output_text: list[str] = []

    loop = 0

    for busentry in busentries:
        output_text.extend(print_data("sym/TB/bus/pos   : ", busentry.position))
        output_text.extend(print_data("sym/TB/bus/uuid  : ", busentry.uuid))
        output_text.extend(print_data("sym/TB/bus/size  : ", busentry.size))

        output_text.extend(print_stroke("sym/TB/bus", busentry.stroke))

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
def print_connection(prefix, connection, printout=False):
    output_text: list[str] = []

    output_text.extend(print_data(prefix + "/type  : ", connection.type))

    for pts in connection.points:
        output_text.extend(print_data(prefix + "/pos   : ", pts))

    output_text.extend(print_stroke(prefix, connection.stroke))

    output_text.extend(print_data(prefix + "/uuid  : ", connection.uuid))

    if printout:
        textbox("Details for Connection ", output_text, False)
        return ""
    else:
        return output_text


# ==================================================================================================================
def print_connections(connections, printout=False):
    output_text: list[str] = []

    loop = 0

    for connection in connections:
        output_text.extend(print_connection("sym/TB/con", connection))

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
def print_images(images, printout=False):
    output_text: list[str] = []

    loop = 0

    for image in images:
        output_text.extend(print_data("sym/TB/img/pos   : ", image.position))
        output_text.extend(print_data("sym/TB/img/scale : ", image.scale, True))

        for idata in image.data:
            output_text.extend(print_data("sym/TB/img/data  : ", idata))

        output_text.extend(print_data("sym/TB/img/uuid  : ", image.uuid))
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
def print_texts(texts, printout=False):
    output_text: list[str] = []

    loop = 0

    for text in texts:
        output_text.extend(print_data("sym/TB/txt/text  : ", text.text))
        output_text.extend(print_data("sym/TB/txt/pos   : ", text.position))

        output_text.extend(print_effects("sym/TB/txt", text.effects))

        output_text.extend(print_data("sym/TB/txt/uuid  : ", text.uuid))
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
def print_locallabels(llabels, printout=False):
    output_text: list[str] = []

    loop = 0

    for label in llabels:
        output_text.extend(print_data("sym/TB/lLb/text  : ", label.text))
        output_text.extend(print_data("sym/TB/lLb/pos   : ", label.position))

        output_text.extend(print_effects("sym/TB/lLb", label.effects))

        output_text.extend(print_data("sym/TB/lLb/uuid  : ", label.uuid))
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
def print_globallabels(glabels, printout=False):
    output_text: list[str] = []

    loop = 0

    for glabel in glabels:
        output_text.extend(print_data("sym/TB/gLb/text  : ", glabel.text))
        output_text.extend(print_data("sym/TB/gLb/shape : ", glabel.shape))
        output_text.extend(print_data("sym/TB/gLb/fiAuto: ", glabel.fieldsAutoplaced))
        output_text.extend(print_data("sym/TB/gLb/pos   : ", glabel.position))

        output_text.extend(print_effects("sym/TB/gLb", glabel.effects))

        output_text.extend(print_data("sym/TB/gLb/uuid  : ", glabel.uuid))

        output_text.extend(print_properties("sym/TB/gLb", glabel.properties))

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
def print_hierarchicallabels(hlabels, printout = False):
    output_text: list[str] = []

    loop = 0

    for hlabel in hlabels:
        output_text.extend(print_data("sym/TB/hLb/text  : ", hlabel.text))
        output_text.extend(print_data("sym/TB/hLb/shape : ", hlabel.shape))
        output_text.extend(print_data("sym/TB/hLb/pos   : ", hlabel.position))

        output_text.extend(print_effects("sym/TB/hLb", hlabel.effects))

        output_text.extend(print_data("sym/TB/hLb/uuid  : ", hlabel.uuid))
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
def print_sheets(sheets, printout=False):
    output_text: list[str] = []

    loop = 0

    for sheet in sheets:
        output_text.extend(print_data("sym/TB/sht/pos   : ", sheet.position))
        output_text.extend(print_data("sym/TB/sht/width : ", sheet.width))
        output_text.extend(print_data("sym/TB/sht/height: ", sheet.height))
        output_text.extend(print_data("sym/TB/sht/fieAut: ", sheet.fieldsAutoplaced))
        output_text.extend(print_data("sym/TB/sht/stroke: ", sheet.stroke))
        output_text.extend(print_data("sym/TB/sht/fill  : ", sheet.fill))
        output_text.extend(print_data("sym/TB/sht/uuid  : ", sheet.uuid))

        if not (sheet.sheetName is None):
            output_text.extend(print_data("sym/TB/shtNam/val: ", sheet.sheetName.value))
            output_text.extend(print_data("sym/TB/shtNam/key: ", sheet.sheetName.key))

        if not (sheet.fileName is None):
            output_text.extend(print_data("sym/TB/shtfNm/val: ", sheet.fileName.value))
            output_text.extend(print_data("sym/TB/shtfNm/key: ", sheet.fileName.key))

        for pin in sheet.pins:
            output_text.extend(print_data("sym/TB/sht/piname: ", pin.name))
            output_text.extend(print_data("sym/TB/sht/picoTy: ", pin.connectionType))
            output_text.extend(print_data("sym/TB/sht/pipos : ", pin.position))

            output_text.extend(print_effects("sym/TB/sht", pin.effects))

            output_text.extend(print_data("sym/TB/sht/piuuid: ", pin.uuid))
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
def print_sheetinstances(sheetinstances, printout=False):
    output_text: list[str] = []

    loop = 0

    for sheetinstance in sheetinstances:
        output_text.extend(print_data("sym/TB/sIns/instP: ", sheetinstance.instancePath))
        output_text.extend(print_data("sym/TB/sIns/page : ", sheetinstance.page))
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
def print_symbolinstance(symbolinstances, printout=False):
    output_text: list[str] = []

    loop = 0

    for symbolinstance in symbolinstances:
        output_text.extend(print_data("sym/TB/symS/path : ", symbolinstance.path))
        output_text.extend(print_data("sym/TB/symS/ref  : ", symbolinstance.reference))
        output_text.extend(print_data("sym/TB/symS/unit : ", symbolinstance.unit))
        output_text.extend(print_data("sym/TB/symS/value: ", symbolinstance.value))
        output_text.extend(print_data("sym/TB/symS/footP: ", symbolinstance.footprint))
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
def print_schematic(schematicname, schematic, printout=False):
    output_text: list[str] = [print_data("sym/vers         : ", schematic.version),
                              print_data("sym/gen          : ", schematic.generator),
                              print_data("sym/uuid         : ", schematic.uuid, True),
                              print_data("sym/paper        : ", schematic.paper)]

    if not (schematic.titleBlock is None):
        output_text.extend(print_data("sym/TB/title     : ", schematic.titleBlock.title, True))

        output_text.extend(print_data("sym/TB/date      : ", schematic.titleBlock.date, True))
        output_text.extend(print_data("sym/TB/rev       : ", schematic.titleBlock.revision, True))
        output_text.extend(print_data("sym/TB/company   : ", schematic.titleBlock.company, True))

        if len(schematic.titleBlock.comments) > 0:
            for key, value in schematic.titleBlock.comments.items():
                output_text.extend(print_data("sym/TB/com/value : ", value))
                output_text.extend(print_data("sym/TB/com/key   : ", key))

    output_text.extend(print_libsymbols(schematic.libSymbols))
    output_text.extend(print_schematicsymbols(schematic.schematicSymbols))
    output_text.extend(print_junctions(schematic.junctions))
    output_text.extend(print_noconnects(schematic.noConnects))
    output_text.extend(print_busentries(schematic.busEntries))
    output_text.extend(print_connections(schematic.graphicalItems))
    output_text.extend(print_images(schematic.images))
    output_text.extend(print_texts(schematic.texts))
    output_text.extend(print_locallabels(schematic.labels))
    output_text.extend(print_globallabels(schematic.globalLabels))
    output_text.extend(print_hierarchicallabels(schematic.hierarchicalLabels))
    output_text.extend(print_sheets(schematic.sheets))
    output_text.extend(print_sheetinstances(schematic.sheetInstances))
    output_text.extend(print_symbolinstance(schematic.symbolInstances))

    output_text.extend(print_data("sym/filePath     : ", schematic.filePath, True))

    if printout:
        textbox("Details for Schematic " + schematicname, "Schematic", output_text, False)
        return ""
    else:
        return output_text
