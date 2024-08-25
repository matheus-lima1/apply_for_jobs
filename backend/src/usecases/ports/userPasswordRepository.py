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
            print(f"Error finding password: {e.response['Error']['Message']}")
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
            print(f"Error creating item: {str(error)}")
            return False