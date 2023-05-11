from databases.screen_dbs.screen.__consts import default_time_window
from typing import Tuple
from datetime import datetime
from random import choice
from utils import RandomUtils

class Image:
    current_allocated_ids = []
    def __init__(self, image_encoding:str, date_range:Tuple[datetime, datetime]= None, img_id:str=""):
        if img_id =="":
            img_id = RandomUtils.choose_number_not_in_list(min(self.current_allocated_ids)+1, max(self.current_allocated_ids), self.current_allocated_ids)
            # id = # to generate
        self.id = img_id
        self.encoding = image_encoding
        self.date_range = date_range

    def image_expired(self):
        return datetime.now() > self.date_range[1]

    def in_range(self):
        return not(self.image_expired() and self.date_range[0]<datetime.now())


    def __dict__(self):
        return {
            "encoding": self.encoding,
            "date_range": self.date_range.__dict__
        }