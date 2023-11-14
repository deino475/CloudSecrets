from ._BaseProvider import BaseSecretStoreProvider

class InMemorySecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        self.data = kwargs.get('default_values', {})

    def get(self, secret_name):
        if secret_name in self.data:
            return self.data[secret_name]
        raise Exception("Key does not exist")
    
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
    
    def list_secrets(self):
        return list(self.data.keys())
    
