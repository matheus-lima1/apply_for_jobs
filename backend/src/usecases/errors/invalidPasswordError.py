class InvalidPasswordError(Exception):
        def __init__(self):
            message = 'Senha indisponível para visualização'
            super().__init__(message)