a = 2
b = 3

print('-------------')

# 类


class Student():
    sum = 0
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

        # 在实例方法中访问类变量
        print(Student.name)
        print(self.__class__.name)

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum)


student1 = Student('果果', 18)
# print(student1.name)
# print(student1.__dict__)
# print(Student.__dict__)
student1.print_file()
student1.plus_sum()
Student.plus_sum()
student1.add(1, 2)
Student.add(1, 2)
