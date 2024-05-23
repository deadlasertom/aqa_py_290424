"""Python Built in Functions"""

def name():
    a = 1 + 1
    return a

# abs()  #    Returns the absolute value of a number
print(abs(-5))
# all()  #	Returns True if all items in an iterable object are true
print(all("abc"))
print(all([1, 2, 3]))
print(all([1, 2, 0]))
# any()  #	Returns True if any item in an iterable object is true
print(any([1, 2, 0]))
print(any([1, 0, 0]))
print(any([0, 0, 0]))
# ascii()  #	Returns a readable version of an object. Replaces none-ascii characters with escape character
print(ascii("Україна"))
# bin()  #	Returns the binary version of a number
print(bin(8))
# bytearray()  #	Returns an array of bytes
byte_array = bytearray(b'Hello, World!')
byte_array[0] = 56
print(byte_array.decode('utf-8'))
# bytes()  #	Returns a bytes object
# callable()  #	Returns True if the specified object is callable, otherwise False
# chr()  #	Returns a character from the specified Unicode code.
print(chr(1111))
# classmethod()  #	Converts a method into a class method
# compile()  #	Returns the specified source as an object, ready to be executed
# complex()  #	Returns a complex number
# delattr()  #	Deletes the specified attribute (property or method) from the specified object
# dict()  #	Returns a dictionary (Array)
my_dict = dict(a="b", c=2134, d=[1, "s"])
print(my_dict) 
# dir()  #	Returns a list of the specified object's properties and methods
print(dir(my_dict))
# divmod()  #	Returns the quotient and the remainder when argument1 is divided by argument2
a = 7
b = 3
print(divmod(a, b)) 
print(a // b, a % b)

# enumerate()  #	Takes a collection (e.g. a tuple) and returns it as an enumerate object
fruits = ['apple', 'banana', 'cherry']
print(dict(enumerate(fruits)))
# eval()  #	Evaluates and executes an expression
expression = "3 + 5 * 2"
x = eval(expression)
print(x)
y = 3
z = eval("x+y")  # x+y #
print(z)
# exec()  #	Executes the specified code (or object)

# filter()  #	Use a filter function to exclude items in an iterable object

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter(is_even, numbers)
even_numbers = list(filtered_numbers)
print(even_numbers)

# float()  #	Returns a floating point number
# format()  #	Formats a specified value
# frozenset()  #	Returns a frozenset object
# getattr()  #	Returns the value of the specified attribute (property or method)
print(getattr(numbers, "pop"))

# globals()  #	Returns the current global symbol table as a dictionary
# hasattr()  #	Returns True if the specified object has the specified attribute (property/method)
print(hasattr(numbers, "pop"))

# hash()  #	Returns the hash value of a specified object
print(hash("Hello, World!"))
# help()  #	Executes the built-in help system
# hex()  #	Converts a number into a hexadecimal value
print(hex(42))
# id()  #	Returns the id of an object
print(id(numbers))
my_str = "asdsd"
print(id(my_str))
my_str = my_str + "sf"
print(id(my_str))
# input()  #	Allowing user input
# int()  #	Returns an integer number
print(int("11", 16) == 17)
print(int("10", 8) == 17)
# isinstance()  #	Returns True if a specified object is an instance of a specified object
print(isinstance(5, int))
# issubclass()  #	Returns True if a specified class is a subclass of a specified object
# iter()  #	Returns an iterator object
# len()  #	Returns the length of an object

# list()  #	Returns a list

# locals()  #	Returns an updated dictionary of the current local symbol table
# map()  #	Returns the specified iterator with the specified function applied to each item

# max()  #	Returns the largest item in an iterable
# min()  #	Returns the smallest item in an iterable
print(max(numbers))
print(min(numbers))
my_dict = {'apple': 5, 'banana': 10, 'kiwi': 3, 'orange':7}
max_key = max(my_dict, key=lambda k: my_dict[k])
print(max_key)

# memoryview()  #	Returns a memory view object

# next()  #	Returns the next item in an iterable
# object()  #	Returns a new object

# oct()  #	Converts a number into an octal

# open()  #	Opens a file and returns a file object
# ord()  #	Convert an integer representing the Unicode of the specified character
print(ord("ї"))
# pow()  #	Returns the value of x to the power of y
print(pow(3, 3))
# print()  #	Prints to the standard output device
# property()  #	Gets, sets, deletes a property
# range()  #	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()  #	Returns a readable version of an object
# reversed()  #	Returns a reversed iterator
# round()  #	Rounds a numbers
print(round(2.60))
print(round(2.5034235, 1))
print(round(2.40))
# set()  #	Returns a new set object
# setattr()  #	Sets an attribute (property/method) of an object
# slice()  #	Returns a slice object
print(numbers[2:5])
# sorted()  #	Returns a sorted list
# staticmethod()  #	Converts a method into a static method
# str()  #	Returns a string object
print(str(12345) + "6")
# sum()  #	Sums the items of an iterator
print(sum(numbers))
# super()  #	Returns an object that represents the parent class
# tuple()  #	Returns a tuple
# type()  #	Returns the type of an object
# vars()  #	Returns the **dict** property of an object
# zip()  #	Returns an iterator, from two or more iterators

base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)

list_of_words = ['apple', 'banana', 'cherry']
my_map = map(str.title, list_of_words)
upper_words = list(my_map)
print(upper_words)

list_of_words = ['apple', 'banana', 'cherry']
upper_words = [word.upper() for word in list_of_words]
print(upper_words)

list1 = [1, 2, 3,  5, 7]
list2 = ['a', 'b', 'c', 'd', "dd"]
list3 = ["ddd", "ffff", "dweree", "Hherue", ]
zipped = zip(list1, list2, list3)
print(list(zipped))

my_new_list = [3, 28, 6, 10, 3]

# print(isinstance(my_new_list, (int, list)))

#sort() та sorted()
print(my_new_list)
print(sorted(my_new_list))
print(my_new_list)
print(my_new_list.sort())
print(my_new_list)

print("*"*88)


# Додавання нової функції - Adding new functions
def print_lyrics():
    """Друкує пісню"""
    print("Ой у лузі червона калина похилилася")
    print("Чогось наша славна Україна зажурилася")

print_lyrics()


# Виклик функції
# Параметри та аргументи - Parameters and arguments
def square(number: int) -> int:
    """Calculate the square of number."""
    return number ** 2

print("3**2:", square(3))
print("2**2:", square(2))

# Функція з аргументами
def describe_pet(animal_type:str, pet_name:str) -> str:
    """Display information about a pet."""
    return f"My {animal_type}'s name is {pet_name.title()}."

out = describe_pet("shinshila", "pyizhyk")
print(out)
print(describe_pet("pyizhyk", "shinshila"))
print(describe_pet(pet_name="Seryoga", animal_type="cat"))

def make_pizza(*toppings):
    return f"your pizza contains: {', '.join(*toppings)}"
items = ["salo", "kovbasa", "moskali", "shos ishe"]
print(make_pizza(items))
print("****")


def comma(*args) -> str:
    for arg in args:
        print(arg)
comma(1)
comma(1, 2)
comma(1, 2, 3)
print("****")

print(make_pizza(("aplle", "banana", "kivi")))


def print_kwargs(**kwargs):
    if "age" in kwargs:
        print(f"You have AGE: {kwargs}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Приклад виклику функції
print_kwargs(name="John", age=25, city="New York")
print_kwargs(name="John", city="New York")


def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Опційні задані значення аргументів - Making an Argument Optional
def spam(a, b=42):
    return (a + b)
print(spam(1))
print(spam(1, 1))

def spam_two(a, b, c=3, d=42):
    return (a + b)

def spam_third(a, *args):
    return (a)
print(spam_third(1, 2, 3, 5, "ffff"))

def kward_spam(**kwargs):
    return (kwargs["a"]+kwargs["b"])

print(kward_spam(a=1, b=2, c=4))

# l_square = lambda x: x**2
# # print(l_square(5))

# mul = lambda x, y: x*y
# # print(mul(3, 2))

def check_input(user_input):
    if not isinstance(user_input, int):
        raise TypeError(f"Wrong type: {user_input} not int")

def a_plus_b(a:int, b:int, c=1, d=2, e=3) -> int:
    # check_input(a)
    # check_input(b)
    # check_input(c)
    # check_input(d)
    # check_input(e)
    list(map(check_input, [a, b, c, d, e]))
    return (a + b) * (2*a - b) 


print("a_plus_b(1,2)", a_plus_b(73, 27))
print("a_plus_b(1,2)", a_plus_b(73, 27, 44, 33, 77))
print(a_plus_b(1,2,3,4,"5"))