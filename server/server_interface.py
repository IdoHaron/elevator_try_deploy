from abc import abstractmethod
from server.utils import ServerState
class Server:

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def sever_state(self) -> ServerState:
        raise NotImplementedError

    @abstractmethod
    def change_server_state(self, wanted_server_state:ServerState):
        raise NotImplementedError