import pytest
import os

@pytest.mark.smoke
def test_sum():
    a = 2 + 2
    b = 4
    assert a == b, f"{a} not equal {b}"

def test_string():
    a = "more equipment while keeping a light roll. Weak in magic"
    b = "more equipment while keeping a light roll. Weak in magic"
    assert a == b

def test_list():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a == b

def test_dict():
    a = {"a": 1}
    b = {"a": 1}
    assert a == b

def test_fail_example():
    x = 5
    y = 10
    # if x + y != 11:
    #     pytest.fail("Помилка: Сума x та y не дорівнює 11")
    assert x + y == 15

@pytest.mark.xfail()
def test_xfail_example():
    x = 5
    y = 10
    result = x + y
    expected = 11
    assert result == expected, "Очікуваний результат не співпада"

@pytest.mark.skip(reason="Пропущено бо я так хочу")
def test_for_skip():
    assert True

def is_windows():
    return os.name == "nt"

@pytest.mark.skipif(is_windows(), reason="Test for linux only")
def test_for_linux():
    assert True


def get_error():
    raise AttributeError("character name empty")

def test_error_an_msg():
    with pytest.raises(
        AttributeError,
        match="character name empty"
        ):
        get_error()