
from databases.screen_dbs.screen.__consts import default_time_window
from typing import Tuple, Union
from datetime import datetime
from random import choice
from utils import RandomUtils
from utils.data_types import DateTime
from typing import Dict
from databases.screen_dbs.screen.basic_input_type import BasicInputType

DateRange= Union[Tuple[DateTime, DateTime], str]

class Image(BasicInputType):
    def __init__(self, encoding:str, datetime_range:DateRange= None, presentation_time:int=2, obj_id:Union[int,None]= None):
            # id = # to generate
        super().__init__(encoding=encoding, presentation_time= presentation_time, datetime_range=datetime_range, obj_id=obj_id)
        self.image_time = int(presentation_time)


    def image_premature(self):
        if self.date_range is None:
            return False
        return datetime.now() < self.date_range[0]

    def in_range(self):
        return not(self.presentation_time_expired() and self.date_range[0] < datetime.now())


    def __dict__(self):
        dict_to_return =  super().__dict__()
        dict_to_return["class"] = self.__class__.__name__
        return dict_to_return

    def description(self):
        basic_description = super().description()
        basic_description["properties"]["image time"]= str(self.image_time*default_time_window) + " seconds"
        return basic_description

    def to_html_table_entry(self):
        html_string, image_as_dict = super().to_html_table_entry()
        html_string += f"<td>{image_as_dict['properties']['image time']}</td>"
        html_string+=f"<td>{self.on_screen_representation(500, 600)}</td>"
        html_string+="</tr>"
        return html_string

    def as_full_screen_html(self):
        return f"<img src={self.encoding} style=\"height:100%;width:100%\"> <script>timeout_fetch={default_time_window*1000};\n" \
               f"setInterval(page_reload, timeout_fetch);\n" \
               f"</script>"

    def on_screen_representation(self, width:int, height: int):
        return f"<img src={self.encoding} width=\"{width}\" height=\"{height}\">"

Image.inheriting_class[Image.__name__] = Image

