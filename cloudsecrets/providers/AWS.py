from ._BaseProvider import BaseSecretStoreProvider

class AWSSecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        import boto3
        self.client = boto3.client('secretsmanager')
    
    def get(self, secret_name: str, version_id: str = "AWSCURRENT") -> str:
        return self.client.get_secret_value(
            SecretId = secret_name,
            VersionId = version_id
        ).get('SecretString')
    
    def create(self, secret_name: str, secret_value: str, **kwargs) -> str:
        result = self.client.create_secret(
            Name=secret_name, 
            SecretString=secret_value
        )
        return result.get('ARN')

    def update(self, secret_name: str, secret_value: str, **kwargs) -> str:
        result = self.client.update_secret(
            SecretId=secret_name, 
            SecretString=secret_value
        )
        return result.get('ARN')
    
    def delete(self, secret_name: str, **kwargs) -> str:
        result = self.client.delete_secret(
            SecretId=secret_name
        )
        return result.get('ARN')
    
    def list_secrets(self):
        raise NotImplementedError
    
