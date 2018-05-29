#枚举类，既可以用成员名称引用枚举常量
#又可以直接根据value的值获得枚举常量

from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

#@unique用于检查保证没有重复值
@unique
class gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

    