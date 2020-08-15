"""LESSON 03
Create a function that return the square area
"""

def square(side_a, side_b):
    return side_a * side_b

if __name__ == "__main__":
    assert callable(square), "Function doesn't exist"
    assert square(10, 20) == 200, "Doesn't return the square area"
    assert square(3, 9) == 27, "Doesn't return the square area"