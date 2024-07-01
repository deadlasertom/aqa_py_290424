from abc import ABC, abstractmethod


class Humanioid(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class Person():

    def __init__(self, name):
        self.name = name.title()

    def say_hello(self):
        print('Hi, I am', self.name)
    

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salry = salary
#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         self.salry = salary


    def say_hello(self):
        super().say_hello()
        print("My salary is:", self.salry)





if __name__ == "__main__":
    homo_sap = Person("ALICE")
    homo_sap.say_hello()
    
    worked_woman = Employee("mary", 20000)
    worked_woman.say_hello()
