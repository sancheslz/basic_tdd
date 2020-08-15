"""LESSON 17
Goal: Sum all numbers of a list
"""


def sum_my_list(my_list: list) -> int:
    total = 0
    for value in my_list:
        total += value
    return total


if __name__ == "__main__":
    assert callable(sum_my_list), "Function doesn't exist"
    assert isinstance(sum_my_list([1, 2]), int), "Return isn't an integer"
    assert sum_my_list(
        [10, 20, 30, 0]
    ) == 60, "Return not right"

    # Test Battery: Checking with builtin sum()
    from random import randrange
    for test in range(100):
        my_list = [randrange(0, 100) for x in range(0, 100)]
        assert sum_my_list(my_list) == sum(my_list), "Return not right"
