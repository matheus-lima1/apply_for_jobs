class InvalidPasswordError(Exception):
        def __init__(self):
            message = 'Senha inválida'
            super().__init__(message)