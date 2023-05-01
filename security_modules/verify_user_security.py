from typing import Union, Tuple

from databases.users_board.user import User
from security_modules.security_module import SecurityModule
from databases.users_board.users_board import UsersBoard
class UserLoginSecurity(SecurityModule):

    def __init__(self, user_db_object:UsersBoard):
        super().__init__(user_db_object)

    def fetch_and_verify_user(self, client_id: str, client_security_details) -> Tuple[bool, Union[None, User]]:
        user = self._user_db.login_user(client_id, client_security_details)
        return user.is_authenticated(), user

    def connected_client(self, client_id: str) -> Union[None, User]:

        return self._user_db.is_logged_in(client_id)
