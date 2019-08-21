
from .ast import *


def gen_matrix(exp, mat, i):
    "Generate a matrix."

    if len(mat) <= i:
        mat.append([])

    for child in exp.children():
        gen_matrix(child, mat, i+1)

    mat[i].append(exp)


def main():
    input = And(
        Xor(Terminal("Cin"), Xor(Terminal("A"), Terminal("B"))),
        Or(And(Terminal("A"), Terminal("B")), And(Terminal("Cin"), Xor(Terminal("A"),
        Terminal("B")))))
    input = input.desugar()

    mat = []
    gen_matrix(input, mat, 0)
    mat.reverse()

    print(mat)


if __name__ == "__main__":
    main()
