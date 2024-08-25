class NonExistsPasswordError(Exception):
        def __init__(self):
            message = 'Senha não encontrada'
            super().__init__(message)