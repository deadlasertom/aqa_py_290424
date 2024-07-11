import pytest

# Припустимо, що у нас є кілька фіктивних фікстур для підготовки тестового середовища.
@pytest.fixture(scope='class')
def prepare_database():
    print("Підготовка бази даних...")
    yield
    print("Очищення бази даних...")

@pytest.fixture(scope='class')
def prepare_config():
    print("Підготовка конфігурації...")
    yield
    print("Очищення конфігурації...")


@pytest.fixture(params=[(1, 2, 3), (5, 5, 10), (10, 3, 13)])
def input_data(request):
    return request.param