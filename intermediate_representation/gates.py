"""
Takes the AST from the compiler frontend and
turns it into something usable by save file creator.
"""


# Universal constants
__UNIFORM_WIDTH  = 7
__UNIFORM_HEIGHT = 4
__UNIFORM_DEPTH  = 7


class Point:
    """
    A point in three dimensional space.
    """

    def __init__(
            self,
            x, # int
            y, # int
            z  # int
        ):
        self.x = x
        self.y = y
        self.z = z


class Module():
    """
    A rectangular prism in the three dimensional space.
    Mostly used to represent a logic gate.

    Also contains a dictionary each for inputs and outputs
    where keys are the *put name and values are points relative
    to the (0, 0, 0) where the left, down, near corner of the Module is.
    """

    def __init__(
            self,
            origin, # Point
            width,  # int
            height, # int
            depth,  # int
            inputs, # dict
            outputs # dict
        ):

        self.origin = origin
        self.width = width
        self.height = height
        self.depth = depth

        # A good check would be to control that inputs and outputs
        # do not run out of module bounds here.
        self.inputs = inputs
        self.outputs = outputs


    def to_blocks():
        """
        Used to turn the module into a three dimensional 'matrix'
        of (block type, coordinates) pairs.
        """
        raise NotImplementedError()


class NOT(Module):
    """
    Logical NOT gate.
    """

    def __init__(
            self,
            origin # Point
        ):

        inputs = {
            "A": Point(),
        }

        outputs = {
            "Y": Point(),
        }

        super(NOT, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )


class AND(Module):
    """
    Logical AND gate.
    """

    def __init__(
            self,
            origin # Point
        ):

        inputs = {
            "A": Point(0, 1, 2),
            "B": Point(0, 1, 4),
        }

        outputs = {
            "Y": Point(6, 1, 3),
        }

        super(AND, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )


class OR(Module):
    """
    Logical OR gate.
    """

    def __init__(
        self,
        origin # Point
    ):

        inputs = {
            "A": Point(0, 1, 2),
            "B": Point(0, 1, 4),
        }

        outputs = {
            "Y": Point(6, 1, 3),
        }

        super(OR, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )


class INPUT(Module):
    """
    User input.
    """

    def __init__(
        self,
        origin # Point
    ):

        inputs = {
            "A": Point(0, 1, 2),
        }

        outputs = {
            "Y": Point(6, 1, 3),
        }

        super(OR, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )


class OUTPUT(Module):
    """
    User output.
    """

    def __init__(
        self,
        origin # Point
    ):

        inputs = {
            "A": Point(0, 1, 2),
            "B": Point(0, 1, 4),
        }

        outputs = {
            "Y": Point(6, 1, 3),
        }

        super(OR, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )
