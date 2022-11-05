#  ===================================================================
#  Source File Name : user_display_pcblibtable.py
#  Purpose          : PCB Lib Table specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_libtable(libtablename, libtable, printout=False):
    output_text: list[str] = [print_data("libtbl/type      : ", libtable.type)]

    for lib in libtable.libs:
        output_text.extend(print_data("libtbl/Lib/name  : ", lib.name))
        output_text.extend(print_data("libtbl/Lib/type  : ", lib.type))
        output_text.extend(print_data("libtbl/Lib/uri   : ", lib.uri))
        output_text.extend(print_data("libtbl/Lib/option: ", lib.options))
        output_text.extend(print_data("libtbl/Lib/desc  : ", lib.description))

    output_text.extend(print_data("libtbl/filePath  : ", libtable.filePath))

    if printout:
        textbox("Details for Symbol Lib Table " + libtablename, "Symbol Lib Table", output_text, False)
        return ""
    else:
        return output_text
