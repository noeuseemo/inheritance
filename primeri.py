#1
class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")


#2
class Employee:

    def __init__(self, name):
        self.__name = name  # имя работника

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")

    def work(self):
        print(f"{self.name} работает")

#3
class Person:

    def __init__(self, name):
        self.__name = name   # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} ")


class Employee(Person):

    def work(self):
        print(f"{self.name} работает")


p1 = Employee("Алиса")
print(p1.name)
p1.display_info()
p1.work()

#4

class Employee:
    def work(self):
        print("Работник работает")



class Student:
    def study(self):
        print("Студент учится")


class WorkingStudent(Employee, Student):        
    pass



s1 = WorkingStudent()
s1.work()
s1.study()

#5

class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} работает")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} учится")


class WorkingStudent(Employee, Student):
    pass


ws = WorkingStudent("Вася")
ws.work()
ws.study()