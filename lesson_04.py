"""LESSON 04
Goal: Discover the number of days in 'n' months
Hint: Consider all months with 30 days
"""

def count_month_days(months):
    return months * 30

if __name__ == "__main__":
    assert callable(count_month_days), "Function not defined"
    assert count_month_days(2) == 60, "Return not wornking"
    assert count_month_days(1) == 30, "Return not wornking"
