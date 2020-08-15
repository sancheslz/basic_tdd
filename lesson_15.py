"""LESSON 15
Goal: Create a function that discover all prime numbers of an interval
"""


def is_prime(number: int) -> bool:
    data = list()
    for n in range(1, number):
        if number % n == 0:
            data.append(n)
    if len(data) < 2:
        return True
    return False


def prime_list(number: int) -> list:
    response = list()
    for value in range(2, number):
        if is_prime(value):
            response.append(value)
    return response


if __name__ == "__main__":
    # Discover if is a prime number
    assert callable(is_prime), "Function <is_prime> not found"
    assert is_prime(2) == True, "Don't return a prime number"
    assert is_prime(6) == False, "Don't return a prime number"

    # Discover the list of prime numbers
    assert callable(prime_list), "Function <prime_list>  not found"
    assert isinstance(prime_list(10), list), "Don't return a list"
    assert prime_list(10) == [2, 3, 5, 7], "Prime numbers not found"
