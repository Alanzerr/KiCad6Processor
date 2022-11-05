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
            output_text.extend(print_data("wks/Line/name    : ", object.name))
            output_text.extend(print_data("wks/Line/start   : ", object.start))
            output_text.extend(print_data("wks/Line/end     : ", object.end))
            output_text.extend(print_data("wks/Line/option  : ", object.option, True))
            output_text.extend(print_data("wks/Line/linewidt: ", object.lineWidth, True))
            output_text.extend(print_data("wks/Line/repeat  : ", object.repeat, True))
            output_text.extend(print_data("wks/Line/incrx   : ", object.incrx, True))
            output_text.extend(print_data("wks/Line/incry   : ", object.incry, True))
            output_text.extend(print_data("wks/Line/comment : ", object.comment, True))

        elif isinstance(object, Rect):
            output_text.extend(print_data("wks/Rect/name    : ", object.name))
            output_text.extend(print_data("wks/Rect/start   : ", object.start))
            output_text.extend(print_data("wks/Rect/end     : ", object.end))
            output_text.extend(print_data("wks/Rect/option  : ", object.option, True))
            output_text.extend(print_data("wks/Rect/lineWidt: ", object.lineWidth, True))
            output_text.extend(print_data("wks/Rect/repeat  : ", object.repeat, True))
            output_text.extend(print_data("wks/Rect/incrx   : ", object.incrx, True))
            output_text.extend(print_data("wks/Rect/incry   : ", object.incry, True))
            output_text.extend(print_data("wks/Rect/comment : ", object.comment, True))

        elif isinstance(object, Polygon):
            output_text.extend(print_data("wks/Poly/name    : ", object.name))
            output_text.extend(print_data("wks/Rect/position: ", object.position))
            output_text.extend(print_data("wks/Rect/option  : ", object.option, True))
            output_text.extend(print_data("wks/Rect/rotate  : ", object.rotate, True))

            for coord in object.coordinates:
                output_text.extend(print_data("wks/Rect/name    : ", coord))

            output_text.extend(print_data("wks/Rect/repeat  : ", object.repeat, True))
            output_text.extend(print_data("wks/Rect/incrx   : ", object.incrx, True))
            output_text.extend(print_data("wks/Rect/incry   : ", object.incry, True))
            output_text.extend(print_data("wks/Rect/comment : ", object.comment, True))

        elif isinstance(object, Bitmap):
            output_text.extend(print_data("wks/Bmap/name    : ", object.name))
            output_text.extend(print_data("wks/Bmap/position: ", object.position))
            output_text.extend(print_data("wks/Bmap/option  : ", object.option, True))
            output_text.extend(print_data("wks/Bmap/scale   : ", object.scale))
            output_text.extend(print_data("wks/Bmap/repeat  : ", object.repeat, True))
            output_text.extend(print_data("wks/Bmap/incrx   : ", object.incrx, True))
            output_text.extend(print_data("wks/Bmap/incry   : ", object.incry, True))
            output_text.extend(print_data("wks/Bmap/comment : ", object.comment, True))

            for data in object.pngdata:
                output_text.extend(print_data("wks/Bmap/pngdata : ", data))

        elif isinstance(object, TbText):
            output_text.extend(print_data("wks/Text/text    : ", object.text))
            output_text.extend(print_data("wks/Text/name    : ", object.name))
            output_text.extend(print_data("wks/Text/position: ", object.position))
            output_text.extend(print_data("wks/Text/option  : ", object.option, True))
            output_text.extend(print_data("wks/Text/rotate  : ", object.rotate, True))

            output_text.extend(print_data("wks/Text/font/lwi: ", object.font.linewidth, True))

            if not (object.font.size is None):
                output_text.extend(print_data("wks/Text/font/wid: ", object.font.size.width))
                output_text.extend(print_data("wks/Text/font/hei: ", object.font.size.height))

            output_text.extend(print_data("wks/Text/font/bld: ", object.font.bold))
            output_text.extend(print_data("wks/Text/font/ita: ", object.font.italic))

            if not (object.justify is None):
                output_text.extend(print_data("wks/Text/jst/hor : ", object.justify.horizontally, True))
                output_text.extend(print_data("wks/Text/jst/ver : ", object.justify.vertically, True))
                output_text.extend(print_data("wks/Text/jst/mir : ", object.justify.mirror))

            output_text.extend(print_data("wks/Text/maxlen  : ", object.maxlen, True))
            output_text.extend(print_data("wks/Text/maxheigh: ", object.maxheight, True))
            output_text.extend(print_data("wks/Text/repeat  : ", object.repeat, True))
            output_text.extend(print_data("wks/Text/incrx   : ", object.incrx, True))
            output_text.extend(print_data("wks/Text/incry   : ", object.incry, True))
            output_text.extend(print_data("wks/Text/inclabel: ", object.incrlabel, True))
            output_text.extend(print_data("wks/Text/comment : ", object.comment, True))

        loop += 1

    if printout:
        textbox("Details for Objects ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_worksheet(wksname, wks, printout=False):
    output_text: list[str] = [print_data("wks/version      : ", wks.version),
                              print_data("wks/generator    : ", wks.generator),
                              print_data("wks/setup/txtsize: ", wks.setup.textSize),
                              print_data("wks/setup/linewid: ", wks.setup.lineWidth),
                              print_data("wks/setup/tlinewd: ", wks.setup.textLineWidth),
                              print_data("wks/setup/lmargin: ", wks.setup.leftMargin),
                              print_data("wks/setup/rmargin: ", wks.setup.rightMargin),
                              print_data("wks/setup/tmargin: ", wks.setup.topMargin),
                              print_data("wks/setup/bmargin: ", wks.setup.bottomMargin)]

    output_text.extend(print_objects(wks.drawingObjects))

    output_text.extend(print_data("wks/filepath     : ", wks.filePath))

    if printout:
        textbox("Details for Worksheet " + wksname, "Worksheet", output_text, False)
        return ""
    else:
        return output_text
