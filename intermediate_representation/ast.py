# Input:
#   And(x, y)
#   Or(x, y)
#   Not(x)
#   Terminal variables


class Operation:
    """
    Class that defines the AST types
    """
    def simplify(self):
        raise NotImplementedError("Class %s doesn't implement simplyfy()" % (self.__class__.__name__))


class And(Operation):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation

    def simplify(self):
        And(self.x.simplify(), self.y.simplify())


class Or(Operation):
    def __init__(self, x, y):
        self.x = x  # Operation
        self.y = y  # Operation

    def simplify(self):
        Or(self.x.simplify(), self.y.simplify())


class Not(Operation):
    def __init__(self, x):
        self.x = x  # Operation

    def simplify(self):
        Not(self.x.simplify())


class Terminal(Operation):
    def __init__(self, identifier):
        self.identifier = identifier  # String

    def simplify(self):
        Terminal(self.identifier)


if __name__ == "__main__":

    input = And(Or(Or("x", And("y", "z")), "x"), Or("x", Not(And("a", "x"))))
    input.simplify()

    print("Hey")
