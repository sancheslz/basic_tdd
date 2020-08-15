"""LESSON 22
Goal: Write a code that invert some text passed
"""


def text_interver(text: str) -> str:
    return text[::-1]


if __name__ == "__main__":
    assert callable(text_interver), "Function not defined"
    assert text_interver('animal') == 'lamina', "Returned text don't match"
