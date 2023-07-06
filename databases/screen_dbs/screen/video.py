from utils import DateTimeUtils
from databases.screen_dbs.screen.basic_input_type import BasicInputType
from databases.screen_dbs.screen.__consts import default_time_window
class Video(BasicInputType):
    def __init__(self, encoding, datetime_range, video_time, destination=None, obj_id=None):
        _datetime_range = None
        if datetime_range is not None and "datetime_range" in datetime_range:
            _datetime_range= datetime_range
        super().__init__(encoding=encoding,datetime_range=_datetime_range, obj_id=obj_id)
        self.video_time = int(int(video_time) / default_time_window)


    def description(self):
        return super().description()

    def to_html_table_entry(self):
        html_string, video_as_dict = super().to_html_table_entry()
        html_string += f"<td>not applicable</td>"
        html_string+=f"<td><video id=\"v_id_{video_as_dict['properties']['id']}\" src={video_as_dict['encoding']} width=\"500\" height=\"600\">" \
                     f"<source src=\"/{video_as_dict['encoding']}\" type=\"video/mp4\"> Your browser does not support the video tag." \
                     f"</video></td>" \
                     f"<script>" \
                     f"\nconst video_element = document.getElementById('v_id_{video_as_dict['properties']['id']}');\n" \
                     f"video_element.load();\n video_element.play();\n" \
                     f"</script>"
                     #"video_element.addEventListener('ended', function() { video_element.play(); });" \
        html_string+="</tr>"
        return html_string


    def __dict__(self):
        dict_to_return = super().__dict__()
        dict_to_return["video_time"] = self.video_time
        dict_to_return["class"] = self.__class__.__name__
        return dict_to_return

Video.inheriting_class[Video.__name__] = Video
