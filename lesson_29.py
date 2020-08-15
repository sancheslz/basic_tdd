"""LESSON 29
Goal: Create a function "bubble_sort" to order a list of values
"""


def bubble_sort(values_list, *, reverse=False):
    current = 0
    final = []
    for _ in range(len(values_list)):
        for item in values_list:
            if item > current:
                current = item
        final.insert(0, current) if not reverse else final.append(current)
        values_list.remove(current)
        current = 0
    return final


if __name__ == "__main__":
    assert callable(bubble_sort), "Function <bubble_sort> not defined"
    test = [50, 30, 20, 40, 70, 0, 60]

    data = [0, 20, 30, 40, 50, 60, 70]
    assert bubble_sort(test) == data, "Sorting not working"

    test = [50, 30, 20, 40, 70, 0, 60]
    data = [70, 60, 50, 40, 30, 20, 0]
    assert bubble_sort(test, reverse=True) == data, "Sorting not working"
