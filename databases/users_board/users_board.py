from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from databases.general_user_based_db import GeneralUserDBEntry
from utils.data_types import UserId
from databases.users_board.user import User



class UsersBoard(GeneralUserDBEntry, ABC):
    @abstractmethod
    def login_user(self, user_id:str, password:str):
        raise NotImplementedError

    @abstractmethod
    def is_logged_in(self, user_id:str):
        raise NotImplementedError