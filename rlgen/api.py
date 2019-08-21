"""

Manage API with II and parser.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

from intermediate_representation.ast import *

from .constants import GATES_Y, GATES_X, GATES_X_SPACE
from .inputs import gen_inputs
from .wires import gen_input_wires, gen_gate_wire
from .block import gen_gate_from_tabs


# Golbal variables.
DIM = None


def place_gate(x, z, gate):
    "Place a gate at the specific location."

    if isinstance(gate, Terminal):
        return  # Terminal is not a gate.

    types = (Or, And, Not)
    x = GATES_X + x * (4 + GATES_X_SPACE) + 1
    z = z * (5 + 4) - 2
    gen_gate_from_tabs(DIM, x, GATES_Y, z, types.index(gate.__class__))


def wire_g2g(ox, oz, ing, inum, index, index2):
    "Make a gate-to-gate wire"

    if isinstance(ing, Terminal):
        return  # Terminal is not a gate.

    ox = GATES_X + ox * (4 + GATES_X_SPACE)
    ix = GATES_X + ing.x * (4 + GATES_X_SPACE) + 5
    oz = oz * (5 + 4)
    iz = ing.z * (5 + 4)

    if inum == 1:
        oz -= 1
    elif inum == 3:
        oz += 1

    gen_gate_wire(DIM, ix, iz, ox, oz, GATES_Y, index, index2)


def wire_i2g(ox, oz, ing, inum, inputs):
    "Make a gate-to-gate wire"

    if not isinstance(ing, Terminal):
        return

    idx = inputs.index(ing.identifier)
    x = GATES_X + ox * (4 + GATES_X_SPACE)
    z = oz * (5 + 4)

    if inum == 1:
        z -= 1
    elif inum == 3:
        z += 1

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
        wire_g2g(exp.x, exp.z, ch[0], 2, ch[0].index, ch[0].index2)
    elif len(ch) == 2:
        wire_g2g(exp.x, exp.z, ch[0], 1, ch[0].index, ch[0].index2)
        wire_g2g(exp.x, exp.z, ch[1], 3, ch[1].index, ch[1].index2)

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

    print(exp)
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
            cell.index = z
            cell.index2 = len(column) - z
            place_gate(x, z, cell)

    # Generate gate to gate wires.
    gen_g2g_wires(exp)

    # Generate input to gate wires.
    gen_i2g_wires(exp, inputs)
