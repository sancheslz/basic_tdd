"""LESSON 13
Goal: Calculate the Bhaskara 
"""


def bhaskara(a, b, c):

    def delta(a, b, c):
        result = (b ** 2) - (4 * a * c)
        if result > 0:
            return result
        return False

    delta = delta(a, b, c)
    if delta:
        r1 = (-b + (delta ** 0.5)) / (2 * a)
        r2 = (-b - (delta ** 0.5)) / (2 * a)
        return int(r1), int(r2)
    return 'Delta not defined'


if __name__ == "__main__":
    assert callable(bhaskara), "Equation not defined"
    assert bhaskara(1, 0, -16) == (4, -4), "Return not right"
    assert bhaskara(1, -1, -6) == (3, -2), "Return not right"
    assert bhaskara(1, 0, -144) == (12, -12), "Return not right"
    assert bhaskara(7, 3, 4) == "Delta not defined", "Return not right"
