"""
Takes the AST from the compiler frontend and
turns it into something usable by save file creator.
"""

# Universal constants
__UNIFORM_X_SIZE = 5
__UNIFORM_Y_SIZE = 4
__UNIFORM_Z_SIZE = 4


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

    def add(
            self,
            point # Point
        ):
        x = self.x + point.x
        y = self.y + point.y
        z = self.z + point.z
        return Point(x, y, z)

    def add(
            self,
            dx, # int
            dy, # int
            dz  # int
        ):
        return self.add(Point(dx, dy, dz))


class Module:
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
            x_size,  # int
            y_size, # int
            z_size,  # int
            inputs, # dict
            outputs # dict
        ):

        self.origin = origin
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size

        # A good check would be to control that inputs and outputs
        # do not run out of module bounds here.
        self.inputs = inputs
        self.outputs = outputs

    def to_blocks(self):
        """
        Used to turn the module into a three dimensional 'matrix'
        of (block type, coordinates) pairs.
        """
        raise NotImplementedError()


class Operation:
    """
    Class that defines the AST types
    """
    def simplify(self):
        raise NotImplementedError("Class %s doesn't implement simplyfy()" % (self.__class__.__name__))


class And(Operation, Module):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation

    def simplify(self):
        And(self.x.simplify(), self.y.simplify())


class Or(Operation, Module):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation

    def simplify(self):
        Or(self.x.simplify(), self.y.simplify())


class Not(Operation, Module):
    def __init__(self, x):
        self.x = x  # Operation

    def simplify(self):
        Not(self.x.simplify())


class Terminal(Operation, Module):
    def __init__(self, identifier):
        self.identifier = identifier  # String

    def simplify(self):
        Terminal(self.identifier)


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
            "A": Point(3, 1, 3),
            "B": Point(1, 1, 3),
        }

        outputs = {
            "Y": Point(-2, 1, 0),
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
            "A": Point(3, 1, 3),
            "B": Point(1, 1, 3),
        }

        outputs = {
            "Y": Point(-2, 1, 0),
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

        inputs = {}

        outputs = {
            "Y": Point(-2, 1, 0),
        }

        super(OR, self).__init__(
            origin,
            __UNIFORM_WIDTH,
            __UNIFORM_HEIGHT,
            __UNIFORM_DEPTH,
            inputs,
            outputs
        )


if __name__ == "__main__":

    input = And(Or(Or("x", And("y", "z")), "x"), Or("x", Not(And("a", "x"))))
    input.simplify()



    print("Hey")
