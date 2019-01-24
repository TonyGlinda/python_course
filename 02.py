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


# 创建一个类的对象
a = Employee('Tony', 30000)
a.dispaly_employee()
a.display_count()
