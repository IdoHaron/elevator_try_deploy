from databases.screen_dbs.screen.__consts import default_time_window
from typing import Tuple
from datetime import datetime
from random import choice
from utils import RandomUtils

class Image:
    current_allocated_ids = []
    def __init__(self, image_encoding:str, date_range:Tuple[datetime, datetime]= None, image_time:int=2, img_id:str=""):
        if img_id =="":
            if len(self.current_allocated_ids)==0:
                img_id=0
            elif max(self.current_allocated_ids)-min(self.current_allocated_ids) >= len(self.current_allocated_ids)-1:
                img_id = max(self.current_allocated_ids) + 1
            else:
                img_id = RandomUtils.choose_number_not_in_list(min(self.current_allocated_ids)+1, max(self.current_allocated_ids), self.current_allocated_ids)
            # id = # to generate
        self.id = img_id
        self.encoding = image_encoding
        self.date_range = date_range
        self.image_time = image_time
        self.current_allocated_ids.append(img_id)

    def image_expired(self):
        return datetime.now() > self.date_range[1]

    def in_range(self):
        return not(self.image_expired() and self.date_range[0]<datetime.now())


    def __dict__(self):
        return {
            "encoding": self.encoding,
            "date_range": self.date_range.__dict__
        }