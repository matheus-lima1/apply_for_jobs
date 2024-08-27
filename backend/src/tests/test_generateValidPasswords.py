import unittest
import string
from src.services.generatePasswordValueService import GeneratePasswordValueService
from src.services.validatePasswordService import ValidatePasswordService

class TestGenerateValidPasswords(unittest.TestCase):

    def setUp(self):
        self.validatePasswordService = ValidatePasswordService(None)
        self.generatePasswordValueService = GeneratePasswordValueService(self.validatePasswordService)

    def testGeneratePasswordUppercaseOnly(self):
        policies = {
            "uppercase": True,
            "lowercase": False,
            "numeric": False,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordLowercaseOnly(self):
        policies = {
            "uppercase": False,
            "lowercase": True,
            "numeric": False,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordNumericOnly(self):
        policies = {
            "uppercase": False,
            "lowercase": False,
            "numeric": True,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordSpecialOnly(self):
        policies = {
            "uppercase": False,
            "lowercase": False,
            "numeric": False,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseAndLowercase(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": False,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseAndNumeric(self):
        policies = {
            "uppercase": True,
            "lowercase": False,
            "numeric": True,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseAndSpecial(self):
        policies = {
            "uppercase": True,
            "lowercase": False,
            "numeric": False,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordLowercaseAndNumeric(self):
        policies = {
            "uppercase": False,
            "lowercase": True,
            "numeric": True,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordLowercaseAndSpecial(self):
        policies = {
            "uppercase": False,
            "lowercase": True,
            "numeric": False,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordNumericAndSpecial(self):
        policies = {
            "uppercase": False,
            "lowercase": False,
            "numeric": True,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseLowercaseNumeric(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": False
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseLowercaseSpecial(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": False,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordUppercaseNumericSpecial(self):
        policies = {
            "uppercase": True,
            "lowercase": False,
            "numeric": True,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordLowercaseNumericSpecial(self):
        policies = {
            "uppercase": False,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordAllPolicies(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        minLength = 7
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testGeneratePasswordWithoutPolicies(self):
        policies = {
            "uppercase": False,
            "lowercase": False,
            "numeric": False,
            "special": False
        }
        minLength = 7

        with self.assertRaises(ValueError):
            self.generatePasswordValueService.generate(policies, minLength)

    def testGeneratePasswordWithMinLength(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        minLength = 10
        password = self.generatePasswordValueService.generate(policies, minLength)

        self.assertTrue(len(password) >= minLength)

    def testValidatePasswordWithAllPolicies(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        password = "A1b2C3!"
        minLength = 7

        self.assertTrue(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testValidatePasswordTooShort(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        password = "A1b!"
        minLength = 7

        self.assertFalse(self.validatePasswordService.validatePolicies(password, policies, minLength))

    def testValidatePasswordMissingCharacterType(self):
        policies = {
            "uppercase": True,
            "lowercase": True,
            "numeric": True,
            "special": True
        }
        password = "A1b2C3"
        minLength = 7

        self.assertFalse(self.validatePasswordService.validatePolicies(password, policies, minLength))


if __name__ == '__main__':
    unittest.main()
