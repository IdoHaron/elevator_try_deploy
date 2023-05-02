from json import dump
from abc import abstractmethod
from pathlib import Path
from abc import ABC
class JsonDB(ABC):
    #database_path=None
    @abstractmethod
    def __dict__(self):
        raise NotImplementedError


    #def __del__(self):
     #   self._save_db()