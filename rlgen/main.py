"""

Entry point of this utility.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

import os.path as path
import shutil
import argparse

from mceditlib.worldeditor import WorldEditor
from .inputs import gen_input
from .block import gate_base

def load_empty_world():
    "Load the empty world."

    root = path.abspath(path.join(path.dirname(__file__), ".."))
    folder = path.join(root, "assets", "New_World")
    result = path.join(root, "New_World_Result")

    shutil.copytree(folder, result)
    return WorldEditor(result)

def main():
    "Entry point of this utility."

    # Parse CLI.
    parser = argparse.ArgumentParser(prog="rlgen")


    # Load Minecraft world and create logic gates.
    world = load_empty_world()
    dim = world.getDimension()
    gate_base(dim,0,56,0)
    gen_input(dim, 0, 0)

    world.saveChanges()
    # DO NOT CALL "world.close()"
