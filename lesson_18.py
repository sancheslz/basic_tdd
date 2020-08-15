"""LESSON 18
Goal: Write a function that copy all elements of a list
"""


def copy_all(initial_list: list) -> list:
    return initial_list[:]


if __name__ == "__main__":
    assert callable(copy_all), "Function doesn't exit"
    initial = [1, 2, 3, 4]
    copied = copy_all(initial)
    assert copied == initial, "Values aren't equal"
    assert id(copied) != id(initial), "Lists have the same id"
