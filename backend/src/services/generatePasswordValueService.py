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
            raise ValueError("Políticas de senha não definidas, não permitido gerar senha.")
        
        password = []
        if policies.get('uppercase'):
            password.append(random.choice(string.ascii_uppercase))
        if policies.get('lowercase'):
            password.append(random.choice(string.ascii_lowercase))
        if policies.get('numeric'):
            password.append(random.choice(string.digits))
        if policies.get('special'):
            password.append(random.choice(string.punctuation))
        
        remainingLength = minLength - len(password)
        if remainingLength > 0:
            password.extend(random.choices(passwordCharacters, k=remainingLength))
        
        random.shuffle(password)
        
        password = ''.join(password)
        
        return password
    
    # função anterior que falhava nos testes unitários
    # def generate(self, policies, minLength):
    #     passwordCharacters = []

    #     if policies.get('uppercase'):
    #         passwordCharacters.extend(string.ascii_uppercase)
    #     if policies.get('lowercase'):
    #         passwordCharacters.extend(string.ascii_lowercase)
    #     if policies.get('numeric'):
    #         passwordCharacters.extend(string.digits)
    #     if policies.get('special'):
    #         passwordCharacters.extend(string.punctuation)

    #     if not passwordCharacters:
    #         raise ValueError("No policies are set to True, cannot generate password.")
        
    #     password = ''.join(random.choice(passwordCharacters) for _ in range(minLength))

    #     # melhoria futura > trocar recursão por retry        
    #     if not self.validatePasswordService.validatePolicies(password, policies, minLength):
    #         return self.generate(policies, minLength)

    #     return password
