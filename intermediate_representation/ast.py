# Input:
#   And(x, y)
#   Or(x, y)
#   Not(x)
#   Terminal variables

class Sugar:
    def desugar(self):
        raise NotImplementedError("Class %s doesn't implement desugar()" % (self.__class__.__name__))


class Operation:
    """
    Class that defines the AST types
    """
    def depth(self):
        raise NotImplementedError("Class %s doesn't implement depth()" % (self.__class__.__name__))

    def module(self):
        raise NotImplementedError("Class %s doesn't implement module()" % (self.__class__.__name__))

    def children(self):
        raise NotImplementedError("Class %s doesn't implement children()" % (self.__class__.__name__))


class And(Operation, Sugar):
    def __init__(self, left, right):
        self.left = left  # Operation
        self.right = right  # Operation
        self.depth = 0

    def desugar(self):
        return And(self.left.desugar(), self.right.desugar())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.left.depth(self.depth)
            self.right.depth(self.depth)
        return self.depth

    def children(self):
        return [self.left, self.right]

    def __str__(self):
        return "And(%s, %s)" % (self.left, self.right)


class Or(Operation, Sugar):
    def __init__(self, left, right):
        self.left = left  # Operation
        self.right = right  # Operation
        self.depth = 0

    def desugar(self):
        return Or(self.left.desugar(), self.right.desugar())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.left.depth(self.depth)
            self.right.depth(self.depth)
        return self.depth

    def children(self):
        return [self.left, self.right]

    def __str__(self):
        return "Or(%s, %s)" % (self.left, self.right)

class Not(Operation, Sugar):
    def __init__(self, op):
        self.op = op  # Operation
        self.depth = 0

    def desugar(self):
        return Not(self.op.desugar())

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1
            self.op.depth(self.depth)

    def children(self):
        return [self.op]

    def __str__(self):
        return "Not(%s)" % (self.op)


class Terminal(Operation, Sugar):
    def __init__(self, identifier):
        self.identifier = identifier  # String
        self.depth = 0

    def desugar(self):
        return self

    def depth(self, parent_depth = 0):
        if self.depth == 0:
            self.depth = parent_depth + 1

    def children(self):
        return list()

    def __str__(self):
        return "T[%s]" % (self.identifier)


class Pass(Operation, Sugar):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def desugar(self):
        return Pass(self.left.desugar(), self.right.desugar())

    def depth(self, parent_depth = 0):
        parent_depth

    def children(self):
        return [self.left, self.right]

    def __str__(self):
        return "Pass(%s, %s)" % (self.left, self.right)


class Xor(Sugar):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def desugar(self):
        return Or(And(self.left.desugar(), Not(self.right.desugar())), And(Not(self.left.desugar()), self.right.desugar()))


if __name__ == "__main__":
    input = Pass(
        Xor(Terminal("Cin"), Xor(Terminal("A"), Terminal("B"))),
        Or(And(Terminal("A"), Terminal("B")), And(Terminal("Cin"), Xor(Terminal("A"), Terminal("B"))))
    )
    input = input.desugar()

    print(str(input))
