import pytest

# use fixture
# def test_addition(input_data):
#     x, y, result = input_data
#     assert result == x + y
def add(x, y):
    return x + y

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -5, 5)
])
def test_addition(x, y, expected):
    result = add(x, y)
    assert result == expected


# Фікстура для обробки значення параметра
@pytest.fixture
def prepare_data(request):
    data = request.param * 2
    return data

# Параметризований тест з використанням фікстури та параметра indirect
@pytest.mark.parametrize("prepare_data", [1, 2, 3], indirect=True)
def test_example(prepare_data):
    assert prepare_data % 2 == 0
