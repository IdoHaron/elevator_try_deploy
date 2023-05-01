from databases.data_map import MapDB
from pathlib import Path
class CurrentImagesElevator(MapDB):
    def __init__(self, path_to_db:Path):
        super().__init__(path_to_db)


    def __dict__(self) -> dict:
        pass