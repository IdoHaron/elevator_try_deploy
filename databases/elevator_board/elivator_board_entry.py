from utils.data_types import UserId
class ElevatorBoardEntry:
    __slots__ = ["user_id", "board_name"]
    def __init__(self, user_id:UserId, board_name:str):
        self.user_id = user_id
        self.board_name = board_name
