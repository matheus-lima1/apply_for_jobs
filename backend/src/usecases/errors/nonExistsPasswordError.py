class NonExistsPasswordError(Exception):
        def __init__(self):
            message = 'Senha inexistente/expirada'
            super().__init__(message)