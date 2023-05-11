from random import choice
from abc import ABC, abstractmethod
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
