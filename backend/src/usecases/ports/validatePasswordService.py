import time
class ValidatePasswordService:
    def __init__(self, repository):
        self.repository = repository

    def check(self, password):
        remainingQueries = int(password.get('remaining-queries', 0).get('N'))

        deadline = int(password.get('deadline', 0).get('N'))
        now = int(time.time())

        if (remainingQueries > 0 and now < deadline):
            return True
        else:
            return False