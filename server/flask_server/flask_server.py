from flask import Flask
from server.server_interface import Server
from server.utils import ServerState
from pathlib import Path
from importlib import reload
from flask_login import LoginManager
from random import choices
from string import ascii_uppercase, ascii_lowercase, digits


class FlaskServer(Server):
    _SERVER: Flask = Flask(__name__, template_folder="../../website_pages", static_folder="../../static")
    length_of_secret_key = 8
    _LOGIN_MANAGER = LoginManager()
    _SERVER.secret_key = ''.join(choices(ascii_uppercase + digits+ ascii_lowercase, k=length_of_secret_key))
    _LOGIN_MANAGER.init_app(_SERVER)
    def __init__(self, wanted_module_name: str = __name__, path_to_templates: Path = ""):
        self.wanted_module_name = wanted_module_name
        self.server_state = ServerState.DOWN
        self.path_to_templates = path_to_templates
        # self.server_up()

    def start_server(self):
        return self.server_up()

    def server_up(self):
        if self.server_state is ServerState.UP:
            return
        if self.path_to_templates == "":
            FlaskServer._SERVER = Flask(self.wanted_module_name)
        else:
            print(self.path_to_templates.__str__())
            FlaskServer._SERVER = Flask(self.wanted_module_name, template_folder=self.path_to_templates.__str__())
        self.server_state = ServerState.UP

        # should figure out if there is a way to start the server purely from python

    def server_sleep(self):
        if self.server_state is ServerState.SLEEP:
            return
        self.server_state = ServerState.SLEEP

    def server_down(self):
        if self.server_state is ServerState.DOWN:
            return
        self.server_state = ServerState.DOWN

    def change_server_state(self, wanted_server_state: ServerState):
        if wanted_server_state is ServerState.UP:
            return self.start_server()
        if wanted_server_state is ServerState.SLEEP and wanted_server_state is ServerState.DOWN:
            self.start_server()
            return self.server_sleep()
        if wanted_server_state is ServerState.SLEEP:
            return self.server_sleep()
        if wanted_server_state is ServerState.DOWN:
            return self.server_down()

    @property
    def sever_state(self) -> ServerState:
        return self.server_state
