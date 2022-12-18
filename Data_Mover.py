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

from debug_print import *
# from user_display_libtable import *
# from user_display_footprint import *
from Supplemental_Classes import *


# ==================================================================================================================
def calc_circle(point1, point2, point3):
    circle = Circle()

    # Returns the center and radius of the circle passing the given 3 points.
    # In case the 3 points form a line, returns (None, infinity).
    temp = point2.X ** 2 + point2.Y ** 2
    bc = (point1.X ** 2 + point1.Y ** 2 - temp) / 2
    cd = (temp - point3.X ** 2 - point3.Y ** 2) / 2
    det = (point1.X - point2.X) * (point2.Y - point3.Y) - (point2.X - point3.X) * (point1.Y - point2.Y)

    if abs(det) < 1.0e-10:
        return None

    # Center of circle
    circle.center = Coordinate(X = round(((bc * (point2.Y - point3.Y) - cd * (point1.Y - point2.Y)) / det), 6),
                               Y = round((((point1.X - point2.X) * cd - (point2.X - point3.X) * bc) / det), 6))

    circle.radius = round((((circle.center.X - point1.X) ** 2 + (circle.center.Y - point1.Y) ** 2) ** 0.5), 6)

    return circle


# ==================================================================================================================
# Runs through the graphical items and finds the geometric center.
def find_centroid(gr_items):
    extends_top_right   = Position(X        = 0.0,
                                   Y        = 0.0,
                                   angle    = 0.0,
                                   unlocked = True)  # If false then this needs processed, otherwise it's the first point.

    extends_bottom_left = Position(X        = 0.0,
                                   Y        = 0.0,
                                   angle    = 0.0,
                                   unlocked = True)  # Just ignore this.

    for gitem in gr_items:
        top_right   = Position(X        = 0.0,
                               Y        = 0.0,
                               angle    = 0.0,
                               unlocked = True)  # If false then this needs processed, otherwise ignore.

        bottom_left = Position(X        = 0.0,
                               Y        = 0.0,
                               angle    = 0.0,
                               unlocked = True)  # DO not use this so "True" so that it is ignored.

        # Don't worry about text and textbox
        if isinstance(gitem, GrLine):
            if gitem.layer == "Edge.Cuts":
                if gitem.start.X > gitem.end.X:
                    top_right.X   = gitem.start.X
                    bottom_left.X = gitem.end.X
                else:
                    top_right.X   = gitem.end.X
                    bottom_left.X = gitem.start.X

                if gitem.start.Y > gitem.end.Y:
                    top_right.Y   = gitem.start.Y
                    bottom_left.Y = gitem.end.Y
                else:
                    top_right.Y   = gitem.end.Y
                    bottom_left.Y = gitem.start.Y

                bottom_left.unlocked = True
                top_right.unlocked   = False

                debug_print("Line   " + str(top_right) + " " + str(bottom_left))

        elif isinstance(gitem, GrRect):
            if gitem.layer == "Edge.Cuts":
                if gitem.start.X > gitem.end.X:
                    top_right.X   = gitem.start.X
                    bottom_left.X = gitem.end.X
                else:
                    top_right.X   = gitem.end.X
                    bottom_left.X = gitem.start.X

                if gitem.start.Y > gitem.end.Y:
                    top_right.Y   = gitem.start.Y
                    bottom_left.Y = gitem.end.Y
                else:
                    top_right.Y   = gitem.end.Y
                    bottom_left.Y = gitem.start.Y

                bottom_left.unlocked = True
                top_right.unlocked   = False

                debug_print("Rect   " + str(top_right) + " " + str(bottom_left))

        elif isinstance(gitem, GrCircle):
            if gitem.layer == "Edge.Cuts":
                # use Pythagoras to determine the radius
                a = round(gitem.center.X - gitem.end.X, 6)
                b = round(gitem.center.Y - gitem.end.Y, 6)

                radius = round(math.sqrt(pow(a, 2) + pow(b, 2)), 6)

                bottom_left.X        = gitem.center.X - radius
                bottom_left.Y        = gitem.center.Y - radius
                bottom_left.unlocked = True

                top_right.X          = gitem.center.X + radius
                top_right.Y          = gitem.center.Y + radius
                top_right.unlocked   = False

                debug_print("Circle " + str(top_right) + " " + str(bottom_left))

        elif isinstance(gitem, GrArc):
            if gitem.layer == "Edge.Cuts":
                # For simplicity, determine the circle based on the arc and us it!
                point1 = Coordinate(X = gitem.start.X,
                                    Y = gitem.start.Y,
                                    Z = 0.0)

                point2 = Coordinate(X = gitem.mid.X,
                                    Y = gitem.mid.Y,
                                    Z = 0.0)

                point3 = Coordinate(X = gitem.end.X,
                                    Y = gitem.end.Y,
                                    Z = 0.0)

                circle = calc_circle(point1, point2, point3)

                bottom_left.X        = round(circle.center.X - circle.radius, 6)
                bottom_left.Y        = round(circle.center.Y - circle.radius, 6)
                bottom_left.unlocked = True

                top_right.X          = round(circle.center.X + circle.radius, 6)
                top_right.Y          = round(circle.center.Y + circle.radius, 6)
                top_right.unlocked   = False

                debug_print("Arc    " + str(top_right) + " " + str(bottom_left))

        elif isinstance(gitem, GrPoly):
            if gitem.layer == "Edge.Cuts":
                bottom_left = Position(X        = gitem.coordinates[0].X,
                                       Y        = gitem.coordinates[0].Y,
                                       angle    = 0.0,
                                       unlocked = True)

                top_right   = Position(X        = gitem.coordinates[0].X,
                                       Y        = gitem.coordinates[0].Y,
                                       angle    = 0.0,
                                       unlocked = False)

                for coord in gitem.coordinates:
                    if coord.X > top_right.X:
                        top_right.X = coord.X

                    elif coord.X < bottom_left.X:
                        bottom_left.X = coord.X

                for coord in gitem.coordinates:
                    if coord.Y > top_right.Y:
                        top_right.Y = coord.Y

                    elif coord.Y < bottom_left.Y:
                        bottom_left.Y = coord.Y

                debug_print("Poly   " + str(top_right) + " " + str(bottom_left))

        elif isinstance(gitem, GrCurve):
            if gitem.layer == "Edge.Cuts":
                # Documentation on this is poor and apparently not supported in KiCAD 6
                bottom_left = Position(X        = 0.0,
                                       Y        = 0.0,
                                       angle    = 0.0,
                                       unlocked = True)

                top_right   = Position(X        = 0.0,
                                       Y        = 0.0,
                                       angle    = 0.0,
                                       unlocked =True)  # Can ignore as this does not affect the footprint size

                debug_print("Curve  " + str(top_right) + " " + str(bottom_left))

        if not top_right.unlocked:
            if extends_top_right.unlocked:
                extends_top_right.X        = top_right.X
                extends_top_right.Y        = top_right.Y
                extends_top_right.unlocked = False

                extends_bottom_left.X      = bottom_left.X
                extends_bottom_left.Y      = bottom_left.Y

            else:
                if top_right.X > extends_top_right.X:
                    extends_top_right.X   = top_right.X

                if top_right.Y > extends_top_right.Y:
                    extends_top_right.Y   = top_right.Y

                if bottom_left.X < extends_bottom_left.X:
                    extends_bottom_left.X = bottom_left.X

                if bottom_left.Y < extends_bottom_left.Y:
                    extends_bottom_left.Y = bottom_left.Y

        debug_print("Extent " + str(extends_top_right) + " " + str(extends_bottom_left))

    outline = Outline()

    centroid_out      = Coordinate2D()
    centroid_out.X    = round(extends_bottom_left.X + ((extends_top_right.X - extends_bottom_left.X) / 2), 6)
    centroid_out.Y    = round(extends_bottom_left.Y + ((extends_top_right.Y - extends_bottom_left.Y) / 2), 6)

    # top_right_out     = Coordinate2D()
    # top_right_out.X   = extends_top_right.X
    # top_right_out.Y   = extends_top_right.Y

    # bottom_left_out   = Coordinate2D()
    # bottom_left_out.X = extends_bottom_left.X
    # bottom_left_out.Y = extends_bottom_left.Y

    top_right_out     = Coordinate2D()
    top_right_out.X   = round(extends_top_right.X - centroid_out.X, 6)
    top_right_out.Y   = round(extends_top_right.Y - centroid_out.Y, 6)

    bottom_left_out   = Coordinate2D()
    bottom_left_out.X = round(extends_bottom_left.X - centroid_out.X, 6)
    bottom_left_out.Y = round(extends_bottom_left.Y - centroid_out.Y, 6)

    outline.centroid    = centroid_out
    outline.top_right   = top_right_out
    outline.bottom_left = bottom_left_out

    debug_print("C  " + str(outline.centroid))
    debug_print("TR " + str(outline.top_right))
    debug_print("BL " + str(outline.bottom_left))

    return outline


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
    distance = round(math.sqrt((orig_pos.X ** 2) + (orig_pos.Y ** 2)), 6)

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


# ==================================================================================================================
def draw_line(gitem, x1, y1, x2, y2, offset, flip, layer):

    if(y1 - y2 > 1) or (y2 - y1 > 1):
        debug_print(str(x1) + "/" + str(y1) + " " + str(x2) + "/" + str(y2))

    new_start = Position(X        =  x1 - offset.X,
                         Y        = (y1 - offset.Y) * flipped(flip),
                         angle    =  0.0,
                         unlocked =  False)

    new_end   = Position(X        =  x2 - offset.X,
                         Y        = (y2 - offset.Y) * flipped(flip),
                         angle    =  0.0,
                         unlocked =  False)

    line = FpLine(start  = new_start,
                  end    = new_end,
                  layer  = layer,
                  width  = gitem.width,
                  stroke = None,
                  locked = gitem.locked,
                  tstamp = gitem.tstamp)

    return line


# ==================================================================================================================
# Flip the angle in the x-axis if the board is flipped
def flip_angle(x, y, flip):
    if flip:
        angle = round((math.atan2(0 - y, x) / math.pi * 180), 6)
    else:
        angle = round((math.atan2(y, x) / math.pi * 180), 6)

    # angle1 = round(math.atan2(0 - y, x) / math.pi * 180), 6)
    # angle2 = round(math.atan2(y, x) / math.pi * 180), 6)

    # print("In " + str(angle1) + " " + str(angle2))

    if angle == 0:
        result = 0

    elif angle == 180:
        result = 180

    elif angle == -180:
        result = 180

    else:
        if flip:
            if angle >= 0:
                result = angle
                # print(">0f " + str(angle) + " " + str(result))
            else:
                result = 180 + (180 + angle)
                # print("<0f " + str(angle) + " " + str(result))
        else:
            if angle >= 0:
                result = angle
                # print(">0n " + str(angle) + " " + str(result))
            else:
                result = 180 + (180 + angle)
                # print("<0n " + str(angle) + " " + str(result))

    return result


# ==================================================================================================================
# takes the graphicitems (poly, circle, arc, etc and converts them into lines
def vectorise_outline(gr_items, offset, flip):
    vectoritems: List() = []

    new_layer = "Margin"

    for gitem in gr_items:
        # if isinstance(gitem, GrText):
        #     if gitem.layer == "Edge.Cuts":
        #         new_pos = Position(X        = pt_soff(gitem.position, offset).X,
        #                            Y        = pt_soff(gitem.position, offset).Y * flipped(flip),
        #                            angle    = gitem.position.angle,
        #                            unlocked = gitem.position.unlocked)
        #
        #         vectoritems.append(FpText(type     = "user",
        #                                   text     = gitem.text,
        #                                   position = new_pos,
        #                                   hide     = False,
        #                                   layer    = new_layer,
        #                                   effects  = gitem.effects,
        #                                   tstamp   = gitem.tstamp))
        #
        # elif isinstance(gitem, GrTextBox):
        #     if gitem.layer == "Edge.Cuts":
        #         new_pts = list()
        #
        #         new_start = Position(X        = pt_soff(gitem.start, offset).X,
        #                              Y        = pt_soff(gitem.start, offset).Y * flipped(flip),
        #                              angle    = gitem.start.angle,
        #                              unlocked = gitem.start.unlocked)
        #
        #         new_end   = Position(X        = pt_soff(gitem.end, offset).X,
        #                              Y        = pt_soff(gitem.end, offset).Y * flipped(flip),
        #                              angle    = gitem.end.angle,
        #                              unlocked = gitem.end.unlocked)
        #
        #         for pts in gitem.pts:
        #             new_pts.append(Position(X        = pt_soff(pts, offset).X,
        #                                     Y        = pt_soff(pts, offset).Y * flipped(flip),
        #                                     angle    = pts.angle,
        #                                     unlocked = pts.unlocked))
        #
        #         vectoritems.append(FpTextBox(locked      = gitem.locked,
        #                                      text        = gitem.text,
        #                                      start       = new_start,
        #                                      end         = new_end,
        #                                      pts         = new_pts,
        #                                      angle       = gitem.angle,
        #                                      layer       = new_layer,
        #                                      tstamp      = gitem.tstamp,
        #                                      effects     = gitem.effects,
        #                                      stroke      = gitem.stroke,
        #                                      renderCache = gitem.renderCache))

        if isinstance(gitem, GrLine):
            if gitem.layer == "Edge.Cuts":
                vectoritems.append(draw_line(gitem, gitem.start.X, gitem.start.Y, gitem.end.X, gitem.end.Y, offset, flip, new_layer))

        elif isinstance(gitem, GrRect):
            if gitem.layer == "Edge.Cuts":
                #                   X2, Y2
                #   +-----------------+
                #   | 4             3 |
                #   |                 |
                #   | 1             2 |
                #   +-----------------+
                # X1, Y1

                vectoritems.append(draw_line(gitem, gitem.start.X, gitem.start.Y, gitem.end.X,   gitem.start.Y, offset, flip, new_layer))
                vectoritems.append(draw_line(gitem, gitem.end.X,   gitem.start.Y, gitem.end.X,   gitem.end.Y,   offset, flip, new_layer))
                vectoritems.append(draw_line(gitem, gitem.end.X,   gitem.end.Y,   gitem.start.X, gitem.end.Y,   offset, flip, new_layer))
                vectoritems.append(draw_line(gitem, gitem.start.X, gitem.end.Y,   gitem.start.X, gitem.start.Y, offset, flip, new_layer))

        elif isinstance(gitem, GrCircle):
            if gitem.layer == "Edge.Cuts":
                circle_array_x = []
                circle_array_y = []

                # Use Pythagoras to determine the radius
                ptx = gitem.end.X - gitem.center.X
                pty = gitem.end.Y - gitem.center.Y

                radius = round(math.sqrt((ptx * ptx) + (pty * pty)), 6)

                # This gives a point every 5 degrees so good approximation
                number_of_points = 72

                # now calculate the points and draw the circle as line segments
                for loop in range(0, number_of_points + 1):
                    circle_array_x.append(round(gitem.center.X + (math.cos(2 * math.pi / number_of_points * loop) * radius), 6))
                    circle_array_y.append(round(gitem.center.Y + (math.sin(2 * math.pi / number_of_points * loop) * radius), 6))

                    if loop > 0:
                        vectoritems.append(draw_line(gitem, circle_array_x[loop - 1], circle_array_y[loop - 1], circle_array_x[loop], circle_array_y[loop],
                                                     offset, flip, new_layer))

        elif isinstance(gitem, GrArc):
            if gitem.layer == "Edge.Cuts":
                if flip:  # flip
                    start = gitem.end
                    middle = gitem.mid
                    end = gitem.start

                else:  # no flip
                    start = gitem.start
                    middle = gitem.mid
                    end = gitem.end

                circle = calc_circle(start, middle, end)

                circle_array = []
                arc_array    = []

                start_angle  = flip_angle(start.X - circle.center.X, start.Y - circle.center.Y, flip)
                end_angle    = flip_angle(end.X - circle.center.X,   end.Y - circle.center.Y,   flip)

                # to deal with an end point that goes thru the 0 point we need to add 360.
                if end_angle < start_angle:
                    end_angle = end_angle + 360

                # print("S - " + str(start.X)  + "/" + str(start.Y)  + " " + str(start_angle))
                # print("M - " + str(middle.X) + "/" + str(middle.Y) + " " + str(middle_angle))
                # print("E - " + str(end.X)    + "/" + str(end.Y)    + " " + str(end_angle))

                # This gives a point every 5 degrees so good approximation
                number_of_points = 72

                # now calculate the points and draw the circle as line segments to deal will all arc, we create the data for two circles, this allows the subsequent
                # extraction of data not have to worry about running through the end of one circle
                for loop in range(0, (2 * number_of_points) - 1):
                    pttx  = round(circle.center.X +  (math.cos(2 * math.pi / number_of_points * loop) * circle.radius), 6)
                    ptty  = round(circle.center.Y + ((math.sin(2 * math.pi / number_of_points * loop) * circle.radius) * flipped(flip)), 6)
                    angle = loop * (360/number_of_points)

                    circle_array.append(Position(X     = pttx,
                                                 Y     = ptty,
                                                 angle = angle))

                cflag = False
                sflag = False

                # not extract data based on the original start/end and the calculated intermediate angles
                arc_array.append(start)

                for pos in circle_array:
                    if (pos.angle >= end_angle) and sflag:
                        cflag = True

                    if (pos.angle > start_angle) and (not cflag):
                        arc_array.append(pos)
                        sflag = True

                arc_array.append(end)

                # now calculate the points and draw the circle as line segments
                for loop in range(0, len(arc_array)):
                    if loop > 0:
                        vectoritems.append(draw_line(gitem, arc_array[loop - 1].X, arc_array[loop - 1].Y, arc_array[loop].X, arc_array[loop].Y,
                                                     offset, flip, new_layer))

        elif isinstance(gitem, GrPoly):
            if gitem.layer == "Edge.Cuts":
                new_coords = list()

                for coord in gitem.coordinates:
                    new_coords.append(coord)

                for loop in range(0, len(new_coords)):
                    if loop > 0:
                        vectoritems.append(draw_line(gitem, new_coords[loop - 1].X, new_coords[loop - 1].Y, new_coords[loop].X, new_coords[loop].Y, offset, flip, new_layer))

                    # And close the polygon
                    if loop == len(new_coords) - 1:
                        vectoritems.append(draw_line(gitem, new_coords[loop].X, new_coords[loop].Y, new_coords[0].X, new_coords[0].Y, offset, flip, new_layer))

        elif isinstance(gitem, GrCurve):
            if gitem.layer == "Edge.Cuts":
                new_coords = list()

                for coord in gitem.coordinates:
                    new_coords.append(Position(X        = pt_soff(coord, offset).X,
                                               Y        = pt_soff(coord, offset).Y * flipped(flip),
                                               angle    = coord.angle,
                                               unlocked = coord.unlocked))

                for loop in range(0, len(new_coords)):
                    vectoritems.append(draw_line(gitem, new_coords[loop - 1].X, new_coords[loop - 1].Y, new_coords[loop].X, new_coords[loop].Y,
                                                 offset, flip, new_layer))

    return vectoritems
