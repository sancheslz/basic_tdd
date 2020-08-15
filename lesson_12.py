"""LESSON 12
Goal: Write a code that change from ºC to ºF or ºF to C
"""


def temp_converter(temp: int, to_scale: str) -> int:
    """Temperature converter from Celsius <> Fahrenheit

    Args:
        temp (int): integer of temperature to be converted
        scale (str): scale to be converted to

    Returns:
        int: value converted with the other scale
    """

    if to_scale.upper() == 'C':
        return int(((temp - 32) / 9) * 5)
    return int(((temp * 9) + 160) / 5)


if __name__ == "__main__":
    assert callable(temp_converter), "Function not defined"
    assert temp_converter(100, 'F') == 212, "Error on Celsius to Fahrenheit"
    assert temp_converter(212, 'C') == 100, "Error on Fahrenheit to Celsius"
