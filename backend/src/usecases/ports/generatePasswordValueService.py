import random
import string


class GeneratePasswordValueService:

    def __init__(self, validatePasswordService):
        self.validatePasswordService = validatePasswordService


    def generate(self, policies, minLength):
        passwordCharacters = []

        if policies.get('uppercase'):
            passwordCharacters.extend(string.ascii_uppercase)
        if policies.get('lowercase'):
            passwordCharacters.extend(string.ascii_lowercase)
        if policies.get('numeric'):
            passwordCharacters.extend(string.digits)
        if policies.get('special'):
            passwordCharacters.extend(string.punctuation)

        if not passwordCharacters:
            raise ValueError("No policies are set to True, cannot generate password.")
        
        password = ''.join(random.choice(passwordCharacters) for _ in range(minLength))

        # melhoria futura > trocar recursão por retry        
        if not self.validatePasswordService.validatePolicies(password, policies, minLength):
            return self.generate(policies, minLength)

        return password