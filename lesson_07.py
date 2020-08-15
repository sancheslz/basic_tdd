"""LESSON 07
Goal: Write a code that return the previous and the next value of a number
"""

def pn_value(number):
    return number-1, number+1

if __name__ == "__main__":
    assert callable(pn_value), "Function doesn't exit"
    assert pn_value(10) == (9, 11), "Return not working"
