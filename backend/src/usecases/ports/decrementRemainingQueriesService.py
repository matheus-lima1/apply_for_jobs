class DecrementRemainingQueriesService:
    def __init__(self, userPasswordRepository):
        self.userPasswordRepository = userPasswordRepository

    def decrement(self, id):
        self.userPasswordRepository.update(
            id, "remaining-queries", 1, 
            expression="#field = #field - :val"
        )