from time import sleep
from random import random
class User:
    max_comparison_time_python = 0.05
    def __init__(self, user_id: str, hashed_password:str):
        self.user_id = user_id
        self.__hashed_password= hashed_password
        self.__is_authenticated = False

    @property
    def is_active(self):
        return True

    def get_id(self):
        return  self.user_id

    def is_authenticated(self):
        return self.__is_authenticated

    def is_anonymous(self):
        return False

    def hasher(self, password:str)->str:
        # non hash
        return password


    def authenticate(self, password:str):

        self.__is_authenticated = self.__hashed_password==self.hasher(password)
        # can implement constant time
        sleep_time = random()*self.max_comparison_time_python
        sleep(sleep_time)
        return self.__is_authenticated
