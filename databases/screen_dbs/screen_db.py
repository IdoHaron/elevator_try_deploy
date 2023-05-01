from abc import abstractmethod
from exceptions.database_error.exceptions import ValueNotFound

class ScreenDB:
    modified_screens:set = set()

    def __init__(self, path_current_db_state):
        self._current_db_state:dict = self._load_db(path_current_db_state)
        self.database_path =path_current_db_state

    @abstractmethod
    def _load_db(self, path_current_db_state):
        raise NotImplementedError

    def get_image(self, screen_id:str):
        if not self.legal_screen_id(screen_id):
            raise ValueNotFound
        if screen_id in self.modified_screens:
            self.modified_screens.remove(screen_id)
        return self._current_db_state[screen_id]

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
    def modify_screen(self, screen_id:str, image:str):
        raise NotImplementedError

    def __dict__(self):
        return self._current_db_state.copy()

    def legal_screen_id(self, screen_id) -> bool:
        return screen_id in self.__dict__().keys()