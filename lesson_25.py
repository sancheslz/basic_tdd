"""LESSON 25
Goal: Create a class called "Calc" with two methods, to show the n_previous and the next number
"""


class Calc:

    def __init__(self, initial: int):
        self.initial = initial

    def n_previous(self):
        return self.initial - 1

    def n_next(self):
        return self.initial + 1

    def both(self):
        return self.n_previous(), self.n_next()


if __name__ == "__main__":
    assert callable(Calc), "Class <Calc> not defined"
    assert callable(Calc.n_previous), "Function <n_previous> not defined"
    assert callable(Calc.n_next), "Function <n_next> not defined"

    calc = Calc(10)
    assert calc.n_previous() == 9, "Previous not working"
    assert calc.n_next() == 11, "Next not working"
    assert calc.both() == (9, 11), "Next not working"
