from __future__ import annotations


#TODO(Ido): learn how to minimaize outside exposure of modules __all__
from email_server.message_server import MessageServer
from server.flask_server.flask_server import FlaskServer
from flask import render_template, request, redirect
from input_pipelines.input_pipeline import InputPipeline
from utils.decorators import singleton
from security_modules.security_module import SecurityModule
from json import loads
from flask_login import LoginManager, login_user, login_required,current_user
from pathlib import Path
from importlib import reload
from databases.elevator_board.elevator_boards_table import ElevatorBoardsTable
from server.utils import string_to_select_entry, start_select_entry, end_select_entry
from databases.template.templates_db import TemplatesDB
from base64 import b64encode
from databases.screen_dbs.screen_db import ScreenDB

#TODO(ido): should figure-out how 

# @singleton
class FlaskMessageServer(FlaskServer, MessageServer):
    server_instace:FlaskMessageServer = None
    board_select_name = "board"

    def __init__(self, message_manager: InputPipeline, security_module: SecurityModule,
                 user_to_screen_db_class: ElevatorBoardsTable,
                 template_db:TemplatesDB,
                 screen_db:ScreenDB,
                 wanted_module_name: str = __name__,
                 host: str = "127.0.0.1", port: int = 80):
        FlaskServer.__init__(self, wanted_module_name=wanted_module_name, path_to_templates=Path("website_pages"))
        MessageServer.__init__(self, message_manager, security_module)
        self.user_to_screen_db_class = user_to_screen_db_class
        self.login_manager = LoginManager()
        self._screen_db = screen_db
        self._template_db = template_db
        FlaskMessageServer.server_instace = self
        FlaskServer._SERVER.run(host=host, port=port, debug=True)# ,ssl_context='adhoc')
        #reload(FlaskMessageServer)
        #self.login_manager.init_app(self._SERVER)


    @staticmethod
    @FlaskServer._SERVER.route("/fetch_messages/<board_id>/<security_details>")
    def client_fetch_new_messages(board_id: str, security_details: str) -> str:
        #TODO(ido): move security details from 
        if not FlaskMessageServer.server_instace._security_module.fetch_and_verify_user(board_id, security_details):
            return ''
        print("here")
        return FlaskMessageServer.server_instace._message_manager.get_new_messages(board_id)

    def get_app(self):
        return FlaskServer._SERVER

    @staticmethod
    @FlaskServer._SERVER.route("/")
    def load_login_page():
        return render_template("login_page.html")

    @staticmethod
    @FlaskServer._SERVER.route("/login", methods=["POST"])
    def login_details():
        #TODO(Ido): think about uniting with the basic index route.
        username, password = request.form["username"], request.form["password"]
        is_login_legal, user_object= FlaskMessageServer.server_instace._security_module.fetch_and_verify_user(username, password)
        print(f"login is: {is_login_legal} legal")
        next = request.args.get('next')
        if is_login_legal:
            login_user(user_object)
            print(f"and the user object is with: {user_object.is_authenticated()} authentication value")
        #TODO(ido): add check for url safe for  redirection
            return redirect(next or "/message_form_window")
        return redirect(next or  "/")

    @staticmethod
    @FlaskServer._LOGIN_MANAGER.user_loader
    def load_user(user_id):
        return FlaskMessageServer.server_instace._security_module.connected_client(user_id)

    
    @staticmethod
    @FlaskServer._SERVER.route("/message_form_window")
    def message_form_window():
        #TODO(Ido): might be worth to unite with the post location
        #TODO(Ido): read about serving with images, think about how to make the templates dynamic so other templates could be showed.
        print(current_user)
        connected_user_id = current_user.get_id()
        server_instance = FlaskMessageServer.server_instace
        boards= server_instance.user_to_screen_db_class.fetch_info_by_id(connected_user_id)
        constructed__boards_string = start_select_entry(server_instance.board_select_name)
        for board in boards:
            constructed__boards_string += string_to_select_entry(board.board_name)
        constructed__boards_string+= end_select_entry()
        print(constructed__boards_string)
        return render_template("message_form.html", boards=[board.board_name for board in boards],
                               templates=FlaskMessageServer.server_instace._template_db.get_all_templates()
                               )

    @staticmethod
    @FlaskServer._SERVER.route("/new_image", methods=["POST"])
    @login_required
    def new_image():
        data = loads(request.data.decode("ASCII"))
        FlaskMessageServer.server_instace._screen_db.modify_screen(data["destination"],data["image"])
        return ""
        # board_name, image_in_code = request.form["board_name"], request.form["image"]


    @staticmethod
    @FlaskServer._SERVER.route("/template/<template>")
    @login_required
    def template_fetch(template:str):
        print(template)
        return FlaskMessageServer.server_instace._template_db.get_encoding(template)

    @staticmethod
    @FlaskServer._SERVER.route("/elevator/<elevator_id>")
    def fetch_image_for_elevator(elevator_id:str):
        if  FlaskMessageServer.server_instace._screen_db.legal_screen_id(elevator_id):
            return render_template("elevator_client.html", screen_id=elevator_id,
                                   current_img=FlaskMessageServer.server_instace._screen_db.get_image(elevator_id))
        return "sorry, page not found"