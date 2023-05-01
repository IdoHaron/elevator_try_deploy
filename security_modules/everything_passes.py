from security_modules.security_module import SecurityModule
from databases.users_board.user import User
from typing import Tuple, Union

class EverythingPasses(SecurityModule):
    def __init__(self):
        super().__init__(None)
    def fetch_and_verify_user(self, client_id: str, client_security_details) -> Tuple[bool, Union[None, User]]:
        return True, User(client_id, "")

    def connected_client(self, client_id:str):
        return User(client_id, "")
