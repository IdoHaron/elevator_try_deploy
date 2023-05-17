import dataclasses

from databases.screen_dbs.screen.image import Image
from typing import Dict, List
from databases.screen_dbs.screen.current_image_manager import CurrentScreenManager
class Screen:
    @dataclasses.dataclass
    class __ImageIndex:
        image_index:int
        in_image_itter_index:int

    def __init__(self, images_to_present:List[dict]):
        self.images:Dict[int, Image] = {}
        for image in images_to_present:
            new_img = Image(**image)
            self.images[new_img.id] = new_img

        self.__current_index = Screen.__ImageIndex(0, 0)
        CurrentScreenManager.add_screen(self)

    @property
    def current_index(self)->int:
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        return self.__current_index.image_index

    def __current_image(self):
        return list(self.images.values())[self.current_index]

    def current_image_encoding(self):
        """
        visual current image
        :return:
        """
        return self.__current_image().encoding

    def remove_image(self, image_id:int):
        del self.images[image_id]

    def add_image(self, image:Image):
        self.images[image.id] = image

    def clear_images(self):
        self.__current_index = Screen.__ImageIndex(0, 0)
        self.images = []

    def itterate(self):
        self.__inc()
        if self.__current_image().image_expired():
            current_image_id = self.__current_image().id
            self.remove_image(current_image_id)
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        if not self.__current_image().image_premature():
            return
        self.__current_index.image_index += 1
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        self.__current_index.in_image_itter_index = 0

    def __inc(self):
        current_image = self.__current_image()
        if self.__current_index.in_image_itter_index + 1 < current_image.image_time:
            self.__current_index.in_image_itter_index += 1
            return
        self.__current_index.image_index += 1
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        self.__current_index.in_image_itter_index = 0


    def __dict__(self):
        result = []
        for i in self.images.values():
            if not i.image_expired():
                result.append(i.__dict__())
        return result

    def flush(self):
        self.clear_images()
