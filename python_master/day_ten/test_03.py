class Student:
    __slots__ = ['_name', '_age', '_gender']

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def say(self):
        print('我是%s, 今年%d岁了' % (self._name, self._age))

    @staticmethod
    def is_adults(age):
        return age >= 18


def main():
    student1 = Student("张三", 13)
    print('我是%s, 今年%d岁了' % (student1.name, student1.age))

    student1.name = '李四'
    student1.say()
    student1._gender = '男'
    # student1._happy = ['唱', '跳', 'rap'] # 此处会报错

    if Student.is_adults(student1.age):
        print('你过关')
    else:
        print('该罚')


if __name__ == '__main__':
    main()
