"""
https://petstore.swagger.io/

Опис: Swagger Petstore - це відкрите API, яке надає можливість управляти даними про домашніх тварин. За допомогою цього API можна додавати нових тварин, знаходити тварин за ідентифікатором, виконувати замовлення на тварин та багато іншого.

Вам потрібно реалізувати програму, яка взаємодіє з Swagger Petstore API, використовуючи HTTP запити. Основні методи запитів, які вам знадобляться: GET, POST, PUT, DELETE.

**Ваші завдання:**

1. Отримати список доступних тварин (метод GET).

1. Зробіть запит до /pet/findByStatus з параметром status, щоб отримати список усіх тварин.

    1. Обробіть відповідь сервера та виведіть список тварин на екран.

1. Додати нову тварину (метод POST).

    Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.

    Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.

    Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.

1. Знайти тварину за ідентифікатором (метод GET).

    1. Введіть ідентифікатор тварини, яку потрібно знайти.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.

    1. Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.

1. Видалити тварину за ідентифікатором (метод DELETE).

    1. Введіть ідентифікатор тварини, яку потрібно видалити.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор тварини, яку потрібно видалити.

    1. Обробіть відпові
"""
import json
import requests

def get_pets_by_status(status):
    url = "https://petstore.swagger.io/v2/pet/findByStatus"
    params = {'status': status}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        pets = response.json()
        for pet in pets:
            print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    else:
        print(f"Can't get pets. Error - {response.status_code}")

status = 'available' #"sold" / "pending"
#get_pets_by_status(status)

def add_pet_post(pet_data):
    url = "https://petstore.swagger.io/v2/pet"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(pet_data))

    if response.status_code == 201 or response.status_code == 200:
        #Насколько я понял, это особеност api, что возвращает 200, вместо 201 поэтому добавил or 
        print ("Pet added succesfully:", response.json())
    else:
         print(f"Can't add pet. Error - {response.status_code}, response{response.text}")

Jack_the_dog = {
    "name": "Jack the dog", 
    "status": "available"
    }

#add_pet_post(Jack_the_dog)

def get_pet_byid(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    params = {'id': id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        pet = response.json()
        print(f"ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}")
    elif response.status_code == 400:
        print ("Invalid ID supplied")
    elif response.status_code == 404:
        print ("pet not found")
    else:
        print(f"Can't get pets. Error - {response.status_code}")

getpetid = 1
get_pet_byid(getpetid)

def delete_pet_byid(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    params = {'id': id}
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        pet = response.json()
        print(f"Pet with id {id} is succesfully deleted")
    elif response.status_code == 400:
        print ("Invalid ID supplied")
    elif response.status_code == 404:
        print ("pet not found")
    else:
        print(f"Can'delete pet. Error - {response.status_code}")

delete_pet_id = 1
delete_pet_byid(delete_pet_id)
get_pet_byid(getpetid)