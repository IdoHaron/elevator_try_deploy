from pathlib import Path
from typing import List

from databases.general_user_based_db import GeneralUserDBEntry
from databases.users_board.users_board import UsersBoard
from utils.data_types import UserId
from json import load
from exceptions.database_error.exceptions import ValueNotFound
from databases.users_board.user import User
from databases.json_db import JsonDB

class JsonUsersBoard(UsersBoard, JsonDB):
    def __dict__(self):
        return self.json_content.copy()

    def __init__(self, database_path: Path):
        super().__init__(database_path)
        self.json_content:dict = {}
        self.connect_to_db()

    def fetch_info_by_id(self, user_id: UserId) -> List[User]:
        print(user_id)

        if not self.value_in_database(user_id):
            raise ValueNotFound
        hashed_password= self.json_content[user_id]
        return [User(user_id, hashed_password)]

    def login_user(self, user_id:str, password:str):
        user = self.fetch_info_by_id(user_id)[0]
        user.authenticate(password)
        return user


    def connect_to_db(self):
        with self.database_path.open("r") as f:
            self.json_content = load(f)

    def value_in_database(self, value_in_db: str):
        print(self.json_content)
        return value_in_db in self.json_content.keys()

    def is_logged_in(self, user_id:str):
        user = self.fetch_info_by_id(user_id)[0]
        if user.is_authenticated():
            return user
        return False