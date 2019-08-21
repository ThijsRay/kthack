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
from .inputs import gen_inputs
from .wires import gen_input_wires


def load_empty_world():
    "Load the empty world."

    root = path.abspath(path.join(path.dirname(__file__), ".."))
    folder = path.join(root, "assets", "EmptyMap")
    result = path.join(root, "MapResult")

    shutil.rmtree(result, ignore_errors=True)
    shutil.rmtree(path.join(root, "##MapResult.UNDO##"), ignore_errors=True)

    shutil.copytree(folder, result)
    return WorldEditor(result)

def main():
    "Entry point of this utility."

    # Parse CLI.
    parser = argparse.ArgumentParser(prog="rlgen")


    # Load Minecraft world and create logic gates.
    world = load_empty_world()
    dim = world.getDimension()

    # TODO: remove me.
    gen_inputs(dim, 200)

    gen_input_wires(dim, 40, 30, -9, 1)

    world.saveChanges()
    # DO NOT CALL "world.close()"
