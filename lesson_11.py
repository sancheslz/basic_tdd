"""LESSON 11
Goal: Discover if the value is positive or negative
"""


def is_positive(value: int) -> bool:
    if value < 0:
        return False
    return True


if __name__ == "__main__":
    assert callable(is_positive), "Function not defined"
    assert is_positive(3), "Error with positive numbers"
    assert not is_positive(-1), "Error with negative numbers"
    assert is_positive(0), "Zero must be positive"
