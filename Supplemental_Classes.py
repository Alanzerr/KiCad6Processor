#  ===================================================================
#  Source File Name : Supplemental_Classes.py
#  Purpose          : Supplemental classes for various things.
#  Author           : Alan Milne
#  #
#  This is copyright (C) 2022 to Alan Milne
#  ===================================================================

# from typing import Optional, List
# from os import path

# from kiutils.utils.strings import dequote
# from kiutils.utils import sexpr
from kiutils.footprint import *


# ==================================================================================================================
@dataclass
class LongAxis:
    x_axis: bool = False
    y_axis: bool = False


# ==================================================================================================================
@dataclass
class Circle:
    center: Position = Position()
    radius: float    = 0.0


# ==================================================================================================================
@dataclass
class Coordinate2D:
    X: float = 0.0
    Y: float = 0.0


# ==================================================================================================================
@dataclass
class Outline:
    centroid:    Coordinate2D = (0.0, 0.0)
    top_right:   Coordinate2D = (0.0, 0.0)
    bottom_left: Coordinate2D = (0.0, 0.0)

# ==================================================================================================================


# ==================================================================================================================
@dataclass
class OutlineData:
    board_edge:     list()
    non_board_edge: list()


# ==================================================================================================================
@dataclass
class Component:
    pads         = []
    graphicitems = []
    models       = []


# ==================================================================================================================
@dataclass
class AuxData:
    # This is to supplement footprint with extra data to make it easier to use. Built on top of Footprint.

    # Is the footprint origin the center or Pin 1
    center_origin:   bool         = False

    # Offset to Center from pin 1.
    center:          Coordinate2D = Coordinate2D()

    # used to determine the long axis so that we know what way to flip
    longaxis_X:      bool         = True

    flip:            bool         = False
    header:          bool         = True
    pin_pitch:       float        = 0.0
    layer:           str          = ""
    id:              str          = ""
    type:            str          = ""

    # Board offset
    centroid_offset: Position     = Position()

    # Board flip
    board_flip:      bool         = False


# ==================================================================================================================
@dataclass
class Components:
    component_data: list[Component] = field(default_factory=list)

    menu_data:      list[str]       = field(default_factory=list)
