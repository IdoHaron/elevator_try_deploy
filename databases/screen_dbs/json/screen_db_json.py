import json

from databases.screen_dbs.screen_db import ScreenDB
from pathlib import Path
from utils.decorators import singleton
from json import load
from databases.json_db import JsonDB
from databases.screen_dbs.screen.Screen import Screen
from databases.screen_dbs.screen.image import Image

@singleton
class ScreenJsonDB(ScreenDB,JsonDB):
    def __init__(self, path_to_db):
        super().__init__(path_to_db)

    def _load_db(self, path_current_db_state:Path):
        database_state = {}
        with path_current_db_state.open("r") as f:
            x = load(f)
        for screen in x.keys():
            database_state[screen] = Screen(x[screen])
        return database_state

    def add_image_to_screen(self, screen_id, image:Image):
        # need to verify screen exists.
        self._modified_screen(screen_id)
        self._current_db_state[screen_id].add_image(image)
        self._save_db()

    def __dict__(self):
        dict_to_return = {}
        for screen in self._current_db_state.keys():
            dict_to_return[screen] = self._current_db_state[screen].__dict__()
        return dict_to_return

    def remove_image(self, screen_id:str, image_id:int):
        self._current_db_state[screen_id].remove_image(image_id)
    def _save_db(self):
        with self.database_path.open("w") as f:
            json.dump(self.__dict__(), f)

    def flush_screen(self, screen_id:str):
        self._current_db_state[screen_id].flush()