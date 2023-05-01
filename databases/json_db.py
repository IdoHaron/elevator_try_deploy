from json import dump
from abc import abstractmethod
from pathlib import Path
from abc import ABC
class JsonDB(ABC):
    database_path=None
    @abstractmethod
    def __dict__(self):
        raise NotImplementedError
    def save_db(self):
        dictified = self.__dict__()
        print(self.database_path)
        print(dictified)
        #with self.database_path.open("w") as f:
        #    dump(dictified, f)

        # need to implement
        # need to finish implemenatation.

    def __del__(self):
        self.save_db()