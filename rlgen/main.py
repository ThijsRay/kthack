"""

Entry point of this utility.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

import os.path as path
import shutil
import argparse

from mceditlib.worldeditor import WorldEditor


# TODO: remove me.
from .inputs import gen_input
from .block import *
from parser import *
def load_empty_world():
    "Load the empty world."

    root = path.abspath(path.join(path.dirname(__file__), ".."))
    folder = path.join(root, "assets", "EmptyMap")
    result = path.join(root, "MapResult")

    shutil.copytree(folder, result)
    return WorldEditor(result)

def main():
    "Entry point of this utility."

    # Parse CLI.
    parser = argparse.ArgumentParser(prog="rlgen")


    # Load Minecraft world and create logic gates.
    world = load_empty_world()
    dim = world.getDimension()
    my_and(dim,6,56,6)
    my_or(dim,12,56,6)
    my_not(dim,18,56,6)
    # gate_base(dim,6,56,6)
    gen_input(dim, 0, 0)

    world.saveChanges()
    # DO NOT CALL "world.close()"
