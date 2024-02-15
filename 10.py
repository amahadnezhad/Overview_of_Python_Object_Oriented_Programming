"""
Exercise10 -> Create a Student Class With Name And Lastname And Age Attributes
              Print The Attributes With Method
"""


class Student:
    def __init__(self, f_name, l_name, age):
        self.firstname = f_name
        self.lastname = l_name
        self.age = age

    def show(self):
        print("FirstName: ", self.firstname)
        print("LastName: ", self.lastname)
        print("Age: ", self.age)


stu2 = Student('Reza', "Norzad", 32)
stu2.show()
