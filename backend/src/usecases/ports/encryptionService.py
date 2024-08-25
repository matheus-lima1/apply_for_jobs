from cryptography.fernet import Fernet
import base64
import hashlib
import boto3
import json

class EncryptionService:
    def __init__(self):
        self.salt = self._getSaltFromSecretsManager()
        self.key = self._generateKey()
        self.fernet = Fernet(self.key)

    def _getSaltFromSecretsManager(self) -> bytes:
        # session = boto3.session.Session()
        session = boto3.Session(profile_name='personal')
        client = session.client(service_name='secretsmanager', region_name='us-east-1')

        try:
            getSecretValueResponse = client.get_secret_value(SecretId='dev/test-salt')
            secret = getSecretValueResponse['SecretString']
            secretDict = json.loads(secret)
            return secretDict['salt'].encode()
        except Exception as e:
            print(f"Error retrieving secret (SM): {str(e)}")
            raise

    def _generateKey(self) -> bytes:
        key = hashlib.sha256(self.salt).digest()
        return base64.urlsafe_b64encode(key[:32])

    def encrypt(self, password: str) -> str:
        encryptedPassword = self.fernet.encrypt(password.encode())
        return encryptedPassword.decode()

    def decrypt(self, password: str) -> str:
        decryptedPassword = self.fernet.decrypt(password.encode())
        return decryptedPassword.decode()