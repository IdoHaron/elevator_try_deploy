from __future__ import annotations

from databases.screen_dbs.screen.__consts import default_time_window
from typing import Tuple, Union
from datetime import datetime
from random import choice
from utils import RandomUtils
from utils.data_types import DateTime
from utils import DateTimeUtils
from typing import Dict

DateRange= Union[Tuple[DateTime, DateTime], str]

class Image:
    images_map:Dict[int, Image] = {}
    def __init__(self, image_encoding:str, datetime_range:DateRange= None, image_time:int=2, img_id:Union[int,None]= None):
        ids = list(self.images_map.keys())
        if img_id is None:
            if len(ids)==0:
                img_id=0
            elif max(ids)-min(ids) >= len(ids)-1:
                img_id = max(ids) + 1
            else:
                img_id = RandomUtils.choose_number_not_in_list(min(ids)+1, max(ids), ids)
            # id = # to generate
        self.id = int(img_id)
        self.images_map[self.id] = self
        self.encoding = image_encoding
        self.date_range = None
        if datetime_range is not None:
            if datetime_range is str:
                datetime_range = datetime_range.split("-")
            self.date_range = (DateTimeUtils.construct_datetime(datetime_range[0]), DateTimeUtils.construct_datetime(datetime_range[1]))
        self.image_time = int(image_time)

    def image_expired(self):
        if self.date_range is None:
            return False
        return datetime.now() > self.date_range[1]

    def image_premature(self):
        if self.date_range is None:
            return False
        return datetime.now() < self.date_range[0]

    def in_range(self):
        return not(self.image_expired() and self.date_range[0]<datetime.now())


    def __dict__(self):
        dict_to_return =  {
            "image_properties":{
                "img_id": self.id,
                "image_time": self.image_time
            },
            "image_encoding": self.encoding
        }
        if self.date_range is not None:
            dict_to_return["datetime_range"] = (self.date_range[0].__str__(), self.date_range[1].__str__())
        return dict_to_return