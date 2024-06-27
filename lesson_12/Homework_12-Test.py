import unittest
from datetime import datetime
from homework_12 import Human

class homework_methods_test(unittest.TestCase):
    
    def setUp(self):
       self.Johny = Human ("Johny", "Silverhand", "Male", datetime(1988, 11, 16))
       self.Adam = Human ("Adam", "Smasher", "Male", datetime(1980, 6, 21))
       self.Jack = Human ("Jack", "Welles", "Male", datetime(2046, 5, 26))
       self.Judy = Human ("Judy", "Alvarez", "Female", datetime(2053, 3, 13))
       self.Panam = Human ("Panam", "Palmer", "Female", datetime(2044, 1, 5))

    def test_1_eat(self):
        self.Johny.eat()
        Actual_result = self.Johny.base_energy
        expected_result = 105
        self.assertEqual(Actual_result, expected_result )



    def test_2_sleep(self):
        self.Adam.sleep()
        Actual_result = self.Adam.base_energy
        expected_result = 110
        self.assertEqual(Actual_result, expected_result )
    
    def test_3_talk(self):
        self.Jack.talk()
        Actual_result = self.Jack.base_energy
        expected_result = 95
        self.assertEqual(Actual_result, expected_result )

    def test_4_walk(self):
        self.Judy.walk()
        Actual_result = self.Judy.base_energy
        expected_result = 90
        self.assertEqual(Actual_result, expected_result )


    def test_5_homework(self):
        self.Panam.do_homework()
        Actual_result = self.Panam.base_energy
        expected_result = 10
        self.assertEqual(Actual_result, expected_result )

    def test_6_homework_extreme(self):
        self.Panam.do_homework()
        self.Panam.do_homework()
        Actual_result = self.Panam.base_energy
        expected_result = 1
        self.assertEqual(Actual_result, expected_result )

    def test_7_Humans_list_ne(self):
        self.assertIsNotNone(Human.Humans)
    
if __name__ == "__main__":
    unittest.main(verbosity=4)