def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @staticmethod
    def my_static_method():
        print("This is a static method.")

    @classmethod
    def my_class_method(cls):
        print("This is a class method.")

def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator2
def say_hello2(name):
    print(f"Hello, {name}!")


def setup_teardown_decorator(func):
    def wrapper(*args, **kwargs):
        setup()
        result = func(*args, **kwargs)
        teardown()
        return result
    return wrapper


@setup_teardown_decorator
def test_example():
    # Тут проводяться тести
    pass

def validate(a):
    assert isinstance(a, str), f"{a} is {type(a)}"

def validate_params_decorator(func):
    def wrapper(*args, **kwargs):
        # Валідація вхідних параметрів
        validate(args[0])
        result = func(*args, **kwargs)
        return result
    return wrapper

@validate_params_decorator
def test_example(param):
    # Тут проводяться тести
    pass

if __name__ == "__main__":
    say_hello()
    say_hello2("Siri")
    test_example("1")