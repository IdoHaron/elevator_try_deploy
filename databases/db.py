from abc import abstractmethod
class DB:
    @abstractmethod
    def __del__(self):
        raise NotImplementedError