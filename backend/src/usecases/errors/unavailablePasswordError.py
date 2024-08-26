class UnavailablePasswordError(Exception):
        def __init__(self):
            message = 'Senha indisponível'
            super().__init__(message)