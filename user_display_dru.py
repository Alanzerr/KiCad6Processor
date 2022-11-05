#  ===================================================================
#  Source File Name : user_display_dru.py
#  Purpose          : Design Rules specific display tasks.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os

from user_display import *


# ==================================================================================================================
def print_contraints(constraints, printout=False):
    output_text: list[str] = []

    loop = 0

    for constraint in constraints:
        output_text.extend(print_data("dru/rules/const  : ", str(loop + 1)))
        output_text.extend(print_data("dru/rules/cst/typ: ", constraint.type))
        output_text.extend(print_data("dru/rules/cst/min: ", constraint.min, True))
        output_text.extend(print_data("dru/rules/cst/opt: ", constraint.opt, True))
        output_text.extend(print_data("dru/rules/cst/max: ", constraint.max, True))

        for element in constraint.elements:
            output_text.extend(print_data("dru/rules/cst/ele: ", element, True))
        loop += 1

    if printout:
        textbox("Details for Constraints ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_rules(rules, printout=False):
    output_text: list[str] = []

    loop = 0

    for rule in rules:
        output_text.extend(print_data("dru/rules        : ", str(loop + 1)))
        output_text.extend(print_data("dru/rules/name   : ", rule.name))

        output_text.extend(print_contraints(rule.constraints))

        output_text.extend(print_data("dru/rules/cond   : ", rule.condition))
        output_text.extend(print_data("dru/rules/layer  : ", rule.layer, True))
        loop += 1

    if printout:
        textbox("Details for Rules ", output_text, False)
        return ""
    else:
        if loop == 0:
            return ""
        else:
            return output_text


# ==================================================================================================================
def print_designrules(druname, dru, printout=False):
    output_text: list[str] = [print_data("dru              : ", dru.version)]

    output_text.extend(print_rules(dru.rules))

    if printout:
        textbox("Details for Design Rules " + druname, "Design Rules", output_text, False)
        return ""
    else:
        return output_text
