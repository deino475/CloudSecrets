from ._BaseProvider import BaseSecretStoreProvider

class AzureSecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient
        KVUri = f"https://{kwargs.get('key_vault_name')}.vault.azure.net"

        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=KVUri, credential=self.credential)
    
    def create(self, secret_name, secret_value):
        self.client.set_secret(secret_name, secret_value)
    
    def update(self, secret_name, secret_value):
        self.client.set_secret(secret_name, secret_value)
    
    def get(self, secret_name):
        return self.client.get_secret(secret_name)

    def delete(self, secret_name):
        poller = self.client.begin_delete_secret(secret_name)
        poller.result()



