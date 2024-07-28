import requests
import unittest
import random
import string
from hillel_api import API
s = requests.session()

"""Написати п'ять тестів на api, що покривають пункти

1. Реєстрація користувача

2. Створення машини POST cars

3. редагування машини

4. отримання даних через GET в Cars або Expenses

5. Видалення користувача

"""

def generate_random(length = 5):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))


class test_api_hw(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
       cls.session = requests.Session()
       cls.random_user_data =  {
                "name": generate_random(), 
                "lastName": generate_random(),
                "email": (f"{generate_random()}@mail.com"), 
                "password": "ABCabc123",
                "repeatPassword": "ABCabc123"}
       cls.default_user_data_signup = {
                "name": "Arthur", 
                "lastName": "Morgan",
                "email": "test12345@mail.com", 
                "password": "ABCabc123",
                "repeatPassword": "ABCabc123"
                }
       cls.default_user_data_signin = {
          "email": "test12345@mail.com",
          "password": "ABCabc123",
          "remember": False}         
       cls.test_car_data = {
             "carBrandId": 1,
             "carModelId": 1,
             "mileage": 155}
       cls.test_upd_car_data = {
             "carBrandId": 13,
             "carModelId": 14,
             "mileage": 3000}
       
   @classmethod
   def tearDownClass(cls):
      cls.session.close()
    
class Test_Auth(test_api_hw):
   def test_1_signup(self):
      response = API.auth.signup(self.session, self.random_user_data)
      print("Test 1 - TestAuth")
      print(f"Status code = {response.status_code}")
      print(f"Respons Body = {response.text}")
      self.assertEqual(response.status_code, 201)
      



class test_Users(test_api_hw):
   def test_2_delete(self):
       print("Test 2 - delete")
       API.auth.signup(self.session, self.default_user_data_signup)
       API.auth.signin(self.session, self.default_user_data_signin)
       response = API.users.users_delete(self.session)
       print(f"Status code = {response.status_code}")
       print(f"Respons Body = {response.text}")
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.text, ('{"status":"ok"}'))


class test_cars(test_api_hw):
   def test_3_post_car(self):
      print("Test 3 - post car")
      API.auth.signup(self.session, self.default_user_data_signup)
      API.auth.signin(self.session, self.default_user_data_signin)
      response = API.cars.cars_post(self.session, self.test_car_data)
      print(f"Response code = {response.status_code}")
      print(f"Response Body = {response.text}")
      self.assertEqual (response.status_code, 200) #В документации указан код 200 для Post/cars
      API.users.users_delete

   def test_4_update_car(self):
       print("Test 4 - update car")
       API.auth.signup(self.session, self.default_user_data_signup)
       API.auth.signin(self.session, self.default_user_data_signin)

       response_1 = API.cars.cars_post(self.session, self.test_car_data)
       response_1_json = response_1.json()
       car_id_ = response_1_json['data']['id']

       response_2 = API.cars.cars_id_put(self.session, car_id_, self.test_upd_car_data)
       response_2_json = response_2.json()
   
       car_mileage = response_2_json['data']["mileage"]

       print(f"Response code = {response_2.status_code}")
       print(f"Response Body = {response_2.text}")

       self.assertEqual (response_2.status_code, 200) 
       self.assertEqual (car_mileage, 3000)

       API.users.users_delete

#изначально планировал тестировать expenses, но не понял где взять номер странички 
   def test_5_get(self):
       print("Test 5 - get")
       API.auth.signup(self.session, self.default_user_data_signup)
       API.auth.signin(self.session, self.default_user_data_signin)
       response = API.cars.cars_get(self.session)
       print(f"Status code = {response.status_code}")
       print(f"Respons Body = {response.text}")
       self.assertEqual(response.status_code, 200)


       
   
if __name__ == '__main__':
    unittest.main()













