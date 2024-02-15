"""
Exercise8 -> Create a Student Class With Name And Lastname And Age Attribute
"""


class Student():
    def __init__(self, f_name, l_name, age):
        self.firstname = f_name
        self.lastname = l_name
        self.age = age


stu1 = Student('Amir', 'Mohammadi', 18)
print("FirstName: ", stu1.firstname)
print("LastName: ", stu1.lastname)
print("Age: ", stu1.age)
