

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        super().get_details()
        print("Department:", self.department)


mgr = Manager("Divya", 75000, "IT")
mgr.get_details()
