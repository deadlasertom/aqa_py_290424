

# number = input("Enter number:")
# number_int = int(number)
# print (number_int>3)

def input_number(message: str = "Enter number:") -> int:
    """Convert sting input to int or None"""
    number = input(message)
    try:
        number_int = int(number)
    except ValueError:
        print("Try again!")
        number_int = input_number()
    return number_int

# number_int = input_number()
# print (number_int>3)


def div(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("b is equal 0! Fix it!")
       #return
    return result

def minicalc():
    a = input_number( "Enter number A:")
    b = input_number( "Enter number B:")

    return div(a, b)

# result = minicalc()
# print(result)


print ("*" * 88)
def is_ping_db(conut_pings: int) -> bool:
    if  54 > conut_pings >= 5:
        return True
    elif conut_pings >= 55:
        raise TooLargeError("Too fast! Dont use local host")#conut_pings
    else:
        # built-in
        raise ConnectionError("Error db connection")

# print(is_ping_db(4))


class TooLargeError(Exception):
    def __init__(self, value) -> None:
        message = f"Value {value} is too large and hard to calculate"
        super().__init__(message)


def connect_to_db(name_of_db):
    count_ping = len(name_of_db)
    try:
        connect = is_ping_db(count_ping)
        # add action
        #return connect
    # except ConnectionError as e:
    #     print(e)  #, "Try again!"
    #     return
    # except TooLargeError as e:
    #     print(e)  #, "Use net!"
    #     return

    except (ConnectionError, TooLargeError) as e:
        print(f"Error '{e}' durring  connect to db")
        return "local"
    else:
        return count_ping
        # if not exception
    finally:
        pass # always!
    return connect



print(connect_to_db("aaaa"))
print(connect_to_db("bbbbbbb"))
print(connect_to_db("abba" * 55))




# def factorial(n:int):
#     if n > 100:
#         raise TooLargeError(n)

def read_readme():
    with open("README.md", encoding="utf8") as file:
        content = file.read()
    # file = None
    # try:
    #     file = open("README.md", encoding="utf8")
    #     content = file.read()
    # except Exception as e:
    #     print("Виникла помилка:", {e})
    #     return
    # finally:
    #     if file is not None:
    #         file.close()
    return content

print(read_readme())


# # print(div(1, 1))
# # print(connect_to_db("abcd"))
# # print(factorial(100))
# # print(factorial(10100))

# read_readme()