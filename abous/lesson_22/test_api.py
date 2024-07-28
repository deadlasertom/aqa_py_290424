from lesson_22 import auth_signup


def test_auth_signup():
    name = "Aa"
    last_name = "Bbb"
    email = "someone1232148384@gmail.com"
    password = "QAsd1234!@"
    response = auth_signup(name, last_name, email, password)
    assert response.status_code == 201, "Wrong status code"
    r_json = response.json()
    assert r_json.get("status") == "ok", "Key 'status' is not ok"
