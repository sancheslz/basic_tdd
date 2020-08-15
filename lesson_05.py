"""LESSON 05
Goal: Update salary value with a given tax
Hint: Consider the salary 1000.00/month and tax 15%
"""

def update_salary(salary, tax):
    if not isinstance(tax, float):
        tax = tax/100
    return salary * (1 + tax)



if __name__ == "__main__":
    assert callable(update_salary), "Function not defined"
    assert update_salary(1000, 15) == 1150, "Salary not updated"
    assert update_salary(1000, 0.15) == 1150, "Salary not updated"
