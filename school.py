# Parent class: Person
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."


# Child class: Student
class Student(Person):
    def __init__(self, name, age, country, major, gpa):
        super().__init__(name, age, country)
        self.major = major
        self.gpa = gpa

    def study(self):
        return f"{self.name} is studying {self.major} with a current GPA of {self.gpa}."


# Child class: Staff
class Staff(Person):
    def __init__(self, name, age, country, position, department):
        super().__init__(name, age, country)
        self.position = position
        self.department = department

    def work(self):
        return f"{self.name} works as a {self.position} in the {self.department} department."


# Example usage
if __name__ == "__main__":
    # Create Person object
    person_1 = Person("Manny", 33, "USA")
    print(person_1)  # Manny is 33 years old and is from USA.

    # Create Student object
    student_1 = Student("Tammy", 19, "Vietnam", "Computer Science", 3.54)
    print(student_1.study())  # Tammy is studying Computer Science with a current GPA of 3.54.

    # Create Staff object
    staff_1 = Staff("Brittney", 36, "Canada", "Neuroscientist", "Biology")
    print(staff_1.work())  # Brittney works as a Neuroscientist in the Biology department.
