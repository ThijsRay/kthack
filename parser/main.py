# Input:
#   And(x, y)
#   Or(x, y)
#   Not(x)
#   Terminal variables


class Operation:
    def simplifly(self):
        raise NotImplementedError("Class %s doesn't implement aMethod()" % (self.__class__.__name__))


class And(Operation):
    def __init__(self, x: Operation, y: Operation):
        self.x = x
        self.y = y

    def simplifly(self):
        And(self.x.simplifly(), self.y.simplify())


class Or(Operation):
    def __init__(self, x: Operation, y: Operation):
        self.x = x
        self.y = y

    def simplifly(self):
        Or(self.x.simplifly(), self.y.simplify())


class Not(Operation):
    def __init__(self, x: Operation):
        self.x = x

    def simplifly(self):
        Not(self.x.simplifly())


class Terminal(Operation):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def simplifly(self):
        Terminal(self.identifier)
