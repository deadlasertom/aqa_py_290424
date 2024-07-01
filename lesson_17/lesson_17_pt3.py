from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "Woooff"
    
    def sound(self):
        return "gav"

class Cat(Animal):
    
    def make_sound(self):
        pass

if __name__ == "__main__":
    bingo = Dog()
    print(bingo.make_sound())
    print(bingo.sound())
    felix = Cat()
    print(felix)
