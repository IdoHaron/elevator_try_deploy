from pathlib import Path
from abc import ABC, abstractmethod
from databases.db import DB

class MapDB(ABC, DB):
    @abstractmethod
    def __dict__(self)->dict:
        raise NotImplementedError
