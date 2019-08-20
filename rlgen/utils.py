"""

Make wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""


def gen_square(dim, x, y, z, width=5, height=4):
    "Generate a gate square."

    iron = dim.blocktypes["minecraft:iron_block"]
    for dz in range(width):
        dim.setBlock(x, y, z + dz, iron)
        dim.setBlock(x + height - 1, y, z + dz, iron)
    for dx in range(height):
        dim.setBlock(x + dx, y, z, iron)
        dim.setBlock(x + dx, y, z + width - 1, iron)

    sandstone = dim.blocktypes["minecraft:sandstone"]
    for dz in range(width-2):
        for dx in range(height-2):
            dim.setBlock(x + dx + 1, y, z + dz + 1, sandstone)
