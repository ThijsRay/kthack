"""

Generate wires between gates.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from .constants import FLOOR_Y, COLORS, INPUT_TOWER_X, INPUT_TOWER_Z, INPUT_TOWER_DZ


def gen_tower(dim, x, y, z, height, color="orange"):
    "Generate first input tower."

    whool = dim.blocktypes["minecraft:wool[color=%s]" % color]
    torch = dim.blocktypes["minecraft:redstone_torch[facing=up]"]

    for dy in range(0, height, 2):
        dim.setBlock(x, y + dy, z, whool)
        dim.setBlock(x, y + dy + 1, z, torch)



def gen_input_wires(dim, x, y, z, i):
    "Generate wires from the given input."

    color = COLORS[i]
    wool = dim.blocktypes["minecraft:wool[color=%s]" % color]
    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]

    # Generate route from input tower to gate x position.
    ty = FLOOR_Y + 1 + (i * 4)
    tz = INPUT_TOWER_Z + (i * INPUT_TOWER_DZ)

    for tx in range(INPUT_TOWER_X, x):
        # TODO: add reapeters.
        dim.setBlock(tx, ty, tz, wool)
        dim.setBlock(tx, ty + 1, tz, wire)


    # Generate next route to gate y position.
    if y == ty:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=north,locked=false]"]
        dim.setBlock(tx, y + 1, tz, repeater)

    elif y < ty:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=north,locked=false]"]
        
        dim.setBlock(tx, ty, tz, wool)
        dim.setBlock(tx, ty + 1, tz, wire)

    else:
        repeater = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=north,locked=false]"]
        dim.setBlock(tx, ty, tz, wool)
        dim.setBlock(tx, ty + 1, tz, wire)

def wire(dim,x1,z1,type1,x2,z2,type2):
    stone = dim.blocktypes["minecraft:sandstone"]
    wire = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]
    difx = abs(x1-x2)
    dify = abs(z1-z2)
    floor = 250
    new_x = x1*4 + 4*x1
    new_z = z1*5 + 4*z1
    for i in range(difx*2):
        dim.setBlock(new_x+i,floor,new_z + 2,stone)
        dim.setBlock(new_x+i,floor+1,new_z + 2 ,wire)
    ty = 0
    if(type2 == 1):
        ty = -1
    if(type2 == 3):
        ty += 1
    for j in range(dify*4 + ty):
        dim.setBlock(new_x+2,floor,new_z+i + 2,stone)
        dim.setBlock(new_x+2,floor+1,new_z+i + 2,wire)

    for i in range(difx*2):
        dim.setBlock(new_x+2+i,floor,new_z + 2,stone)
        dim.setBlock(new_x+2+i,floor+1,new_z + 2,wire)
