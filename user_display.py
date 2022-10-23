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

    elif isinstance(data, Effects):
        if newline:
            return prefix + str(data.font) + "\n" + prefix + str(data.justify) + "," + str(data.hide)
        else:
            return "\n" + prefix + str(data.font) + "\n" + prefix + str(data.justify) + "," + str(data.hide)

    elif isinstance(data, Stroke):
        if newline:
            return prefix + str(data.width) + " " + data.type + "\n" + prefix  + str(data.color)
        else:
            return "\n" + prefix + str(data.width) + " " + data.type + "\n" + prefix  + str(data.color)

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
