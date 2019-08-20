from mceditlib.worldeditor import WorldEditor
import parser
from parser import *
import constants

def gate_base(dim,x,y,z):
    stone = dim.blocktypes["minecraft:iron_block"]
    for i in range(5):
        dim.setblock(x,y,z+i)
        dim.setblock(x+3,y,z+i)
    dim.setblock(x+1,y,z)
    dim.setblock(x+1,y,z+5)
    dim.setblock(x+2,y,z)
    dim.setblock(x+2,y,z+5)
    stone = dim.blocktypes["minecraft:sandstone"]
    for i in range(3):
        dim.setblock(x+1,y,z+i)
        dim.setblock(x+2,y,z+i)
    stone = dim.blocktypes["minecraft:unpowered_repeater"]
    dim.setblock(x+3,y+1,z+3)

def my_and(dim,And,y):
    gate_base(dim,And.x,y,And.z)

def my_or(dim, Or,y):
    gate_base(dim,And.x,y,And.z)

def my_not(dim,Not,y): 
    gate_base(dim,And.x,y,And.z)