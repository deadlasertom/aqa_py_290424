# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = "red"
if alien_color == "green":
    print ("You got 5 points!")


# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = "red"
if alien_color == "green":
    print ("You got 5 points!")
else:
    print ("You got 10 points!")


# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == "green":
        print (f"You got {i} - 5 points!")
    elif i != "green" and i != "red" :
        print (f"You got {i} - 10 points!")
    elif i == "red":
        print (f"You got {i} - 15 points!")  

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = []
temp = input("Please, enter desired topping. If you finished, enter 'quit'")
while True:
    if temp == 'quit':
        print (f"Your order is pizza with {pizza_topping}, thank you.")
        break
    else:
        pizza_topping.append (temp)
        temp = input(f"{temp} added to order. Anything else?")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""
a = int(input("Enter your number"))
b = str(a)
c = 0
for i in b:
    c = int(i) + c
print (f"The sum of all digits in {a} = {c}.")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
c = 0
while True:
    a = int(input("Enter your numbers: "))
    if a == 0:
        print (f"The sum of your numbers is {c}")
        break
    else:
        c = a + c

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
while guesses < max_guesses:
    guess = int(input())
    if guess == secret_number:
        print ("Congratz, you win!")
        break
    elif guess > secret_number:
        print ("Your numbers is too big")
        guesses = guesses + 1
    elif guess < secret_number:
       print ("Your number is to small")
       guesses = guesses + 1
    if guesses == 5:
        print ("Sorry, you lost.")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for i in fruits:
    if i == "orange":
        continue
    else:
        print (i)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#result = ["Відповідь вставте сюди"]
#print(result)  #  [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i % 2 == 0]
print (f"Task 10 - result = {result}")