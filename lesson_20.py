"""LESSON 19
Goal: Create a function that check if there are repeated values in a list
"""


def hasRepeated(my_list: list) -> bool:
    checked = list()
    for value in my_list:
        if value in checked:
            return True
        checked.append(value)
    return False


def hasRepeated_alternaive(my_list: list) -> bool:
    return len(my_list) != len(set(my_list))


if __name__ == "__main__":
    for func in [hasRepeated, hasRepeated_alternaive]:
        assert callable(func), "Function not defined"
        assert isinstance(
            func([1, 2]), bool
        ), "Returned value isn't a boolean type"
        assert func(
            [1, 2, 3, 2, 5]
        ) == True, "Don't work with repeated values"
        assert func(
            [1, 2, 3, 5]
        ) == False, "Don't work with non repeated values"
