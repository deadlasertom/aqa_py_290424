from abc import ABC, abstractmethod

class TestABC(ABC):
    @abstractmethod
    def setup(self):
        """Метод для підготовки до тесту."""
        pass

    @abstractmethod
    def test(self):
        """Метод для виконання тесту."""
        pass

    @abstractmethod
    def teardown(self):
        """Метод для очищення після тесту."""
        pass

class RealTest(TestABC):
    def setup(self):
        print("Підготовка до тесту прикладу")

    def test(self):
        print("Виконання тесту прикладу")

    def teardown(self):
        print("Очищення після тесту прикладу")

if __name__ == "__main__":
    test = RealTest()
    test.setup()
    test.test()
    test.teardown()
