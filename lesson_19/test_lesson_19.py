import pytest


@pytest.fixture(scope="function")
def my_fixture():
    # Ця частина коду буде виконана перед кожним тестом,
    # який використовує цю фікстуру
    data = {"key": "value"}
    yield data


@pytest.fixture(scope="function", autouse=True)
def login():
    # templpate for user login
    print("templpate for user login")
    yield


def test_use_fixture(my_fixture):
    assert "key" in my_fixture
    assert my_fixture["key"] == "value"


def test_use_fixture_2(my_fixture):
    assert "key" in my_fixture
    assert my_fixture["key"] == "value"


def test_use_fixture_3():
    pass


class TestClass:
    def test_1(self):
        assert 1 == 1 
    
    def test_2(self):
        assert True      
    