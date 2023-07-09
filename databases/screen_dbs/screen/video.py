from utils import DateTimeUtils
from exceptions.definition_errors import InsufficientInformation
from databases.screen_dbs.screen.basic_input_type import BasicInputType
from databases.screen_dbs.screen.__consts import default_time_window
from math import ceil
class Video(BasicInputType):
    def __init__(self, encoding, datetime_range, video_duration=None, presentation_time=None, destination=None, obj_id=None):
        if video_duration is None:
            presentation_time = presentation_time
        else:
            presentation_time = int(ceil(float(presentation_time)) / default_time_window)
        if presentation_time is None:
            raise InsufficientInformation
        _datetime_range = None
        if datetime_range is not None and "datetime_range" in datetime_range:
            _datetime_range= datetime_range
        super().__init__(encoding=encoding, presentation_time=presentation_time, datetime_range=_datetime_range, obj_id=obj_id)


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

    def as_full_screen_html(self):
        return f"<video id=\"v_id_{self.id}\" src={self.encoding} style=\"height:100%;width:100%\">" \
                     f"<source src=\"/{self.encoding}\" type=\"video/mp4\"> Your browser does not support the video tag." \
                     f"</video></td>" \
                     f"<script>" \
                     f"\nconst video_element = document.getElementById('v_id_{self.id}');\n" \
                     f"video_element.load();\n video_element.play();\n" \
                     f"</script>"

Video.inheriting_class[Video.__name__] = Video
