#  ===================================================================
#  Source File Name : user_display.py
#  Purpose          : Common display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

from easygui import *
import tkinter as tk
import os

from debug_print import *


def user_selection(msg, selection):
    if not selection:
        # There is nothing to select (except exit). Need to do this as choicebox does not operate with 1 entry!
        display_msg = "Exit (and save output)? \n\r \n\rNOTE: Select \"Cancel\" to quit (without saving)."
        display_title = msg + " action(s)"

        # Swapped Cancel/Ok round to make it consistant with choicebox
        choice = ccbox(msg            = display_msg,
                       title          = display_title,
                       choices        = ("Cancel", "Ok"))

        # if choice is None then selected cancel (which is effectively quit)
        if not choice:
            return "Exit"                                                 # Finished selecting tasks.
        else:
            return "Quit"                                                 # Do nothing.

    else:
        # There are thing to select!
        display_msg = "What " + msg + " related task do you want to perform? \n\r \n\rNOTE: Select \"Cancel\" to quit (" \
                                      "without saving)."
        display_title = msg + " action(s)"
        selection_length = len(selection) + 1

        display_selection = selection.copy()

        position = 0

        for entry in display_selection:
            display_selection[position] = "Task " + str(position + 1) + ": " + entry
            position += 1

        display_selection.append("Task " + str(position + 1) + ": Exist (and save output)")

        choice = choicebox(display_msg, display_title, display_selection)

        # if choice is None then selected cancel (which is effectively quit)
        if choice is None:
            return "Quit"                                                 # Do nothing.
        elif choice[5:choice.find(":")] == str(len(display_selection)): # Last entry
            return "Exit"                                                 # Finished selecting tasks.
        else:
            return choice[0:choice.find(":")]                             # Return User selection