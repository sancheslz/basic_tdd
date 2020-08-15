"""LESSON 27
Goal: Create a class that receiving three values, answer if it's a triangle or not
"""


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        if ((self.a > self.b + self.c) or \
            (self.b > self.a + self.b) or \
            (self.c > self.a + self.b)):
            return False
        return True


if __name__ == "__main__":
    assert callable(Triangle), "Class <Triangle> not defined"
    assert callable(Triangle.is_triangle), "Function <is_triangle> not defined"

    assert Triangle(3, 4, 5).is_triangle(), "Real triangle not found"
    assert Triangle(1, 4, 5).is_triangle(), "Fake triangle not found"
