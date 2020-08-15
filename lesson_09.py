"""LESSON 09
Goal: Calculate the car production cost. Use the equation below:
final_cost = factory_cost + (factory_cost * distributor_percent) + (factory_cost * tax_percent)
Note: Consider the follow values:
- factory_cost = 10000
- distributor_percent = 20%
- tax_percent = 45%
"""

distributor_percent = 0.20
tax_percent = 0.45


def final_cost(factory_cost):
    distributor_value = factory_cost * distributor_percent
    tax_value = factory_cost * tax_percent
    return factory_cost + distributor_value + tax_value


if __name__ == "__main__":
    assert callable(final_cost), "Function not defined"
    assert final_cost(10000) == 16500, "Function return not right"
