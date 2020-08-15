"""LESSON 08
Goal: Create a function for each arithmetic operator (+, -, *, /) 
"""


def sum_values(a: int, b: int) -> int:
    return a + b


def diff_values(a: int, b: int) -> int:
    return a - b


def multi_values(a: int, b: int) -> int:
    return a * b


def divide_values(a: int, b: int) -> int:
    return a / b


if __name__ == "__main__":
    assert callable(sum_values), "Function <sum_values> not defined"
    assert callable(diff_values), "Function <diff_values> not defined"
    assert callable(multi_values), "Function <multi_values> not defined"
    assert callable(divide_values), "Function <divide_values> not defined"
    assert sum_values(10, 5) == 15, "Function <sum_values> not working"
    assert diff_values(10, 5) == 5, "Function <diff_values> not working"
    assert multi_values(10, 5) == 50, "Function <multi_values> not working"
    assert divide_values(10, 5) == 2, "Function <divide_values> not working"
