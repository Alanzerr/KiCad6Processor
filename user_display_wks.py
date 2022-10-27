#  ===================================================================
#  Source File Name : user_display_wks.py
#  Purpose          : Worksheet specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_objects(objects, printout=False):
    output_text: list[str] = []

    loop = 0

    for object in objects:
        if isinstance(object, Line):
            output_text.append(merge_data(False, False, " wks/Line/name    : ", object.name))
            output_text.append(merge_data(False, False, " wks/Line/start   : ", object.start))
            output_text.append(merge_data(False, False, " wks/Line/end     : ", object.end))
            output_text.append(merge_data(True,  False, "*wks/Line/option  : ", object.option))
            output_text.append(merge_data(True,  False, "*wks/Line/linewidt: ", object.lineWidth))
            output_text.append(merge_data(True,  False, "*wks/Line/repeat  : ", object.repeat))
            output_text.append(merge_data(True,  False, "*wks/Line/incrx   : ", object.incrx))
            output_text.append(merge_data(True,  False, "*wks/Line/incry   : ", object.incry))
            output_text.append(merge_data(True,  False, "*wks/Line/comment : ", object.comment))

        elif isinstance(object, Rect):
            output_text.append(merge_data(False, False, " wks/Rect/name    : ", object.name))
            output_text.append(merge_data(False, False, " wks/Rect/start   : ", object.start))
            output_text.append(merge_data(False, False, " wks/Rect/end     : ", object.end))
            output_text.append(merge_data(True,  False, "*wks/Rect/option  : ", object.option))
            output_text.append(merge_data(True,  False, "*wks/Rect/lineWidt: ", object.lineWidth))
            output_text.append(merge_data(True,  False, "*wks/Rect/repeat  : ", object.repeat))
            output_text.append(merge_data(True,  False, "*wks/Rect/incrx   : ", object.incrx))
            output_text.append(merge_data(True,  False, "*wks/Rect/incry   : ", object.incry))
            output_text.append(merge_data(True,  False, "*wks/Rect/comment : ", object.comment))

        elif isinstance(object, Polygon):
            output_text.append(merge_data(False, False, " wks/Poly/name    : ", object.name))
            output_text.append(merge_data(False, False, " wks/Rect/position: ", object.position))
            output_text.append(merge_data(True,  False, "*wks/Rect/option  : ", object.option))
            output_text.append(merge_data(True,  False, "*wks/Rect/rotate  : ", object.rotate))

            for coord in object.coordinates:
                output_text.append(merge_data(False, False, " wks/Rect/name    : ", coord))

            output_text.append(merge_data(True,  False, "*wks/Rect/repeat  : ", object.repeat))
            output_text.append(merge_data(True,  False, "*wks/Rect/incrx   : ", object.incrx))
            output_text.append(merge_data(True,  False, "*wks/Rect/incry   : ", object.incry))
            output_text.append(merge_data(True,  False, "*wks/Rect/comment : ", object.comment))

        elif isinstance(object, Bitmap):
            output_text.append(merge_data(False, False, " wks/Bmap/name    : ", object.name))
            output_text.append(merge_data(False, False, " wks/Bmap/position: ", object.position))
            output_text.append(merge_data(True,  False, "*wks/Bmap/option  : ", object.option))
            output_text.append(merge_data(False, False, " wks/Bmap/scale   : ", object.scale))
            output_text.append(merge_data(True,  False, "*wks/Bmap/repeat  : ", object.repeat))
            output_text.append(merge_data(True,  False, "*wks/Bmap/incrx   : ", object.incrx))
            output_text.append(merge_data(True,  False, "*wks/Bmap/incry   : ", object.incry))
            output_text.append(merge_data(True,  False, "*wks/Bmap/comment : ", object.comment))

            for data in object.pngdata:
                output_text.append(merge_data(False, False, " wks/Bmap/pngdata : ", data))

        elif isinstance(object, TbText):
            output_text.append(merge_data(False, False, " wks/Text/text    : ", object.text))
            output_text.append(merge_data(False, False, " wks/Text/name    : ", object.name))
            output_text.append(merge_data(False, False, " wks/Text/position: ", object.position))
            output_text.append(merge_data(True,  False, "*wks/Text/option  : ", object.option))
            output_text.append(merge_data(True,  False, "*wks/Text/rotate  : ", object.rotate))

            output_text.append(merge_data(True,  False, "*wks/Text/font/lwi: ", object.font.linewidth))

            if not (object.font.size is None):
                output_text.append(merge_data(False, False, " wks/Text/font/wid: ", object.font.size.width))
                output_text.append(merge_data(False, False, " wks/Text/font/hei: ", object.font.size.height))

            output_text.append(merge_data(False, False, " wks/Text/font/bld: ", object.font.bold))
            output_text.append(merge_data(False, False, " wks/Text/font/ita: ", object.font.italic))

            if not (object.justify is None):
                output_text.append(merge_data(True,  False, "*wks/Text/jst/hor : ", object.justify.horizontally))
                output_text.append(merge_data(True,  False, "*wks/Text/jst/ver : ", object.justify.vertically))
                output_text.append(merge_data(False, False, " wks/Text/jst/mir : ", object.justify.mirror))

            output_text.append(merge_data(True,  False, "*wks/Text/maxlen  : ", object.maxlen))
            output_text.append(merge_data(True,  False, "*wks/Text/maxheigh: ", object.maxheight))
            output_text.append(merge_data(True,  False, "*wks/Text/repeat  : ", object.repeat))
            output_text.append(merge_data(True,  False, "*wks/Text/incrx   : ", object.incrx))
            output_text.append(merge_data(True,  False, "*wks/Text/incry   : ", object.incry))
            output_text.append(merge_data(True,  False, "*wks/Text/inclabel: ", object.incrlabel))
            output_text.append(merge_data(True,  False, "*wks/Text/comment : ", object.comment))

        loop += 1

    if printout:
        textbox("Details for Objects ", output_text, False)
        return None
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_worksheet(wksname, wks, printout=False):
    output_text: list[str] = [merge_data(False, False, " wks/version      : ", wks.version),
                              merge_data(False, False, " wks/generator    : ", wks.generator),
                              merge_data(False, False, " wks/setup/txtsize: ", wks.setup.textSize),
                              merge_data(False, False, " wks/setup/linewid: ", wks.setup.lineWidth),
                              merge_data(False, False, " wks/setup/tlinewd: ", wks.setup.textLineWidth),
                              merge_data(False, False, " wks/setup/lmargin: ", wks.setup.leftMargin),
                              merge_data(False, False, " wks/setup/rmargin: ", wks.setup.rightMargin),
                              merge_data(False, False, " wks/setup/tmargin: ", wks.setup.topMargin),
                              merge_data(False, False, " wks/setup/bmargin: ", wks.setup.bottomMargin)]

    output_text.extend(print_objects(wks.drawingObjects))

    output_text.append(merge_data(False, False, " wks/filepath     : ", wks.filePath))

    if printout:
        textbox("Details for Worksheet " + wksname, "Worksheet", output_text, False)
        return None
    else:
        return output_text
