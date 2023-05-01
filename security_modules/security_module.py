from abc import abstractmethod
from typing import Union
from databases.users_board.users_board import UsersBoard
from typing import Tuple, Union
from databases.users_board.user import User

class SecurityModule:
    def __init__(self, user_db:UsersBoard):
        self._user_db = user_db
    @abstractmethod
    def fetch_and_verify_user(self, client_id: str, client_security_details) -> Tuple[bool, Union[None, User]]:
        raise NotImplementedError

    @abstractmethod
    def connected_client(self, client_id:str)->Union[None, User]:
        raise NotImplementedError
