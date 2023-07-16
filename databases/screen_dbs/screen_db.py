from abc import abstractmethod
from exceptions.database_error.exceptions import ValueNotFound
from databases.screen_dbs.screen.Screen import Screen
from typing import Dict, List
from databases.screen_dbs.screen.basic_input_type import BasicInputType

class ScreenDB:
    modified_screens:set = set()

    def __init__(self, path_current_db_state):
        self._current_db_state:Dict[str, Screen] = self._load_db(path_current_db_state)
        self.database_path =path_current_db_state

    @abstractmethod
    def _load_db(self, path_current_db_state):
        raise NotImplementedError

    def get_image(self, screen_id:str):
        if not self.legal_screen_id(screen_id):
            raise ValueNotFound
        if screen_id in self.modified_screens:
            self.modified_screens.remove(screen_id)
        return self._current_db_state[screen_id].current_obj_encoding()


    def get_encoding_as_html(self, screen_id:str):
        if not self.legal_screen_id(screen_id):
            raise ValueNotFound
        if screen_id in self.modified_screens:
            self.modified_screens.remove(screen_id)
        return self._current_db_state[screen_id].current_obj_as_html()

    def get_all_obj_id(self, screen_id:str)->List[int]:
        return list(self._current_db_state[screen_id].all_obj.keys())

    def did_image_modify(self, screen_id:str):
        """
        :param screen_id: the id to check if modified
        :return: did the image that needs to be presented modified since the last fetch.
        """
        if screen_id in self.modified_screens:
            return True
        return False
    def _modified_screen(self, screen_id:str):
        self.modified_screens.add(screen_id)
    @abstractmethod
    def add_obj_to_screen(self, screen_id:str, image:BasicInputType):
        raise NotImplementedError

    def __dict__(self):
        return self._current_db_state.copy()

    def legal_screen_id(self, screen_id:str) -> bool:
        return screen_id in self.__dict__().keys()

    @abstractmethod
    def remove_obj(self, screen_id:str, obj_id:int):
        raise NotImplementedError

    @abstractmethod
    def _save_db(self):
        raise NotImplementedError

    @abstractmethod
    def flush_screen(self, screen_id:str):
        raise NotImplementedError