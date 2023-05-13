import dataclasses

from databases.screen_dbs.screen.image import Image
from typing import List
from databases.screen_dbs.screen.current_image_manager import CurrentScreenManager
class Screen:
    @dataclasses.dataclass
    class __ImageIndex:
        image_index:int
        in_image_itter_index:int

    def __init__(self, images_to_present:List[dict]):
        self.images:List[Image] = []
        for image in images_to_present:
            self.images.append(Image(**image))

        self.__current_index = Screen.__ImageIndex(0, 0)
        CurrentScreenManager.add_screen(self)

    @property
    def current_index(self)->int:
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        return self.__current_index.image_index

    def current_image(self):
        return self.images[self.current_index].encoding

    def add_image(self, image:Image):
        self.images.append(image)

    def clear_images(self):
        self.__current_index = Screen.__ImageIndex(0, 0)
        self.images = []

    def itterate(self):
        current_image = self.images[self.__current_index.image_index]
        if self.__current_index.in_image_itter_index+ 1 < current_image.image_time:
            self.__current_index.in_image_itter_index+=1
            return
        self.__current_index.image_index += 1
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        self.__current_index.in_image_itter_index = 0


    def __dict__(self):
        result = []
        for i in self.images:
            if not i.image_expired():
                result.append(i.__dict__())
        return result