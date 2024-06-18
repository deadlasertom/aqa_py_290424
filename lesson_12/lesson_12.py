

class MobilePhone:
    it_has_button = False

    def __init__(self, brandname: str, model: str, it_has_button: bool = False) -> None:
        """ 
        Init for MobilePhone
        brandname
        model
        """
        self.brandname = brandname
        self.model = model
        self.it_has_button = it_has_button


nokia = MobilePhone("Nokia", 4420, True)
# nokia.it_has_button = True
print("nokia", nokia.it_has_button, nokia.model, nokia.brandname)

iphone = MobilePhone("Iphone", 17)
print("iphone", iphone.it_has_button, iphone.model, iphone.brandname)

class Student():
    age = 27
    def __init__(self, name) -> None:
        self.name = name

alex = Student("Alex")

katya = Student("Katya")

print(alex.name, alex.age)
print(katya.name, katya.age)

class Bank():
    name = "SomeoneBnk"
    count = 0

    def __init__(self):
        self.count_me()
    
    @classmethod
    def count_me(cls):
        cls.count += 1
    
    @classmethod
    def all_change_name(cls, new_name):
        cls.name = new_name
    
    def change_name(self, new_name):
        self.name = new_name

    def __repr__(self) -> str:
        return f"Банк {self.name} існує!"

class Operation(Bank):

    def __init__(self):
        self.balance = 0
    
    @staticmethod
    def plus(a, b):
        return a + b
    
    def add(self, sum):
        """ add some money to acc """
        self.balance = self.plus(self.balance, sum)
    
    def withdraw(self, sum):
        self.balance = self.balance - sum
        # self.balance -= sum

class Account(Operation):

    def __init__(self, name: str, balance: float):
        self.acc_name = name
        self.balance = balance

    def __repr__(self) -> str:
        return f"Валюта: {self.acc_name}, Баланс: {self.balance}"

  

teta_bank = Bank()
teta_bank.change_name("Teta Bank")
print(teta_bank.name, teta_bank.count)

bogdana_bank = Bank()
bogdana_bank.change_name("Bogdana Bank")
print(bogdana_bank.name, bogdana_bank.count)

print(teta_bank.count)

# count_bks = Bank().plus(2, 2)
# print(count_bks)


oper_bank = Operation()
print(oper_bank.balance)
oper_bank.add(1000)
oper_bank.withdraw(50)
print(oper_bank.balance)
print(oper_bank)

grn_acc = Account("grn", 1000)

print(grn_acc.acc_name, grn_acc.balance, grn_acc.name)
grn_acc.add(1)
print(grn_acc.balance)
print(grn_acc)
print(teta_bank)
