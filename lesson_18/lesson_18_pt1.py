

def fibonacci_generator(a=1, b=1):
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))

print("***")
fib2 = fibonacci_generator(34, 55)
for _ in range(10):
    print(next(fib))

print("***")

squares_generator = (x ** 2 for x in range(10))
print(type(squares_generator))
for square in squares_generator:
    print(square)

print("********")
def simple_generator():
    yield 1
    yield 2
    yield 3

gen_sim = simple_generator()

print(next(gen_sim))
print(next(gen_sim))


def count_up_to(count, limit):
    while count <= limit:
        yield count
        count += 1

# Створюємо генератор
counter = count_up_to(-20, 5)

print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print("(****)")
for i in counter:
    print(">", i)

gen_expr = (x ** 200 for x in range(10))

for n in gen_expr:
    print(n)


def exponent(x):
    return x ** 2.1415

my_nums = [1, 2, 4, 6]

ex_numbers = map(exponent, my_nums)

print(ex_numbers)
print(next(ex_numbers))
for i in ex_numbers:
    print(i)

def check_input(user_input):
    if not isinstance(user_input, (int, float)):
        raise TypeError(f"Wrong type: {user_input} not int")

def a_plus_b(a:int, b:int, c=1, d=2, e=3) -> int:
    list(map(check_input, [a, b, c, d, e]))
    # check_input(a)
    # check_input(b)
    # check_input(c)
    return (a + b) * (2 * a - b) + c - (d / e)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped_data = zip(names, ages)

print(zipped_data)
#print(next(zipped_data))
#print(dict(zipped_data))
for key, value in zipped_data:
    print(f"{key} is {value} years old.")
