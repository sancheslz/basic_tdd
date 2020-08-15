"""LESSON 19
Goal: Create a function that discover the bigger value of a list with aleatory numbers, return its index
"""


def bigger_number(numbers_list: list) -> int:
    bigger = 0
    for number in numbers_list:
        if number > bigger:
            bigger = number
    return numbers_list.index(bigger)


if __name__ == "__main__":
    assert callable(bigger_number), "Function not defined"
    assert isinstance(
        bigger_number([1, 2]), int), "Return isn't an integer"
    assert bigger_number([
        10, 12, 2, 30, 17
    ]) == 3, "Index don't match"

    # Test Battery: Using builtin functions
    from random import randrange
    for test in range(100):
        dataset = [
            randrange(1, number) for number in range(2, 100)
        ]
        assert bigger_number(dataset) == dataset.index(
            max(dataset)), "Returned index don't match"
