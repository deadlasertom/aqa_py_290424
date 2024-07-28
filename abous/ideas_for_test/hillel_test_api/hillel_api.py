import requests
base_api_url = "https://qauto.forstudy.space/api"


class Auth():

    @staticmethod
    def logout(s: requests.session):
        endpoint = "/auth/logout"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def signup(s: requests.session, request_body: dict):
        endpoint = "/auth/signup"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def signin(s: requests.session, request_body: dict):
        endpoint = "/auth/signin"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def resetpassword(s: requests.session, request_body: dict):
        endpoint = "/auth/resetpassword"
        return s.post(base_api_url+endpoint, json=request_body)


class Users():

    @staticmethod
    def current_get(s: requests.session):
        endpoint = "/users/current"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def profile_get(s: requests.session):
        endpoint = "/users/profile"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def profile_put(s: requests.session, request_body: dict):
        endpoint = "/users/profile"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def settings_get(s: requests.session):
        endpoint = "/users/settings"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def settings_put(s: requests.session, request_body: dict):
        endpoint = "/users/settings"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def resetpassword(s:requests.session, user_id:int, token:str):
        # TODO: make this part better
        if not isinstance(user_id, int):
            raise ValueError ("invalid 'user_id', must be integer")
        if not isinstance(token, str):
            raise ValueError ("invalid 'token', must be string")
        
        endpoint = f"/users/resetpassword/{user_id}/{token}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def email_put(s: requests.session, request_body: dict):  #email_put
        endpoint = "/users/email"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def password_put(s: requests.session, request_body: dict): #password_put
        endpoint = "/users/password"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def users_delete(s: requests.session):  #delete_users
        endpoint = "/users"
        return s.delete(base_api_url+endpoint)


class Cars():
    @staticmethod
    def brands_get(s: requests.session): #brands_get
        endpoint = "/cars/brands"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def brands_id_get(s: requests.session, request_body: dict): #brands_id
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/brands/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def models_get(s: requests.session):
        endpoint = "/cars/models"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def models_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/models/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_get(s: requests.session):
        endpoint = "/cars"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_post(s: requests.session, request_body: dict):
        endpoint = "/cars"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def cars_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_id_put(s: requests.session, request_body: dict):
        id_ = request_body.pop("id", 0)
        endpoint = f"/cars/{id_}"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def cars_id_delete(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.delete(base_api_url+endpoint)


class Expenses():

    @staticmethod
    def expenses_get(s: requests.session, request_body: dict):
        car_id = request_body.get("id", 0)
        page = request_body.get("page", 0)
        endpoint = "/expenses"
        query = {"carId": car_id, "page": page}
        return s.get(base_api_url+endpoint, params=query)

    @staticmethod
    def expenses_post(s: requests.session, request_body: dict):
        endpoint = "/expenses"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def expenses_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def expenses_id_put(s: requests.session, request_body: dict):
        id_ = request_body.pop("id") if request_body.get("id") is not None else request_body.get("carId", 1)
        endpoint = f"/expenses/{id_}"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def expenses_id_delete(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.delete(base_api_url+endpoint)


class Instructions():

    @staticmethod
    def instructions_get(s: requests.session, request_body: dict):
        car_brand_id = request_body.get("carBrandId", 0)
        car_model_id = request_body.get("carModelId", 0)
        page = request_body.get("page", 0)
        endpoint = "/instructions"
        query = {"carBrandId": car_brand_id,
                 "carModelId": car_model_id,
                 "page": page}
        return s.get(base_api_url+endpoint, params=query)

    @staticmethod
    def instructions_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/instructions/{id_}"
        return s.get(base_api_url+endpoint)


class API():
    auth = Auth()
    users = Users()
    cars = Cars()
    expenses = Expenses()
    instructions = Instructions()
