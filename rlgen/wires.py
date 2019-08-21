"""

Generate wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from .constants import GATES_Y, GATES_X
from .constants import FLOOR_Y, COLORS, INPUT_TOWER_X, INPUT_TOWER_Z, INPUT_TOWER_DZ


def gen_tower(dim, x, y, z, height, color="orange"):
    "Generate first input tower."

    whool = dim.blocktypes["minecraft:wool[color=%s]" % color]
    torch = dim.blocktypes["minecraft:redstone_torch[facing=up]"]

    for dy in range(0, height, 2):
        dim.setBlock(x, y + dy, z, whool)
        dim.setBlock(x, y + dy + 1, z, torch)



def gen_straight_z_wire(dim, support, z1, z2, x, y, align=4):
    "Generate a straight wire."

    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]
    for tz in range(min(z1, z2), max(z1, z2)+1):
        dim.setBlock(x, y, tz, support)
        dim.setBlock(x, y + 1, tz, wire)

    if z1 < z2:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=north,locked=false]"]
    else:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=south,locked=false]"]

    for z in range(min(z1, z2) + align, max(z1, z2) - 1, 9):
        dim.setBlock(x, y + 1, z, repeater)


def gen_straight_x_wire(dim, support, x1, x2, z, y, align=4):
    "Generate a straight wire."

    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]
    for tx in range(min(x1, x2), max(x1, x2)+1):
        dim.setBlock(tx, y, z, support)
        dim.setBlock(tx, y + 1, z, wire)

    if x1 < x2:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    else:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=east,locked=false]"]

    for x in range(min(x1, x2) + align, max(x1, x2), 8):
        dim.setBlock(x, y + 1, z, repeater)


def gen_input_wires(dim, x, y, z, i):
    "Generate wires from the given input."

    color = COLORS[i]
    repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    wool = dim.blocktypes["minecraft:wool[color=%s]" % color]

    # Generate route from input tower to gate x position.
    ty = FLOOR_Y + 1 + (i * 4)
    tz = INPUT_TOWER_Z + (i * INPUT_TOWER_DZ) - 2
    gen_straight_x_wire(dim, wool, INPUT_TOWER_X, x - 2, tz, ty)

    # Generate next route to gate z position.
    gen_straight_z_wire(dim, wool, tz, z, x - 2, ty)
    # Generate the final tower.
    dim.setBlock(x - 1, ty, z, wool)
    dim.setBlock(x - 1, ty + 1, z, repeater)
    gen_tower(dim, x, ty + 1, z, y - ty, color)
    dim.setBlock(x, y + 1, z, wool)


def gen_gate_wire(dim, x1, z1, x2, z2, y, index, index2):
    stone = dim.blocktypes["minecraft:sandstone"]
    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]

    if z1 > z2:
        X = x1 + (2 * index)
    else:
        X = x1 + (2 * index2)

    gen_straight_x_wire(dim, stone, x1, X, z1, y)

    gen_straight_z_wire(dim, stone, z1, z2, X, y)
    gen_straight_x_wire(dim, stone, X, x2, z2, y)
