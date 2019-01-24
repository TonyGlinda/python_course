class Employee:
    ''' 所有员工的类
    '''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print('Total Employee {0}'.format(Employee.empCount))

    def dispaly_employee(self):
        print('Name : ', self.name, 'salary: ', self.salary)


# 创建第一个类的对象
a = Employee('Tony', 30000)
a.dispaly_employee()
a.display_count()
# 创建第二个类的对象
b = Employee('Glinda', 50000)
b.dispaly_employee()
b.display_count()
# 添加一个类属性
a.age = 24
print(a.age)
# 修改一个类的属性
a.age = 29
print(a.age)
# 删除一个类的属性
del a.age


# 你也可以使用下面的函数方式来访问属性。
hasattr(a, 'age')   # 如果存在age,则返回True
getattr(a, 'age')    # 返回age的属性值
setattr(a, 'age', 25)   # 添加属性age为25
print(a.age)
delattr(a, 'age')   # 删除属性age

# python的内置类属性

