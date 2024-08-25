class ValidatePasswordService:
    def __init__(self, repository):
        self.repository = repository

    def exists(self, password):
        remaining_queries = password.get('remaining-queries', 0)
        if remaining_queries > 0:
            return True
        else:
            return False