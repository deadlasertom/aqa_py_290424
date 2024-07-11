import pytest
import os

# Використання фікстури tmpdir для створення тимчасового каталогу
def test_create_file_in_tmpdir(tmpdir):
    # Створення тимчасового файлу у тимчасовому каталогу
    file_path = tmpdir.join("test_file.txt")

    # Запис даних у створений файл
    file_path.write("Test data")

    # Перевірка, чи файл був створений та містить правильні дані
    assert file_path.isfile()
    assert file_path.read() == "Test data"

# Ще один приклад використання фікстури tmpdir
def test_create_directory_in_tmpdir(tmpdir):
    # Створення тимчасового каталогу у тимчасовому каталогу
    new_dir_path = tmpdir.mkdir("test_directory")

    # Перевірка, чи каталог був створений
    assert new_dir_path.isdir()

# Приклад використання фікстури tmpdir для перевірки її автоматичного видалення
def test_tmpdir_is_removed(tmpdir):
    # Перевірка, чи тимчасовий каталог існує перед видаленням
    assert os.path.exists(tmpdir)

# Після виконання тесту tmpdir буде видалено автоматично


# Використання фікстур з conftest.py на рівні класу.
@pytest.mark.usefixtures("prepare_database", "prepare_config")
class TestClassWithMultipleFixtures:
    def test_method1(self):
        print("Тестування методу 1...")

    def test_method2(self):
        print("Тестування методу 2...")
