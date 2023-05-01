from __future__ import annotations
from databases.general_user_based_db import GeneralUserDBEntry
from utils.data_types import UserId
from typing import List
from pathlib import Path
from databases.elevator_board.elivator_board_entry import ElevatorBoardEntry
from abc import abstractmethod, ABC


class ElevatorBoardsTable(GeneralUserDBEntry, ABC):
    pass