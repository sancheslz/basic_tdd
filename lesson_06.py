"""LESSON 06
Goal: Create a function that return the simple interest of some value
"""

def simple_interest(amount, tax, n_months):
    return amount * (tax / 100) * n_months


if __name__ == "__main__":
    assert callable(simple_interest), "Function not defined"
    assert simple_interest(16000, 4, 4) == 2560, "Returned value not right"
