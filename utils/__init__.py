from random import choice
from abc import ABC, abstractmethod
from utils.data_types import DateTime
from datetime import datetime
from exceptions.type_errors import TypeNotFound
class RandomUtils:
    @staticmethod
    @abstractmethod
    def choose_randomly_from_list(input_list:list):
        return choice(input_list)

    @staticmethod
    def choose_number_not_in_list(min:int, max:int, not_in_list:list):
        # does not support very large numbers)
        all_possible = set(range(min+1, max)) - set(not_in_list)
        return RandomUtils.choose_randomly_from_list(list(all_possible))

class DateTimeUtils(ABC):
    time_as_string = "%Y-%m-%d %H:%M:%S"
    @staticmethod
    @abstractmethod
    def construct_datetime(time:DateTime):
        if type(time) is str:
            return datetime.strptime(time, DateTimeUtils.time_as_string)
        elif type(time) is datetime:
            return time
        elif type(time) is dict:
            time = convert_string_to_int(time)
            print(time)
            return datetime(**time)
        raise TypeNotFound

def convert_string_to_int(dict_time)->dict:
    for key in dict_time.keys():
        dict_time[key] = int(dict_time[key])
    return dict_time