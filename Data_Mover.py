#  ===================================================================
#  Source File Name : Data_Mover.py
#  Purpose          : Routines to move artefacts about
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# import os
import math
# import datetime

# from kiutils.board import *
# from kiutils.libraries import *

# from debug_print import *
# from user_display_libtable import *
# from user_display_footprint import *
from Supplemental_Classes import *


# ==================================================================================================================
# Returns the multiplication factor base on the value of flip
def flipped(flip):
    if flip:
        return -1
    else:
        return 1


# ==================================================================================================================
# Returns the multiplication factor base on the value of flip
def not_flipped(flip):
    if flip:
        return 1
    else:
        return -1


# ==================================================================================================================
# (Simple) Offset the point
def pt_soff(position, centroid_offset):
    pos = Position(X        = position.X - centroid_offset.X,
                   Y        = position.Y - centroid_offset.Y,
                   angle    = position.angle,
                   unlocked = position.unlocked)
    return pos


# ==================================================================================================================
# Offset the point, but based on a vector!
# TODO: Could improve this - see https://stackoverflow.com/questions/55948254/scale-contours-up-grow-outward
# This is not a perfect approach as for a rectangle, it grows more in the long direction than in the short.
def pt_coff(position, centroid_offset, layer):
    match layer:
        case "F.CrtYd":
            offset = 2.54  # This is set to 0.1" or 2.54 mm. Can't find anything to say that use of mm is wrong.
        case "F.SilkS":
            offset = 1.5  # This is set to 0.1" or 2.54 mm. Can't find anything to say that use of mm is wrong.
        case _:
            offset = 0.001  # non-zero to make maths work

    # calculate the new position based on the centroid offset
    orig_pos = pt_soff(position, centroid_offset)

    # calculate the distance based on the pos x and Y and Pythagoras
    distance = math.sqrt((orig_pos.X ** 2) + (orig_pos.Y ** 2))

    # determine the new x,y
    new_pos = Position(X        = ((offset / distance) * orig_pos.X) + orig_pos.X,
                       Y        = ((offset / distance) * orig_pos.Y) + orig_pos.Y,
                       angle    = position.angle,
                       unlocked = position.unlocked)
    return new_pos


# ==================================================================================================================
def new_coordinate_position(fp_position, pad_position, aux_data):
    new_position = Position()

    # update position based on having moved the centroid to 0,0
    position = pt_soff(fp_position, aux_data.centroid_offset)

    match fp_position.angle:
        case 90.0:
            if aux_data.board_flip:
                new_position.X     = ((position.X + aux_data.center.Y) + (pad_position.Y - aux_data.center.Y))
                new_position.Y     = ((position.Y - aux_data.center.X) - (pad_position.X - aux_data.center.X)) * flipped(aux_data.board_flip)
                new_position.angle =   fp_position.angle
            else:
                new_position.X     = ((position.X + aux_data.center.Y) + (pad_position.Y - aux_data.center.Y))
                new_position.Y     = ((position.Y - aux_data.center.X) - (pad_position.X - aux_data.center.X))
                new_position.angle =   fp_position.angle

        case -90.0:
            if aux_data.board_flip:
                new_position.X     = ((position.X - aux_data.center.Y) - (pad_position.Y - aux_data.center.Y))
                new_position.Y     = ((position.Y + aux_data.center.X) + (pad_position.X - aux_data.center.X)) * flipped(aux_data.board_flip)
                new_position.angle =   fp_position.angle
            else:
                new_position.X     = ((position.X - aux_data.center.Y) - (pad_position.Y - aux_data.center.Y))
                new_position.Y     = ((position.Y + aux_data.center.X) + (pad_position.X - aux_data.center.X))
                new_position.angle =   fp_position.angle

        case 180.0:
            if aux_data.board_flip:
                new_position.X     = ((position.X - aux_data.center.X) - (pad_position.X - aux_data.center.X))
                new_position.Y     = ((position.Y - aux_data.center.Y) - (pad_position.Y - aux_data.center.Y)) * flipped(aux_data.board_flip)
                new_position.angle =   fp_position.angle
            else:
                new_position.X     = ((position.X - aux_data.center.X) - (pad_position.X - aux_data.center.X))
                new_position.Y     = ((position.Y - aux_data.center.Y) - (pad_position.Y - aux_data.center.Y))
                new_position.angle =   fp_position.angle

        case _:  # angle is 0.0
            if aux_data.board_flip:
                new_position.X     = ((position.X + aux_data.center.X) + (pad_position.X - aux_data.center.X))
                new_position.Y     = ((position.Y + aux_data.center.Y) + (pad_position.Y - aux_data.center.Y)) * flipped(aux_data.board_flip)
                new_position.angle =   fp_position.angle
            else:
                new_position.X     = ((position.X + aux_data.center.X) + (pad_position.X - aux_data.center.X))
                new_position.Y     = ((position.Y + aux_data.center.Y) + (pad_position.Y - aux_data.center.Y))
                new_position.angle =   fp_position.angle

    return new_position


# ==================================================================================================================
def new_model_position(fp_position, model, model_path, fp_offset, board_flip):
    # update position based on having moved the centroid to 0,0
    position = pt_soff(fp_position, fp_offset)

    # Deal with rotation and offset on pad
    match fp_position.angle:
        case 90.0:
            if board_flip:
                new_rotation = model.rotate.Z - 90
            else:
                new_rotation = model.rotate.Z + 90

            new_model = Model(path   = model_path,
                              pos    = Coordinate(X = position.X,
                                                  Y = position.Y * not_flipped(board_flip),
                                                  Z = model.pos.Z),
                              scale  = model.scale,
                              rotate = Coordinate(X = model.rotate.X,
                                                  Y = model.rotate.Y,
                                                  Z = new_rotation))

        case 180.0:
            if board_flip:
                new_rotation = model.rotate.Z + 0
            else:
                new_rotation = model.rotate.Z + 0

            new_model = Model(path   = model_path,
                              pos    = Coordinate(X = position.X,
                                                  Y = position.Y * not_flipped(board_flip),
                                                  Z = model.pos.Z),
                              scale  = model.scale,
                              rotate = Coordinate(X = model.rotate.X,
                                                  Y = model.rotate.Y,
                                                  Z = new_rotation))

        case -90.0:
            if board_flip:
                new_rotation = model.rotate.Z + 90
            else:
                new_rotation = model.rotate.Z - 90

            new_model = Model(path   = model_path,
                              pos    = Coordinate(X = position.X,
                                                  Y = position.Y * not_flipped(board_flip),
                                                  Z = model.pos.Z),
                              scale  = model.scale,
                              rotate = Coordinate(X = model.rotate.X,
                                                  Y = model.rotate.Y,
                                                  Z = new_rotation))

        case _:  # angle is 0.0
            if board_flip:
                new_rotation = model.rotate.Z + 180
            else:
                new_rotation = model.rotate.Z + 180

            new_model = Model(path   = model_path,
                              pos    = Coordinate(X = position.X,
                                                  Y = position.Y * not_flipped(board_flip),
                                                  Z = model.pos.Z),
                              scale  = model.scale,
                              rotate = Coordinate(X = model.rotate.X,
                                                  Y = model.rotate.Y,
                                                  Z = new_rotation))

    return new_model
