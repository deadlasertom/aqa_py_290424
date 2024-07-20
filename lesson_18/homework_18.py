def log_factorial_calls(func):
    def wrapper(n):
        print(f"Calling factorial({n})")
        result = func(n)
        print(f"Result = {result}")
        return result
    return wrapper

@log_factorial_calls
def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@log_factorial_calls
def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)

for value in factorial_generator(5):
   pass