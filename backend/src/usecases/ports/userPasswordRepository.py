import time
import boto3
import uuid
import os
from botocore.exceptions import ClientError


class UsersPasswordRepository:
    def __init__(self, dynamodb=None):
        self.table_name = 'users-password-dev'
        if not dynamodb:
            session = boto3.Session(profile_name='personal')
            self.dynamodb = session.client('dynamodb', region_name='us-east-1')
        else:
            self.dynamodb = dynamodb


    def findById(self, id):
        try:
            response = self.dynamodb.get_item(
                TableName=self.table_name,
                Key={'id': {'S': id}},
            )
            item = response.get('Item')
            if item:
                return item
            else:
                return None
        except ClientError as e:
            print(f"Erro ao buscar senha: {e.response['Error']['Message']}")
            return None
        
    def update(self, id: str, field: str, value: int, expression="#field = :val"):
        try:
            self.dynamodb.update_item(
                TableName=self.table_name,
                Key={'id': {'S': id}},
                UpdateExpression=f"SET {expression}",
                ExpressionAttributeNames={
                    '#field': field,
                },
                ExpressionAttributeValues={
                    ':val': {'N': str(value)}
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            print(f"Erro ao atualizar senha:: {e.response['Error']['Message']}")
            return None

    def create(self, remainingQueries: int, expirationTime: int, value: str):
        id = str(uuid.uuid4())
        try:
            self.dynamodb.put_item(
                TableName=self.table_name,
                Item={
                    'id': {'S': id},
                    'remaining-queries': {'N': str(remainingQueries)},
                    'deadline': {'N': str(expirationTime + int(time.time()))},
                    'value': {'S': str(value)}
                }
            )
            return id
        except Exception as error:
            print(f"Error ao criar senha: {str(error)}")
            return False