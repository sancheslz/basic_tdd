"""LESSON 10
Goal: Check if the value is odd or even
"""


def odd_or_even(value: int) -> str:
    if value % 2 == 0:
        return 'even'
    return 'odd'


if __name__ == "__main__":
    assert callable(odd_or_even), "Function not defined"
    assert odd_or_even(4) == 'even', "Returning an even value"
    assert odd_or_even(5) == 'odd', "Returning an odd value"
