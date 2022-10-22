#  ===================================================================
#  Source File Name : debug_print.py
#  Purpose          : Simple way to selectively print stuff.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# Set to 0 to disable print to console and 1 to enable.
PRINT = 0


# ==================================================================================================================
def debug_print(text):
    if PRINT == 1:
        print(text)
