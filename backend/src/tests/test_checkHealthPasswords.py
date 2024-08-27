import unittest
import time
from src.services.validatePasswordService import ValidatePasswordService

class TestCheckHealthPasswords(unittest.TestCase):

    def setUp(self):
        self.validatePasswordService = ValidatePasswordService(None)

    def testWithRemainingQueriesAndValidDeadline(self):
        password = {
            'remaining-queries': {'N': '5'},
            'deadline': {'N': str(int(time.time()) + 10000)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertTrue(result)

    def testWithNoRemainingQueries(self):
        password = {
            'remaining-queries': {'N': '0'},
            'deadline': {'N': str(int(time.time()) + 10000)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertFalse(result)

    def testWithNegativeRemainingQueries(self):
        password = {
            'remaining-queries': {'N': '-1'},
            'deadline': {'N': str(int(time.time()) + 10000)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertFalse(result)

    def testWithExpiredDeadline(self):
        password = {
            'remaining-queries': {'N': '5'},
            'deadline': {'N': str(int(time.time()) - 10000)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertFalse(result)

    def testWithNoRemainingQueriesAndExpiredDeadline(self):
        password = {
            'remaining-queries': {'N': '0'},
            'deadline': {'N': str(int(time.time()) - 10000)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertFalse(result)

    def testWithBoundaryDeadline(self):
        now = int(time.time())
        password = {
            'remaining-queries': {'N': '5'},
            'deadline': {'N': str(now)}
        }
        result = self.validatePasswordService.checkHealth(password)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
