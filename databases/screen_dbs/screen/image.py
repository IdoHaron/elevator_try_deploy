from databases.screen_dbs.screen.__consts import default_time_window
from typing import Tuple, Union
from datetime import datetime
from random import choice
from utils import RandomUtils
from utils.data_types import DateTime
from utils import DateTimeUtils

DateRange= Tuple[DateTime, DateTime]

class Image:
    current_allocated_ids = []
    def __init__(self, image_encoding:str, date_range:DateRange= None, image_time:int=2, img_id:Union[int,None]= None):
        if img_id is None:
            if len(self.current_allocated_ids)==0:
                img_id=0
            elif max(self.current_allocated_ids)-min(self.current_allocated_ids) >= len(self.current_allocated_ids)-1:
                img_id = max(self.current_allocated_ids) + 1
            else:
                img_id = RandomUtils.choose_number_not_in_list(min(self.current_allocated_ids)+1, max(self.current_allocated_ids), self.current_allocated_ids)
            # id = # to generate
        self.id = int(img_id)
        self.encoding = image_encoding
        self.date_range = None
        if date_range is not None:
            self.date_range = (DateTimeUtils.construct_datetime(date_range[0]), DateTimeUtils.construct_datetime(date_range[1]))
        self.image_time = int(image_time)
        self.current_allocated_ids.append(img_id)

    def image_expired(self):
        if self.date_range is None:
            return False
        return datetime.now() > self.date_range[1]

    def image_premature(self):
        return datetime.now() < self.date_range[0]

    def in_range(self):
        return not(self.image_expired() and self.date_range[0]<datetime.now())


    def __dict__(self):
        dict_to_return =  {
            "img_id": self.id,
            "image_time": self.image_time,
            "image_encoding": self.encoding
        }
        if self.date_range is not None:
            dict_to_return["date_range"] = (self.date_range[0].__dict__, self.date_range[1].__dict__)
        return dict_to_return