"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import unittest
from homework_15 import log_event

class TestLoginSystem(unittest.TestCase):


    def test_successful_login(self):
        log_event('john_doe', 'success')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: john_doe, Status: success', log_content)


    def test_old_password(self):
        log_event('jane_doe', 'expired')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: jane_doe, Status: expired', log_content)

    def test_incorrect_password(self):
        log_event('jack_doe', 'failed')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: jack_doe, Status: failed', log_content)

if __name__ == "__main__":
    unittest.main(verbosity=2)
