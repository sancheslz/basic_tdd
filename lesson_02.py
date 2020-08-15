"""LESSON 02
Goal: Create a function that return the double of a value
"""


def double(value):
    return value * 2


if __name__ == "__main__":
    assert callable(double), "Function not defined"
    assert double(10) == 20, "Return doesn't match"
