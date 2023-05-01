from databases.screen_dbs.screen_db import ScreenDB
from pathlib import Path
from utils.decorators import singleton
from json import load
from databases.json_db import JsonDB

@singleton
class ScreenJsonDB(ScreenDB,JsonDB):
    def __init__(self, path_to_db):
        super().__init__(path_to_db)

    def _load_db(self, path_current_db_state:Path):
        with path_current_db_state.open("r") as f:
            x = load(f)
        return x

    def modify_screen(self, screen_id, image:str):
        # need to verify screen exists.
        self._modified_screen(screen_id)
        self._current_db_state[screen_id] = image

    def __dict__(self):
        return self._current_db_state.copy()