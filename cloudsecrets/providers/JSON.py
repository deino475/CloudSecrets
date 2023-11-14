from ._BaseProvider import BaseSecretStoreProvider
import json

class JSONSecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        self.data = None
        with open(kwargs['file_name'],'r') as f:
            self.data = json.load(f)

    def get(self, key):
        return self.data[key]
    
    def create(self, secret_name, secret_value):
        if secret_name in self.data:
            raise Exception("Key already exists")
        self.data[secret_name] = secret_value
    
    def update(self, secret_name, secret_value):
        if secret_name not in self.data:
            raise Exception("Key does not exist")
        self.data[secret_name] = secret_value
    
    def delete(self, secret_name):
        if secret_name not in self.data:
            raise Exception("Key does not exist")
        del self.data[secret_name]
        return True

    def list_secrets(self):
        return super().list_secrets()
    
