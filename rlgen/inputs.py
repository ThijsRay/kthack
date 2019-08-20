"""

Make wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from .constants import FLOOR_Y
from .utils import gen_square


def gen_input(dim, x, z, color="orange"):
    "Generate an input at the given coordinates."

    gen_square(dim, x, FLOOR_Y, z)
    dim.setBlock(x + 1, FLOOR_Y + 1, z + 2, "minecraft:wool[color=%s]" % color)
    dim.setBlock(x + 1, FLOOR_Y + 2, z + 2, "minecraft:lever[facing=up_x,powered=false]")


def gen_inputs(world):
    "Generate inputs"


