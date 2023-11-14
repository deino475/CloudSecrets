from abc import ABC, abstractmethod

class BaseSecretStoreProvider(ABC):
    @abstractmethod
    def get(self, secret_name):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, secret_name, secret_value):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, secret_name, secret_value):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, secret_name):
        raise NotImplementedError

    @abstractmethod
    def list_secrets(self):
        raise NotImplementedError

    #Default supported magic methods
    def __contains__(self, key) -> bool:
        try:
            response = self.get(key)
            return response != None
        except:
            return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        if key in self:
            self.update(key, value)
            return
        self.create(key, value)
    
    def __delitem__(self, key):
        self.delete(key)
    