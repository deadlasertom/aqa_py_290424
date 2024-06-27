"""Розробити клас Human.
Людина має:
    Ім'я
    Прізвище
    Дату народження
    Стать
    Енергію = 100
Люди можуть:
    Їсти (Енергія +5)
    Спати (Енергія +10)
    Говорити (Енергія -5)
    Ходити (Енергія -10)
    Робити домашку (Енергія -90)
if __name__ == "__main__":
    Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання
    декількох дій, вивести в кого найбільше енергії лишилося.
Створити тести на клас та на атрибути класу.
"""

from datetime import datetime

class Human:
    base_energy = 100
    Humans = []
    def __init__(self, f_name: str, l_name: str, gender: str, dob: datetime) -> None:
    
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.dob = dob
        Human.Humans.append (self)
        
    def eat(self):
        """ Eat to replenish 5 energy points """
        self.base_energy += 5
    def sleep(self):
        """ Sleep to replenish 10 energy points """
        self.base_energy += 10
        
    def talk(self):
        """ Talk with people, consumes 5 energy points"""
        self.base_energy -= 5
        self.energy_check()
    def walk(self):
        """ Walk from point a to point b, consumes 10 energy points """
        self.base_energy -= 10
        self.energy_check()
    def do_homework(self):
        """ Do the homework, consumes 90 energy points"""
        self.base_energy -= 90
        self.energy_check()
    def energy_check(self):
        """Controls character's energy"""
        if self.base_energy <= 0:
            self.base_energy = 1
            print (f"Too tired, {self.f_name} collapsed")
    
    @classmethod
    def energy_compare(cls):
        energy_counter = 0
        max_energy_person = ""

        if not cls.Humans:
            print ("The list of humans is empty")
            return
        for human in cls.Humans:
            if human.base_energy > energy_counter:
                energy_counter = human.base_energy
                max_energy_person = human.f_name
        print (f"{max_energy_person} has most energy. The energy meter is - {energy_counter}")
            
if __name__ == "__main__": 
   Johny = Human ("Johny", "Silverhand", "Male", datetime(1988, 11, 16))
   Adam = Human ("Adam", "Smasher", "Male", datetime(1980, 6, 21))
   Jack = Human ("Jack", "Welles", "Male", datetime(2046, 5, 26))
   Judy = Human ("Judy", "Alvarez", "Female", datetime(2053, 3, 13))
   Panam = Human ("Panam", "Palmer", "Female", datetime(2044, 1, 5))

   Johny.sleep()
   Johny.talk()

   Adam.eat()
   Adam.sleep()

   Jack.do_homework()
   Jack.do_homework()

   Judy.talk()
   Judy.walk()

   Panam.sleep()
   Panam.do_homework()

   Human.energy_compare()
