# Базис ООП
# успадкування
# інкапсуляція
# поліморфізм
# абстракція

# Життєвий цикл екземпляра класа
# __new__(cls, [...])
# __init__(self, [...])
# __del__(self)
# Інкапсуляція

from typing import Any


class Car():

    def __init__(self, dev, model):
        self.dev = dev
        self.model = model
    
    def __del__(self):
        print(f"The {self.dev} {self.model} object has been destroyed.")
    
    def __repr__(self) -> str:
        return f"The {self.dev} {self.model}"

    def __str__(self) -> str:
        return f"The {self.model} {self.dev} machine"
    
    def __len__(self) -> int:
        return len(self.model)+len(self.dev)
    
    def __add__(self, other_point):
        self.model = self.model + " " + str(other_point)
        return self.model

my_car = Car("Toyota", "Camry")  # init call here
print(my_car)
# print(my_car.dev, my_car.model)  # used
# del my_car  # destroy



print(len(my_car))
print(my_car + "Dkjsdjskj")

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)
    
    def __eq__(self, other_object: object) -> bool:
        return self.x == other_object.x and self.y == other_object.y
    
    def __call__(self, x) -> Any:
        self.x = self.x * x

point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(1, 2)
result = point1 + point2
print(result.x, result.y)
print(point1 == point2)
print(point1 == point3)
point1(5)
print(point1.x)

class Money():

    def __init__(self, amount: float) -> None:
        self.amount = amount
    
    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return type(self)(self.amount + other)
        else:
            raise ValueError("Неправильний тип вхідного значення для операції додавання")
 
    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount - other.amount)
        elif isinstance(other, (int, float)):
            return type(self)(self.amount - other)
        else:
            raise ValueError("Неправильний тип вхідного значення для операції додавання")
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return type(self)(self.amount * scalar)
        else:
            raise ValueError("Неправильний тип для операції множення")
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return type(self)(self.amount / scalar)
        else:
            raise ValueError("Неправильний тип або ділення на нуль")
    


class UAH(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)
 
    def __str__(self):
        return f"{self.amount:.2f} грн"
 
 
class USD(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)
 
    def __str__(self):
        return f"${self.amount:.2f}"

class ForEx():

    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell
    
    def convert_to_usd(self, uah_amount):
        if isinstance(uah_amount, UAH):
            usd_amount = uah_amount.amount / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

    def convert_to_uah(self, usd_amount):
        if isinstance(usd_amount, USD):
            uah_amount = usd_amount.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")


if __name__ == "__main__":
 
    my_uah_cash = UAH(3000)
    my_wife_uah_cash = UAH(30500)
    my_usd_cash = USD(100)
    wife_usd = USD(100)
    my_total_cash = my_uah_cash + my_wife_uah_cash 
    print(my_total_cash)
    print(my_usd_cash - 1)

    privatbank = ForEx(37.05, 37.57)
    akord_bank = ForEx(37.37, 38.00)

    pb_to_uah = privatbank.convert_to_uah(my_usd_cash)
    pb_to_usd = privatbank.convert_to_usd(my_uah_cash)
    ak_to_uah = akord_bank.convert_to_uah(my_usd_cash)
    ak_to_usd = akord_bank.convert_to_usd(my_uah_cash)

    print(f"Продати {my_usd_cash}:", pb_to_uah, "|", ak_to_uah)
    print(f"Купити на {my_uah_cash}:", pb_to_usd, "|", ak_to_usd)

    """
    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)
    """