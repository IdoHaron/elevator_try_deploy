from os import system, getcwd, chdir
from pathlib import Path
from email_server.flask_message_server.flask_email_server import FlaskMessageServer
from security_modules.everything_passes import EverythingPasses
from input_pipelines.dummy_input_pipeline import DummyInput
from databases.elevator_board.json.json_based import JsonElevatorBoardsTable
from databases.users_board.users_board import UsersBoard
from databases.users_board.json.json_based_user_db import JsonUsersBoard
from databases.elevator_board.json.json_based import JsonElevatorBoardsTable
from security_modules.verify_user_security import UserLoginSecurity
from databases.template.json_template_db import JsonTemplatesDB
from pathlib import Path
from os import environ
from os import getcwd
from databases.screen_dbs.json.screen_db_json import ScreenJsonDB
from dotenv import load_dotenv
import sys
import os

load_dotenv()
databases = Path(os.path.abspath(__file__)).parent/"databases"
print(databases)
print(f"python version: {sys.version}")

#port = 3000
#if False:
try:
    port = environ.get('PORT')
except:
    port = 8000
board_int = JsonElevatorBoardsTable(databases /"actual_dbs"/"ElevatorBoard.json")
# users_db = UsersBoard(Path("databases/actual_dbs/users_db.json"))

json_template_db = JsonTemplatesDB(databases/"actual_dbs"/"templates.json")
screen_db = ScreenJsonDB(path_to_db=databases/"actual_dbs"/"current_image_board.json")
users_db = JsonUsersBoard(databases / "actual_dbs" / "users_db.json" )
security_module = UserLoginSecurity(users_db)
security_module = EverythingPasses()


if __name__=="__main__":
    x = FlaskMessageServer(DummyInput(), security_module, board_int, template_db=json_template_db, screen_db=screen_db,
                           port=int(port), to_run=True)
else:
    x = FlaskMessageServer(DummyInput(), security_module, board_int, template_db=json_template_db, screen_db=screen_db,
                           port=int(port), to_run=False)

app = x.app

