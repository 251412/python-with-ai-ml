salaries = [25000, 40000, 52000, 61000, 30000, 80000]
def increase_salary(salaries):
    return list(map(lambda s: int(s + s * 0.10), salaries))
def high_salary_employees(salaries):
    return [s for s in salaries if s > 50000]
def total_payout(salaries):
    return sum(salaries)
updated_salaries = increase_salary(salaries)
high_salary = high_salary_employees(updated_salaries)
total = total_payout(updated_salaries)
print("Updated Salaries:", updated_salaries)
print("High Salary Employees:", high_salary)
print("Total Salary Payout:", total)
