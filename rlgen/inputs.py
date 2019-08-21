"""

Make wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from .constants import FLOOR_Y, COLORS, INPUT_TOWER_X
from .utils import gen_square
from .wires import gen_tower


def gen_input(dim, x, z, i):
    "Generate an input at the given coordinates."

    gen_square(dim, x, FLOOR_Y, z)
    color = COLORS[i % len(COLORS)]

    dim.setBlock(x + 1, FLOOR_Y + 1, z + 2, "minecraft:wool[color=%s]" % color)
    dim.setBlock(x + 1, FLOOR_Y + 2, z + 2, "minecraft:lever[facing=up_x,powered=false]")

    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]
    for dx in range(2, 6):
        dim.setBlock(x + dx, FLOOR_Y + 1, z + 2, wire)

    height = i * 4
    gen_tower(dim, x + 6, FLOOR_Y + 1, z + 2, height, color)


def gen_inputs(dim, n):
    "Generate inputs"

    for i in range(n):
        gen_input(dim, INPUT_TOWER_X - 6, i * 6, i)
