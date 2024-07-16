import json
import requests

from urllib import request, parse

def make_query():
    url = "https://www.example.com"
    response = request.urlopen(url)
    data = response.read()
    print(data)


def post_query():
    url = "https://www.example.com"
    data = {"key1": "value1"}
    encode_data = parse.urlencode(data).encode("utf8")
    response = request.urlopen(url, encode_data)
    data = response.read()
    print(data)

def get_json(url='http://jsonplaceholder.typicode.com/posts/1/comments'):

    response = requests.get(url)
    if response.status_code == 200:
        # try
        data = response.json()  # отримання даних у форматі JSON
        # except
        return data
    else:
        raise AttributeError("WRONG!", response.status_code)
    
def get_with_qp():
    url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
    params = {'postId': 1, 'id': 1} # 'email': 'Nikita@garfield.biz'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()  # отримання даних у форматі JSON
        except json.decoder.JSONDecodeError as e:
            raise e
        return data
    else:
        raise AttributeError("WRONG!", response.status_code)

def post_me():
    url = 'http://jsonplaceholder.typicode.com/posts'
    data_to_send = {'userId': 10, 'id': 101, 'title': 'Some title'}

    response = requests.post(url, data=data_to_send)

    # Перевірка статус-коду
    if response.status_code == 201:
        created_data = response.json()  # отримання даних у форматі JSON
        print('Створено дані:', created_data)
    else:
        print('Помилка. Статус-код:', response.status_code)


def put_me():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}

    response = requests.put(url, data=data_to_send)

    # Перевірка статус-коду
    if response.status_code == 200:
        created_data = response.text  # отримання даних у форматі JSON
        print('Створено дані:', created_data)
    else:
        print('Помилка. Статус-код:', response.status_code)

def delete_me():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}

    response = requests.delete(url, data=data_to_send)

    # Перевірка статус-коду
    if response.status_code == 200:
        print('Дані успішно видалено')
    else:
        print('Помилка. Статус-код:', response.status_code)



def put_me_as_json():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}

    response = requests.put(url, json=data_to_send)

    # Перевірка статус-коду
    if response.status_code == 200:
        created_data = response.json()  # отримання даних у форматі JSON
        print('Створено дані:', created_data)
    else:
        print('Помилка. Статус-код:', response.status_code)

def user_agent():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0', 
               'Content-Type': 'application/json'}
    data_to_send = {'userId': 10, 'id': 101, 'title': 'New title'}

    response = requests.put(url, json=data_to_send, headers=headers)
    return response


if __name__ == "__main__":
    #post_query()
    data = get_with_qp()  # get_json()
    print(data)
    data2 = post_me()
    put_me()
    delete_me()
