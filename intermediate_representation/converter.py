"""
Takes the AST from the compiler frontend and
turns it into something usable by save file creator.
"""

class Point:
    """
    A point in three dimensional space.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Block:
    """
    A rectangular prism in the three dimensional space.
    Used to represent a gate.

    Also contains a dictionary each for inputs and outputs
    where keys are the *put name and values are points relative
    to the (0, 0, 0) where the left, down, near corner of the block is.
    """

    def __init__(self, width, height, depth, inputs, outputs):
        self.width = width
        self.height = height
        self.depth = depth

        # A good check would be to control that inputs and outputs
        # do not run out of block bounds here.
        self.inputs = inputs
        self.outputs = outputs
