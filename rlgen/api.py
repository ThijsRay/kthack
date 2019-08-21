"""

Manage API with II and parser.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from intermediate_representation.ast import *

from .constants import GATES_Y, GATES_X
from .inputs import gen_inputs
from .wires import gen_input_wires


# Golbal variables.
DIM = None


def place_gate(x, z, gate):
    "Place a gate at the specific location."

    # TODO.


def wire_g2g(ox, oz, ing, inum):
    "Make a gate-to-gate wire"

    if isinstance(ing, Terminal):
        return  # Terminal is not a gate.


def wire_i2g(ox, oz, ing, inum, inputs):
    "Make a gate-to-gate wire"

    if not isinstance(ing, Terminal):
        return

    idx = inputs.index(ing.identifier)
    x = GATES_X + ox * (4 + 4)
    z = oz * (5 + 4)

    gen_input_wires(DIM, x, GATES_Y, z, idx)



def generate_matrix(exp, mat, i):
    "Generate a matrix."

    if len(mat) <= i:
        mat.append([])
    for child in exp.children():
        generate_matrix(child, mat, i+1)
    mat[i].append(exp)


def find_inputs(exp, inputs):
    "Find all inputs."

    if isinstance(exp, Terminal) and exp.identifier not in inputs:
        inputs.append(exp.identifier)

    for child in exp.children():
        find_inputs(child, inputs)



def gen_g2g_wires(exp):
    "Generate gate-to-gate wires."

    ch = exp.children()

    if len(ch) == 1:
        wire_g2g(exp.x, exp.z, ch[0], 2)
    elif len(ch) == 2:
        wire_g2g(exp.x, exp.z, ch[0], 1)
        wire_g2g(exp.x, exp.z, ch[1], 3)

    for child in exp.children():
        gen_g2g_wires(child)


def gen_i2g_wires(exp, inputs):
    "Generate input-to-gate wires."

    ch = exp.children()

    if len(ch) == 1:
        wire_i2g(exp.x, exp.z, ch[0], 2, inputs)
    elif len(ch) == 2:
        wire_i2g(exp.x, exp.z, ch[0], 1, inputs)
        wire_i2g(exp.x, exp.z, ch[1], 3, inputs)

    for child in exp.children():
        gen_i2g_wires(child, inputs)



def gen_gates(dim, exp):
    "Generate all gates from input expression."

    global DIM
    DIM = dim

    # Generate exp matrix.
    mat, inputs = [], []
    find_inputs(exp, inputs)
    generate_matrix(exp, mat, 0)

    # Generate inputs.
    gen_inputs(dim, len(inputs))

    # Generate gates.
    for x, column in enumerate(reversed(mat)):
        for z, cell in enumerate(column):
            cell.x = x
            cell.z = z
            place_gate(x, z, cell)

    # Generate gate to gate wires.
    gen_g2g_wires(exp)

    # Generate input to gate wires.
    gen_i2g_wires(exp, inputs)
