from abc import ABC, abstractmethod
from typing import List
from databases.screen_dbs.screen.__consts import default_time_window
from time import sleep
from threading import Thread
class CurrentScreenManager(ABC):
    current_screens:List[object] = []

    @staticmethod
    @abstractmethod
    def add_screen(screen_to_add: object):
        CurrentScreenManager.current_screens.append(screen_to_add)

    @staticmethod
    def __itterate():
        for screen in CurrentScreenManager.current_screens:
            screen.tick()

    @staticmethod
    def timer_function():
        while True:
            sleep(default_time_window)
            CurrentScreenManager.__itterate()



Thread(target=CurrentScreenManager.timer_function).start()