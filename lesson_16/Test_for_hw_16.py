import unittest
from homework_16 import SiteUser

class homework_16_SiteUser_test(unittest.TestCase):

    def setUp(self) :
       self.Johny = SiteUser ("Johny Silverhand", "samurai1988@aft.com", "moderator")
       self.Adam = SiteUser("Adam Smasher", "smasher@arasaka.com", "admin")
       self.Jack = SiteUser ("Jack Welles", "Jaquito@araska.com", "user")

    def test_1_baselogcount(self):
       AR = self.Johny.logcount
       ER = 0
       self.assertEqual (AR, ER)

    def test_2_updatedlogcount(self):
       self.Johny.logcount = 13
       AR = self.Johny.logcount
       ER = 13
       self.assertEqual (AR, ER)

    def test_2_updatedlogcount(self):
       self.Johny.logcount = 13
       AR = self.Johny.logcount
       ER = 13
       self.assertEqual (AR, ER)

    def test_3_levels_eq(self):
       
       AR = self.Johny == self.Adam
       ER = False
       self.assertEqual (AR, ER)

    def test_4_levels_cmpr(self):
       
       AR = SiteUser.compare_levels (self.Jack, self.Adam)
       ER = f"User {self.Jack.name} and user {self.Adam.name} levels are not equal"
       self.assertEqual (AR, ER)
     
    def test_5_str(self):
       AR = str(self.Adam)
       ER = 'Name - "Adam Smasher". Email - "smasher@arasaka.com". Level - "admin".'
       self.assertEqual (AR, ER)

if __name__ == "__main__":
    unittest.main(verbosity=4)