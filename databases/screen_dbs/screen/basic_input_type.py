from __future__ import annotations
from utils import RandomUtils
from typing import Dict
from abc import abstractmethod, ABC
from utils import DateTimeUtils
from datetime import datetime

class BasicInputType(ABC):
    obj_map: Dict[int, BasicInputType] = {}
    inheriting_class = {
    }

    def __init__(self,encoding,datetime_range=None, obj_id=None):
        ids = list(self.obj_map.keys())
        if obj_id is None:
            if len(ids)==0:
                obj_id=0
            elif max(ids)-min(ids) >= len(ids)-1:
                obj_id = max(ids) + 1
            else:
                obj_id = RandomUtils.choose_number_not_in_list(min(ids)+1, max(ids), ids)
        self.id = int(obj_id)
        self.obj_map[self.id] = self
        self.encoding = encoding
        self.date_range = None
        if datetime_range is not None:
            if datetime_range is str:
                datetime_range = datetime_range.split("-")
            self.date_range = (DateTimeUtils.construct_datetime(datetime_range[0]), DateTimeUtils.construct_datetime(datetime_range[1]))

    @abstractmethod
    def description(self):
        dict_to_return =  {
            "properties":{
                "id": self.id,
            },
            "encoding": self.encoding
        }
        if self.date_range is not None:
            dict_to_return["datetime_range"] = (self.date_range[0].__str__(), self.date_range[1].__str__())
        return dict_to_return

    @abstractmethod
    def to_html_table_entry(self):
        image_as_dict = self.description()
        html_string = "<tr>"
        html_string += f"<td>{image_as_dict['properties']['id']}</td>"
        return html_string, image_as_dict


    def presentation_time_expried(self):
        if self.date_range is None:
            return False
        return datetime.now() > self.date_range[1]


    @staticmethod
    def factory_function(object_info:dict):
        _class = object_info["class"]
        del object_info["class"]
        destination_class =BasicInputType.inheriting_class[_class]
        return destination_class(**object_info), _class


    @abstractmethod
    def __dict__(self):
        dict_to_return=  {
            "obj_id": self.id,
            "encoding": self.encoding
        }
        if self.date_range is not None:
            dict_to_return["datetime_range"] = (self.date_range[0].__str__(), self.date_range[1].__str__())
        return dict_to_return
