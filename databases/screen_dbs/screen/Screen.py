from databases.screen_dbs.screen.__image import Image
from typing import List
class Screen:
    def __init__(self, images_to_present:List[dict]):
        self.images:List[Image] = []
        for image in images_to_present:
            self.images.append(Image(**image))
        self.__current_index= 0

    @property
    def current_index(self):
        self.__current_index = self.__current_index % len(self.images)
        return self.__current_index

    def current_image(self):
        return self.images[self.current_index]

    def add_image(self, image_structure:dict):
        self.images.append(Image(**image_structure))

    def clear_images(self):
        self.__current_index = 0
        self.images = []


    def __dict__(self):
        result = []
        for i in self.images:
            if not i.image_expired():
                result.append(i.__dict__())
        return result