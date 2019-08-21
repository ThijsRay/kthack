"""

Entry point of this utility.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

import os.path as path
import shutil

from mceditlib.worldeditor import WorldEditor


# TODO: remove me.
from .inputs import gen_inputs
from .wires import gen_input_wires
from .block import gen_gate_from_tabs
from .wires import wire

from intermediate_representation.ast import *


def load_empty_world():
    "Load the empty world."

    root = path.abspath(path.join(path.dirname(__file__), ".."))
    folder = path.join(root, "assets", "EmptyMap")
    result = path.join(root, "MapResult")

    shutil.rmtree(result, ignore_errors=True)
    shutil.rmtree(path.join(root, "##MapResult.UNDO##"), ignore_errors=True)

    shutil.copytree(folder, result)
    return WorldEditor(result)


def tmp_exp():
    "Generate a temporary expression."

    input = And(
        Xor(Terminal("Cin"), Xor(Terminal("A"), Terminal("B"))),
        Or(And(Terminal("A"), Terminal("B")), And(Terminal("Cin"), Xor(Terminal("A"),
        Terminal("B")))))
    return input.desugar()


def main():
    "Entry point of this utility."

    # Load Minecraft world and create logic gates.
    world = load_empty_world()
    dim = world.getDimension()

    # TODO: remove me.

    # gen_inputs(dim, 200)
    # gen_input_wires(dim, 40, 30, -9, 1)
    gen_gate_from_tabs(dim,0,0,0)
    gen_gate_from_tabs(dim,1,0,1)
    gen_gate_from_tabs(dim,1,1,1)
    wire(dim,1,0,2,0,0,1)
    wire(dim,1,1,2,0,0,3)

    from .api import gen_gates
    gen_gates(dim, tmp_exp())

    world.saveChanges()
    # DO NOT CALL "world.close()"
