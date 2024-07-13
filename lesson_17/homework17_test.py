import unittest
from homework_17 import Employe, Manager, Developer, TeamLead



class staff_test(unittest.TestCase):

    def setUp(self):
       self.Johny = Employe ("Johny", 500)
       self.Adam = Manager ("Adam", 1000, "Security")
       self.Jack = Developer ("Jack", 600, "Python")
       self.Judy = TeamLead ("Judy", 700, "Development", "C++", 13)

    def test_1_employe(self):
       expected_result = ('Johny', 500)
       actual_result = (self.Johny.name, self.Johny.salary)
       self.assertEqual (actual_result, expected_result)

    def test_2_manager(self):
       expected_result = ('Adam', 1000, 'Security')
       actual_result = (self.Adam.name, self.Adam.salary, self.Adam.department)
       self.assertEqual (actual_result, expected_result)

    def test_3_employe(self):
       expected_result = ('Jack', 600, 'Python')
       actual_result = (self.Jack.name, self.Jack.salary, self.Jack.programming_language)
       self.assertEqual (actual_result, expected_result)

    def test_4_employe(self):
       expected_result = ('Judy', 700, 'Development', 'C++', 13)
       actual_result = (self.Judy.name, self.Judy.salary, self.Judy.department, self.Judy.programming_language, self.Judy.team_size)
       self.assertEqual (actual_result, expected_result)   

if __name__ == "__main__":
    unittest.main(verbosity=2)