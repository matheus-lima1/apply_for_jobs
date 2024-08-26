import time
import string

class ValidatePasswordService:
    def __init__(self, repository):
        self.repository = repository

    def checkHealth(self, password):
        remainingQueries = int(password.get('remaining-queries', 0).get('N'))

        deadline = int(password.get('deadline', 0).get('N'))
        now = int(time.time())

        if (remainingQueries > 0 and now < deadline):
            return True
        else:
            return False
        
    def validatePolicies(self, password, policies, minLength):
        if len(password) < minLength:
            return False

        if policies.get('uppercase') and not any(c.isupper() for c in password):
            return False
        if policies.get('lowercase') and not any(c.islower() for c in password):
            return False
        if policies.get('numeric') and not any(c.isdigit() for c in password):
            return False
        if policies.get('special') and not any(c in string.punctuation for c in password):
            return False

        return True

