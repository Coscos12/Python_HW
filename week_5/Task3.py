class Human:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = first_name.capitalize() + ' ' + last_name.capitalize()


class Employee(Human):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    @staticmethod
    def from_string(x):
        new_string = x.split('-')
        return Employee(new_string[0], new_string[1], new_string[2])
