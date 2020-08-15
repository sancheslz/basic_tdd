"""LESSON 14
Goal: Write a function that discover the divisor of a number
"""


def discover_divisors(number):

    # Return an iterator of divisors of a number
    def finder(number):
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                yield divisor

    return list(finder(number))


def discover_divisors_with_listcom(number):

    return [
        divisor for divisor in range(1, number + 1)
        if number % divisor == 0
    ]


if __name__ == "__main__":
    # Main Function
    assert callable(discover_divisors), "Function doesn't exist"
    assert isinstance(discover_divisors(10), list), "Return isn't a list"
    assert discover_divisors(10) == [1, 2, 5, 10], "Return of 10 not right"
    assert discover_divisors(9) == [1, 3, 9], "Return of 9 not right"

    # Alternative Version with List Comprehension
    assert callable(discover_divisors_with_listcom), "Function doesn't exist"
    assert isinstance(discover_divisors_with_listcom(10),
                      list), "Return isn't a list"
    assert discover_divisors_with_listcom(
        10) == [1, 2, 5, 10], "Return of 10 not right"
    assert discover_divisors_with_listcom(
        9) == [1, 3, 9], "Return of 9 not right"
