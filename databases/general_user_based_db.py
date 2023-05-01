from __future__ import annotations

from abc import abstractmethod, ABC
from utils.data_types import UserId
from typing import List
from pathlib import Path


class GeneralUserDBEntry(ABC):
    def __init__(self, database_path: Path):
        self.database_path = database_path

    @abstractmethod
    def fetch_info_by_id(self, user_id: UserId) -> List[GeneralUserDBEntry]:
        raise NotImplementedError

    @abstractmethod
    def connect_to_db(self, database_path: Path):
        pass

    @abstractmethod
    def value_in_database(self, value_in_db: str):
        raise NotImplementedError
