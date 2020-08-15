"""LESSON 16
Goal: Create a list with a range, both included
"""


def list_creator(min_number: int, max_number: int) -> list:
    return [
        number for number in range(min_number, max_number + 1)]


if __name__ == "__main__":
    assert callable(list_creator), "Function not defined"
    assert list_creator(1, 5) == [1, 2, 3, 4, 5], "Don't return all numbers"
