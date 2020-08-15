"""LESSON 23
Goal: Create a class called "Calc" that return a double of a number
"""


class Calc:

    def double(self, number: int) -> int:
        return number * 2


if __name__ == "__main__":
    assert callable(Calc), "Class not defined"
    assert callable(Calc.double), "Function not defined"
    assert Calc().double(2) == 4, "Return of double not working"
