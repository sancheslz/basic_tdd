"""LESSON 26
Goal: Create a class that calc the simple interest
"""


class Financial:

    def simple(self, amount, tax, months):
        return amount * tax * months


if __name__ == "__main__":
    assert callable(Financial), "Class <Financial> not defined"
    assert callable(Financial.simple), "Function <n_previous> not defined"

    assert Financial().simple(16000, 0.04, 4) == 2560, "Value not right"
