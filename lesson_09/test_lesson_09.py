import unittest
import myfunc_08

def sum(a, b):
    return a + b


class ExampleTest(unittest.TestCase):

    def test_01_my_func(self):
        a = 2
        b = 3
        actual_result = sum(a, b)
        expected_result = 5
        self.assertEqual(actual_result, expected_result, f"Sum numbers {a}+{b} is not equal {expected_result}")
    
    def test_02_external_div(self):
        a = 4
        b = 2
        actual_result = myfunc_08.div(a, b)
        expected_result = float(2)
        self.assertEqual(actual_result, expected_result, f"Div numbers {a} to {b} is not equal {expected_result}")

    def test_03_external_is_ping(self):
        conut_pings = 5
        actual_result = myfunc_08.is_ping_db(conut_pings)
        self.assertTrue(actual_result, f"is_ping_db retuned false for {conut_pings}")
        # self.assertNotEqual(a, b) # Перевіряє, чи a не дорівнює b
        # self.assertFalse(expr)
        # self.assertIsNone(a)
        # self.assertIsNotNone(a)
    
    def test_04_exception(self):
        with self.assertRaises(myfunc_08.TooLargeError):
            conut_pings = 55
            actual_result = myfunc_08.is_ping_db(conut_pings)
    
    def test_05_exception(self):
        with self.assertRaises(myfunc_08.TooLargeError):
            conut_pings = 56
            actual_result = myfunc_08.is_ping_db(conut_pings)

    def test_06_exception(self):
        with self.assertRaises(ConnectionError):
            conut_pings = 4
            actual_result = myfunc_08.is_ping_db(conut_pings)

if __name__ == "__main__":
    unittest.main(verbosity=2)
