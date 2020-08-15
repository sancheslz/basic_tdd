"""LESSON 28
Goal: Create a Fibonacci sequence of n numbers 
"""


def fibonacci(value):
    sequence = list()
    for _ in range(1, value + 1):
        if len(sequence) < 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibonacci_last_number(value):
    if value < 2:
        return value
    return fibonacci_last_number(value - 1) + fibonacci_last_number(value - 2)


if __name__ == "__main__":
    assert callable(fibonacci), "Function <fibonacci> not defined"
    assert fibonacci(8) == [
        1, 1, 2, 3, 5, 8, 13, 21], "Returned sequence not working"

    # Function that return the fibonacci last number (recursively)
    assert callable(
        fibonacci_last_number), "Function <fibonacci_last_number> not defined"
    assert fibonacci_last_number(8) == 21, "Returned sequence not working"
