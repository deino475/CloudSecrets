from ._BaseProvider import BaseSecretStoreProvider

class IBMSecretStoreProvider(BaseSecretStoreProvider):
    def __init__(self, **kwargs):
        from ibm_cloud_sdk_core.authenticators.iam_authenticator import IAMAuthenticator
        from ibm_secrets_manager_sdk.secrets_manager_v2 import SecretsManagerV2

        self.client = SecretsManagerV2(
            authenticator=IAMAuthenticator(apikey=kwargs.get('api_key'))
        )
        self.client.set_service_url(kwargs.get('service_url'))
