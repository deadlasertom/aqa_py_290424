class Car:
    def __init__(self, dev, model):
        self.dev = dev # Public attribute
        self._model = model # Protected attribute
        self.__run_meter = 2022 # Private attribute
    
    def display_model(self):
        return (f"Model: {self._model}")
    
    def update_meter(self, run_meter):
        self.__run_meter = self.__run_meter + run_meter
    
    def get_run_meter(self):
        return (f"Run: {self.__run_meter}")

my_car = Car("Toyota", "Camry")
print(my_car.dev)
print(my_car.display_model())
my_car.update_meter(1000)
print(my_car.get_run_meter())
my_car._model = "Corola"
print(my_car._model)


class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Chameleon(Animal):
    pass
# Використання поліморфізму
animals = [Dog("Bingo"), Cat("Felix"), Chameleon("Color")]
for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")


class Person():
 
    def __init__(self, age:int) -> None:
        self.__age = age
        self.__name = ""
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, add_year:int):
        #self.__age = add_year
        if not isinstance(add_year, int):
            raise ValueError("add_year must be int")
        if add_year > self.__age:
            self.__age = self.__age + add_year
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name, str):
            raise ValueError("new_name must be str")
        if len(new_name) >= len(self.__name):
            self.__name = new_name

p = Person(3)
print(p.age)
p.age = 4 
print(p.age)
p.name = "a"
print(p.name)
p.name = "aa"
print(p.name)
p.name = "b"
print(p.name)
