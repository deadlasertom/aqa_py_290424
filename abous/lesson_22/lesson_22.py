import requests
from requests.auth import HTTPDigestAuth
from dotenv import dotenv_values

config = dotenv_values(".env")


base_url = "https://qauto.forstudy.space/api"

def auth_signup(name:str, last_name:str, email:str, password:str):
    user_data =  {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": password
        }
    # base
    auth = (config["USERNAME"], config["PASSWORD"])
    print(auth)
    auth_hash = HTTPDigestAuth('username', 'password')
    my_token = 'my_secret_token'
    headers = {'Authorization': f'Bearer {my_token}'}
    response = requests.post(base_url+"/auth/signup", json=user_data) # , auth=auth, headers=headers
    return response

if __name__ == "__main__":
    name = "Aa"
    last_name = "Bbb"
    email = "someone1232148@gmail.com"
    password = "QAsd1234!@"
    response = auth_signup(name, last_name, email, password)
    print(response.status_code)
