from c2 import Human


class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        
        # 子类调用父类的方法
        # Human.__init__(self, name, age)   不推荐
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print('do homework')
        super(Student, self).do_homework()


student1 = Student('人民路小学', '果果', 18)
# print(student1.sum)
# print(Student.sum)
print(student1.name)
print(student1.age)
student1.do_homework()
# student1.get_name()
