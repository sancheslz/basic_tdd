"""LESSON 01
Goal: Create two variable and then change their values
"""

a = 999
b = 555

a, b = b, a

print(a, b)

if __name__ == "__main__":
    assert a == 555, "Value of 'a' not changed"
    assert b == 999, "Value of 'b' not changed"