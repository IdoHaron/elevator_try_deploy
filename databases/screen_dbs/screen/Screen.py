import dataclasses

from databases.screen_dbs.screen.image import Image
from typing import Dict, List
from databases.screen_dbs.screen.current_image_manager import CurrentScreenManager
from databases.screen_dbs.screen.basic_input_type import BasicInputType
from databases.screen_dbs.screen.video import Video
class Screen:
    @dataclasses.dataclass
    class __ImageIndex:
        image_index:int
        in_image_itter_index:int

    def __init__(self, images_to_present:List[dict]):
        self.images:Dict[int, Image] = {}
        self.videos:Dict[int, Video] = {}
        self.all_obj:Dict[int, BasicInputType] = {}
        for generic_video_img in images_to_present:
            new_obj, _type = BasicInputType.factory_function(generic_video_img)
            if _type=="Image":
                self.images[new_obj.id] = new_obj
            if _type=="Video":
                self.videos[new_obj.id]= new_obj
            self.all_obj[new_obj.id] = new_obj
        self.__current_index = Screen.__ImageIndex(0, 0)
        CurrentScreenManager.add_screen(self)

    @property
    def current_index(self)->int:
        self.__current_index.image_index = self.__current_index.image_index % len(self.all_obj)
        return self.__current_index.image_index

    def __current_obj(self):
        return list(self.all_obj.values())[self.current_index]

    def current_image_encoding(self):
        """
        visual current image
        :return:
        """
        return self.__current_obj().encoding

    def remove_object(self, object_id:int):
        try:
            object_id = int(object_id)
            self.all_obj.pop(object_id)
        except:
            print(f"{self.all_obj.keys()}  {object_id}")
            self.all_obj[object_id] = None
            print(f"{self.all_obj.keys()}  {object_id}")


    def add_image(self, image:Image):
        self.images[image.id] = image

    def clear_images(self):
        self.__current_index = Screen.__ImageIndex(0, 0)
        self.images = {}

    def itterate(self):
        self.__inc()
        if self.__current_obj().presentation_time_expried():
            current_image_id = self.__current_obj().id
            self.remove_object(current_image_id)
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        if not self.__current_obj().presentation_time_expried():
            return
        self.__current_index.image_index += 1
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        self.__current_index.in_image_itter_index = 0

    def __inc(self):
        current_image = self.__current_obj()

        if current_image is not None and self.__current_index.in_image_itter_index + 1 < current_image.image_time:
            self.__current_index.in_image_itter_index += 1
            return
        self.__current_index.image_index += 1
        self.__current_index.image_index = self.__current_index.image_index % len(self.images)
        self.__current_index.in_image_itter_index = 0


    def __dict__(self):
        result = []
        for i in self.all_obj.values():
            if not i.presentation_time_expried():
                result.append(i.__dict__())
        return result

    def flush(self):
        self.clear_images()
