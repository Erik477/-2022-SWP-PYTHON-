from enum import Enum


class Department(Enum):
    UNDEFINED = 0
    MANAGEMENT = 1
    MARKETING = 2
    PRODUCTION = 3


class gender(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2


class Person(object):
    def __init__(self, first_name: str, last_name: str, gender: gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Employee(Person):
    def __init__(self, first_name: str, last_name: str, gender: gender, department: Department = None):
        super().__init__(first_name, last_name, gender)
        if department is None:
            self.department = Department.UNDEFINED 
        else: self.department = department
        


class HeadOfGroup(Employee):
    def __init__(self, first_name: str, last_name: str, gender: gender, department: Department = None):
        super().__init__(first_name, last_name, gender, department)


class Company:
    def __init__(self, employees: list = None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def count_employees_via_type(self, employee_type: type):
        return len([e for e in self.employees if type(e) == employee_type])

    def count_departments(self):
        return len({e.department for e in self.employees})

    def count_employees_per_department(self):
        departments = {e.department: 0 for e in self.employees}
        for e in self.employees:
            departments[e.department] += 1
        return departments

    def get_biggest_department(self):
        biggest_department = list(self.count_employees_per_department().keys())[0]
        for key in self.count_employees_per_department().keys():
            biggest_department = key if self.count_employees_per_department()[key] > \
                                        self.count_employees_per_department()[
                                            biggest_department] else biggest_department
        return biggest_department

    def get_gender_ration(self):
        counter = {
            gender.MALE: 0,
            gender.FEMALE: 0,
            gender.OTHER: 0
        }
        for employee in self.employees:
            counter[employee.gender] += 1 / len(self.employees)
        return counter


if __name__ == '__main__':
    company = Company([
        HeadOfGroup("Julian", "Schmid", gender.MALE, Department.PRODUCTION),
        Employee("Lucas", "Schebor", gender.FEMALE, Department.MARKETING),
        HeadOfGroup("Michael", "Zechner", gender.OTHER, Department.MARKETING)
    ])
    print(company.count_employees_via_type(Employee))
    print(company.count_employees_via_type(HeadOfGroup))
    print(company.count_departments())
    print(company.get_biggest_department())
    print(company.get_gender_ration())