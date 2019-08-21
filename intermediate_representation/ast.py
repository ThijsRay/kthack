# Input:
#   And(x, y)
#   Or(x, y)
#   Not(x)
#   Terminal variables

from

class Operation:
    """
    Class that defines the AST types
    """
    def simplify(self):
        raise NotImplementedError("Class %s doesn't implement simplify()" % (self.__class__.__name__))

    def depth(self):
        raise NotImplementedError("Class %s doesn't implement depth()" % (self.__class__.__name__))

    def module(self):
        raise NotImplementedError("Class %s doesn't implement module()" % (self.__class__.__name__))


class And(Operation):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation
        self.depth = 0

    def simplify(self):
        return And(self.x.simplify(), self.y.simplify())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.x.depth(self.depth)
            self.y.depth(self.depth)

class Or(Operation):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation
        self.depth = 0

    def simplify(self):
        return Or(self.x.simplify(), self.y.simplify())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.x.depth(self.depth)
            self.y.depth(self.depth)


class Not(Operation):
    def __init__(self, x):
        self.x = x  # Operation
        self.depth = 0

    def simplify(self):
        return Not(self.x.simplify())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.x.depth(self.depth)


class Terminal(Operation):
    def __init__(self, identifier):
        self.identifier = identifier  # String
        self.depth = 0

    def simplify(self):
        return self

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1


class Pass(Operation):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def simplify(self):
        return Pass(self.left.simplify(), self.right.simplify())

    def depth(self, parent_depth = 0):
        parent_depth

if __name__ == "__main__":
    input = And(Or(Or("x", And("y", "z")), "x"), Or("x", Not(And("a", "x"))))
    input.simplify()

    print("Hey")
