from mceditlib.worldeditor import WorldEditor
import parser
from parser import *
import constants
import utils 
from utils import gen_square
def gate_base(dim,x,y,z):
    gen_square(dim, x, y, z, width=5, height=4)
    stone = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    dim.setBlock(x+3,y+1,z+2,stone)

def my_and(dim,x,y,z):
    gate_base(dim,x,y,z)
    stone = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    dim.setBlock(x,y+1,z+1,stone)
    dim.setBlock(x,y+1,z+3,stone)
    stone = dim.blocktypes["minecraft:sandstone"]
    dim.setBlock(x+1,y+1,z+1,stone)
    dim.setBlock(x+1,y+1,z+2,stone)
    dim.setBlock(x+1,y+1,z+3,stone)
    stone = dim.blocktypes["minecraft:unlit_redstone_torch[facing=east]"]
    dim.setBlock(x+2,y+1,z+2,stone)
    stone = dim.blocktypes["minecraft:unlit_redstone_torch[facing=up]"]
    dim.setBlock(x+1,y+2,z+1,stone)
    dim.setBlock(x+1,y+2,z+3,stone)

def my_or(dim,x,y,z):
    gate_base(dim,x,y,z)
    stone = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    dim.setBlock(x,y+1,z+1,stone)
    dim.setBlock(x,y+1,z+3,stone)
    stone =  stone = dim.blocktypes["minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"]
    dim.setBlock(x+1,y+1,z+1,stone)
    dim.setBlock(x+1,y+1,z+2,stone)
    dim.setBlock(x+1,y+1,z+3,stone)
    dim.setBlock(x+2,y+1,z+2,stone)

def my_not(dim,x,y,z): 
    gate_base(dim,x,y,z)
    stone = dim.blocktypes["minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"]
    dim.setBlock(x,y+1,z+2,stone)
    stone = dim.blocktypes["minecraft:sandstone"]
    dim.setBlock(x+1,y+1,z+2,stone)
    stone = dim.blocktypes["minecraft:redstone_torch[facing=east]"]
    dim.setBlock(x+2,y+1,z+2,stone)
