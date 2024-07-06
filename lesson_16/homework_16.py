"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = Користувач("John Doe", "john.doe@example.com", "user")
user2 = Користувач("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""

class SiteUser():
    
    def __init__(self, name: str, email: str, level: str) -> None:
        self.name = name
        self.email = email
        self.level = level
        self.logcount = 0
    def __str__(self):
        return f'Name - "{self.name}". Email - "{self.email}". Level - "{self.level}".'
    
    def __eq__(self, other_user):
        return self.level == other_user.level

    def compare_levels(self, other_user):
        
        if self.level == other_user.level:
           return f"User {self.name} and user {other_user.name} have equal levels."
        if self.level != other_user.level:
           return f"User {self.name} and user {other_user.name} levels are not equal"
        else:
            return "Unexpected result in comparison"
        
    @property
    def logcount(self):
        return self._logcount


    @logcount.setter
    def logcount(self, value):
        self._logcount = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    
if __name__ == "__main__": 

   user1 = SiteUser("John Doe", "john.doe@example.com", "user")
   user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
   print (SiteUser.compare_levels(user1, user2)) 
   print (user1 == user2)