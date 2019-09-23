a = 2
b = 3

print('-------------')

# 类


class Student():
    name = 'siyue'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(age)
        print(name)

    def print_file(self):
        print('name: ' + self.name)
        print('age:' + str(self.age))
        print(Student.name)


student1 = Student('果果', 18)
# print(student1.name)
# print(student1.__dict__)
# print(Student.__dict__)
student1.print_file()