#A list stores multiple values in one variable.
#Dictionary stores data
 #Functions process data
 #max()→highest salary
 #min()→lowest salary
 #sum()+len()→average
employees = {
    "Kumar": 45000,
    "Arun": 52000,
    "Divya": 48000,
    "Meena": 60000
}
names = list(employees.keys())
salaries = list(employees.values())
def highest_paid(names, salaries):
    max_salary = max(salaries)
    index = salaries.index(max_salary)
    return names[index]
def lowest_paid(names, salaries):
    min_salary = min(salaries)
    index = salaries.index(min_salary)
    return names[index]
def average_salary(salaries):
    return sum(salaries) / len(salaries)
print("Highest Paid:", highest_paid(names, salaries))
print("Lowest Paid:", lowest_paid(names, salaries))
print("Average Salary:", int(average_salary(salaries)))
