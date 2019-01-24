class Parent:
    parent_attr = 100

    def __init__(self):
        print('调用父类构造函数')

    def parentmethod(self):
        print('调用父类方法')

    def setattr(self, attr):
        Parent.parent_attr = attr

    def getattr(self):
        print('父类属性：', Parent.parent_attr)


class Child(Parent):
    def __init__(self):
        print('调用子类构造函数')

    def childmethod(self):
        print('调用子类的方法')


c = Child()     # 实例化类
c.childmethod()  # 调用子类方法
c.parentmethod()    # 调用父类方法
c.setattr(200)      # 再次调用父类方法，设置属性
c.getattr()     # 再次调用父类方法，获取属性值。


class Parent:  # 定义父类
    def mymethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def mymethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.mymethod()  # 子类调用重写方法
