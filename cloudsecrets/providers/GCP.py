from ._BaseProvider import BaseSecretStoreProvider

class GCPSecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        from google.cloud import secretmanager_v1
        self.request_types = {
            'get' : secretmanager_v1.GetSecretRequest,
            'create' : secretmanager_v1.CreateSecretRequest,
            'update' : None,
            'delete' : secretmanager_v1.DeleteSecretRequest
        }
        self.client = secretmanager_v1.SecretManagerServiceClient()
        self.project_id = f"projects/{kwargs.get('project_id')}"
    
    def get(self, secret_name):
        request = self.request_types['get'](
            name=secret_name,
        )
        response = self.client.get_secret(request=request)
        return response
    
    def create(self, secret_name, secret_value):
        request = self.request_types['create'](
            parent=self.project_id,
            secret_id=secret_name,
            secret=secret_value
        )
        response = self.client.create_secret(request=request)
        return response
    
    def update(self, secret_name, secret_value):
        raise NotImplementedError

    def delete(self, secret_name):
        request = self.request_types['delete'](
            name=secret_name,
        )
        self.client.delete_secret(request=request)
