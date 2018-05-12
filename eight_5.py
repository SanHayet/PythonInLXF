#实例属性和类属性

#count为类属性，所有实例可访问
class Student(object):
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1
        
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')