"""

Make wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from .constants import FLOOR_Y
from .utils import gen_square


def gen_input(dim, x, z):
    "Generate an input at the given coordinates."

    gen_square(dim, x, FLOOR_Y, z)



def gen_inputs(world):
    "Generate inputs"


