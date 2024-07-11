import json
import math
# import mathplotlib as mpl
import os
import random
import re
import sys
# import lesson_20
from collections import OrderedDict
from datetime import datetime
from urllib import request

from lesson_20 import greeting as gr
#from lesson_20 import *

# lesson_20.greeting("alex")
# greeting("Alex")
print(math.pi)
print(math.sqrt(25))
print(25 ** (1/2))
now = datetime.now()
print(now)

print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))

current_directory = os.getcwd()  # отримуємо шлях до поточної папки
print(current_directory)
print(sys.version)
print(sys.path)

data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)   # перетворюємо словних у json
print(parsed_data)

pattern = re.compile(r'\b\w+\b')   # задаємо регуляний вираз
text = "Hello, world!"
matches = pattern.findall(text)    # здійснюємо пошук у тексті за виразом
print(matches)

# відкриваємо адресу
response = request.urlopen('https://www.example.com')
# читаємо зміст веб-документу
html = response.read()
print(html)

my_dict = {'a': 1,  'c': 3, 'b': 2,}
ordered_dict = OrderedDict(my_dict) 
print(ordered_dict)
print("******************")
print(dir(ordered_dict))
print("******************")
print(dir(my_dict))
print(dir())
print(dir(__builtins__))

if __name__ == "__main__":
    print("******************")
    print(json.__file__)
    print(gr.__name__)
