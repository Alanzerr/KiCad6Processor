#  ===================================================================
#  Source File Name : kicad_dru.py
#  Purpose          : Process KiCad6 Design Rules (for PCB).
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

import os

from kiutils.dru import Constraint
from kiutils.dru import DesignRules
from kiutils.dru import Rule

from debug_print import *
from user_display_dru import *


# ==================================================================================================================
def process_kicad_dru(fdir, fname, fext):
    filename = fdir + fname + fext

    # Create new sub-folder (if it does not exist  for the output
    sub_folder = "Modified"
    if not os.path.exists(os.path.join(fdir, sub_folder)):
        os.mkdir(os.path.join(fdir, sub_folder))

    new_filename = fdir + sub_folder + "\\" + fname + fext

    debug_print("KiCad Design Rule filename is %s." % filename)

    designrules = DesignRules().from_file(filename)

    print_designrules(fname, designrules, True)

    # Now ask user what they want to do and keep doing it till they quit (via cancel if "x")
    choice = None

    while (choice != "Quit") and (choice != "Exit"):
        msg = "Design Rule(s)"

        choices = list()
        choices.append("TestBed")    # Task 1

        choice = user_selection(msg, choices)

        match choice:
            case "Task 1":
                debug_print("User selected %s." % choice)

                print("Version    \"%s.\"" % designrules.version)

                if designrules.rules is None:
                    print("No Design Rules to report.")
                else:
                    loop1 = 1
                    for rule in designrules.rules:
                        print("===================================================================")

                        print("Name %i      \"%s.\"" % (loop1, rule.name))

                        print("Condition %i \"%s.\"" % (loop1, rule.condition))
                        loop1 += 2

                        if rule.layer is None:
                            print("No Layers to report.")
                        else:
                            print("===================================================================")

                            loop2 = 1
                            for layer in rule.layer:
                                print("Layer %i    \"%s.\"" % (loop2, layer))
                                loop2 += 1

                        if rule.constraints is None:
                            print("No Contraints to report.")
                        else:
                            print("===================================================================")

                            loop3 = 1
                            for contraint in rule.constraints:
                                print("Type %i      \"%s.\"" % (loop3, contraint.type))
                                print("Min %i       \"%s.\"" % (loop3, contraint.min))
                                print("Opt %i       \"%s.\"" % (loop3, contraint.opt))
                                print("Max %i       \"%s.\"" % (loop3, contraint.max))
                                loop3 += 1

                                if contraint is None:
                                    print("No Contraints to report.")
                                else:
                                    loop4 = 1
                                    print("===================================================================")

                                    for element in contraint.elements:
                                        print("Element %i   \"%s.\"" % (loop4, element))
                                        loop4 += 1

                # ==== Experiment here ====

                minimum: list[str] = ["0.5", "1.0"]

                constraint: list[str]  = [Constraint(type="Ping", min=minimum)]

                layers: list[str]  = ["F.Cu", "B.Cu"]

                designrules.rules.append(Rule(name="Hello", condition="Test", layer=layers, constraints=constraint))

                # ==== Experiment here ====

                print("Version    \"%s.\"" % designrules.version)

                if designrules.rules is None:
                    print("No Design Rules to report.")
                else:
                    loop1 = 1
                    for rule in designrules.rules:
                        print("===================================================================")

                        print("Name %i      \"%s.\"" % (loop1, rule.name))

                        print("Condition %i \"%s.\"" % (loop1, rule.condition))
                        loop1 += 1

                        if rule.layer is None:
                            print("No Layers to report.")
                        else:
                            print("===================================================================")

                            loop2 = 1
                            for layer in rule.layer:
                                print("Layer %i    \"%s.\"" % (loop2, layer))
                                loop2 += 1

                        if rule.constraints is None:
                            print("No Contraints to report.")
                        else:
                            print("===================================================================")

                            loop3 = 1
                            for contraint in rule.constraints:
                                print("Type %i      \"%s.\"" % (loop3, contraint.type))
                                print("Min %i       \"%s.\"" % (loop3, contraint.min))
                                print("Opt %i       \"%s.\"" % (loop3, contraint.opt))
                                print("Max %i       \"%s.\"" % (loop3, contraint.max))
                                loop3 += 1

                                if contraint is None:
                                    print("No Contraints to report.")
                                else:
                                    loop4 = 1
                                    print("===================================================================")

                                    for element in contraint.elements:
                                        print("Element %i   \"%s.\"" % (loop4, element))
                                        loop4 += 1

                designrules.to_file(new_filename)

                msgbox(msg="KiCad Input file " + filename + " has been processed.\n\r \n\rProcessed file is " + new_filename + ".",
                       title="KiCad Design Rules file",
                       ok_button="Exit function")

            case "Quit":
                # User has selected cancel so nothing to do
                debug_print("User selected Quit.")
            case "Exit":
                debug_print("User selected Exit.")
