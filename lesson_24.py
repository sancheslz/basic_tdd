"""LESSON 24
Goal: Create a class called "Area" that return the square and the cubic area of some number
"""


class Area:

    def square(self, a: int, b: int) -> int:
        return a * b

    def cubic(self, a: int, b: int, c: int) -> int:
        return a * b * c

    def magic(self, *args):
        total = 1
        for arg in args:
            total *= arg
        return total


if __name__ == "__main__":
    assert callable(Area), "Class <Area> not defined"
    assert callable(Area.square), "Function <square> not defined"
    assert callable(Area.cubic), "Function <cubic> not defined"

    area = Area()
    assert area.square(3, 9) == 27, "Return of square area not working"
    assert area.cubic(3, 6, 2) == 36, "Return of cubic area not working"

    # Fun test
    assert area.magic(3, 9) == 27, "Magic for square area not working"
    assert area.magic(3, 6, 2) == 36, "Magic for cubic area not working"
