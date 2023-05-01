from abc import abstractmethod
from utils.data_types.message import Message
from input_pipelines.input_pipeline import InputPipeline
from typing import List
from security_modules.security_module import SecurityModule
from flask_login import login_manager


class MessageServer:
    __slots__ = ["_message_manager", "_security_module"]
    @abstractmethod
    def __init__(self, message_manger:InputPipeline, security_module:SecurityModule):
        self._message_manager = message_manger
        self._security_module =  security_module

    @abstractmethod
    def client_fetch_new_messages(self, board_id: str, security_details:str) -> List[Message]:
        raise NotImplementedError
