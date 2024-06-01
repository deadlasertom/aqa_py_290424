# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print ("Task 1")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

 # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
        

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

print ("Task 2")
def two_numbers_sum ():
    """adds two numbers"""
    num_1 = int(input ("Enter first number: "))
    num_2 = int(input ("Enter second number: "))
    result = num_1 + num_2
    return (f"The sum of the {num_1} and {num_2} is {result}")

example = two_numbers_sum()
print (example)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print ("Task 3")
task_3_list = [1,2,3,4,5,6,7,8,9,10]

def avarage_number (numbers):
    """calculates avarage number from the list"""
    items_counter = 0
    sum_counter = 0
    for i in numbers:
        items_counter = items_counter + 1
        sum_counter = sum_counter + i
    result = sum_counter / items_counter
    return result

task_3_example = avarage_number (task_3_list)
print("The avarage in list is :", task_3_example)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print ("Task 4")
def uno_reverse(string):
    "reverses string"
    return ''.join(reversed(string))
original_string = input("Enter text to revert: ")
print (uno_reverse(original_string))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print ("Task 5")
test_list = [1, 22, 333, 4444, 55555]
def max_from_list ():
    """Takes strings trough input, adds them to list and finds longest word in the list"""
    new_list = []
    while True:
        word = input ("Enter the word, that should be added to the list. Enter 'Quit' to finish. ")
        if word == "Quit":
            break
        else:
            new_list.append(word)
    return (max(new_list, key=len))
    
task_5 = max_from_list()
print ("The longest word is:", task_5)


# task 6
print ("Task 6")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    """Checks if second string is substring of the first one."""
    if str2 in str1:
        return str1.find(str2) #and print (f'"{str2}" is substring of "{str1}".')
    else:
        return -1 #and print (f'"{str2}" is not substring of "{str1}".')


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
print ("Task 7")
def aliens_game (alien_color):
        """Starts game where player should shoot at colored aliens"""
        
    if alien_color == "green":
        return (f"You got {alien_color} - 5 points!")
    elif alien_color != "green" and alien_color != "red" :
        return (f"You got {alien_color} - 10 points!")
    elif alien_color == "red":
        return (f"You got {alien_color} - 15 points!") 

print (aliens_game(input("Enter the color of alien you shoot: ")))

# task 8
print ("Task 8")
def pizza_maker ():
    """Asks user to enter toppings for his pizza"""
    pizza_topping = []
    temp = input("Please, enter desired topping. If you finished, enter 'quit' ")
    while True:
        if temp == 'quit':
            return (f"Your order is pizza with {pizza_topping}, thank you.")
            break
        else:
            pizza_topping.append (temp)
            temp = input(f"{temp} added to order. Anything else? ")

task8 = pizza_maker()
print(task8)

# task 9
print ("Task 9")
def fuel_calculator ():
    """Calculates how much fuel is needed and fuel refills needed during the trip"""
    distance = (int(input("Please, enter trip distance: ")))
    fuel_consumption = (int(input("Please, enter how much fuel your car consume every 100 km: ")))
    fuel_capacity = (int(input("Please, enter your fuel tank capacity: ")))
    t_fuel = distance / 100 * fuel_consumption
    stops = t_fuel / fuel_capacity 
    return (f"The family will need at least, {t_fuel}, liters of fuel, and refuel car, {stops}, times.")

trip = fuel_calculator()
print (trip)

# task 10
print ("Task 10")

def random_num_game ():
    """Starts game where player should guess number"""
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
task_9 = random_num_game()
print = (task_9)
