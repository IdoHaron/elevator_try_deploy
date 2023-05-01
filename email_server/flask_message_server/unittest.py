from os import system, getcwd, chdir
from pathlib import Path
from email_server.flask_message_server.flask_email_server import FlaskMessageServer
from security_modules.everything_passes import EverythingPasses
from input_pipelines.dummy_input_pipeline import DummyInput
from databases.elevator_board.json.json_based import JsonElevatorBoardsTable
from databases.users_board.users_board import UsersBoard
from databases.elevator_board.json.json_based import JsonElevatorBoardsTable
from databases.template.json_template_db import JsonTemplatesDB
from pathlib import Path
from os import getcwd
from databases.screen_dbs.json.screen_db_json import ScreenJsonDB

databases = Path(getcwd()).parent.parent/"databases"
board_int = JsonElevatorBoardsTable(databases /"actual_dbs"/"ElevatorBoard.json")
# users_db = UsersBoard(Path("databases/actual_dbs/users_db.json"))

json_template_db = JsonTemplatesDB(databases/"templates"/"templates.json")
screen_db = ScreenJsonDB(path_to_db=databases/"actual_dbs"/"current_image_board.json")

FlaskMessageServer(DummyInput(), EverythingPasses(), board_int, template_db=json_template_db, screen_db=screen_db)

#TODO(Ido): should implement an elevator side test, for the fetching ETC.
