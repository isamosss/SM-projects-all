# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3, json
from botocore.exceptions import ClientError

class RDSCredentials:
    
    def __init__(self):
        
        s = self.get_secret()
        
        self.username = s['username']
        self.password = s['password']
        
    def get_secret(self):
        
        secret_name = "rds!cluster-ce103000-f458-4d4c-a6a1-7cd11cec784f" 
        region_name = "us-east-2"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        # Decrypts secret using the associated KMS key.
        secret = get_secret_value_response['SecretString']

        return json.loads(secret)