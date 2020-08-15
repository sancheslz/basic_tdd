"""LESSON 21
Goal: Count the number of vowels of a text
"""


def vowels_count(text: str) -> int:
    total = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        total += text.lower().count(vowel)
    return total


if __name__ == "__main__":
    assert callable(vowels_count), "Function not defined"
    assert vowels_count('lorem') == 2, "Vowel count not working"
    assert vowels_count('SPAM') == 1, "Vowel count not working"
