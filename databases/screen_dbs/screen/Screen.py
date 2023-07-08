
from databases.screen_dbs.screen.image import Image
from typing import Dict, List
from databases.screen_dbs.screen.current_image_manager import CurrentScreenManager
from databases.screen_dbs.screen.basic_input_type import BasicInputType
from databases.screen_dbs.screen.video import Video
class Screen:

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
        self.__current_index = 0
        CurrentScreenManager.add_screen(self)


    def __current_obj(self):
        return list(self.all_obj.values())[self.__current_index]

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
        self.__current_index = 0
        self.images = {}

    def tick(self):
        if self.__current_obj().tick():
            self.__current_index += 1
            self.__current_index = self.__current_index % len(self.images)

    def __dict__(self):
        result = []
        for i in self.all_obj.values():
            if not i.presentation_time_expired():
                result.append(i.__dict__())
        return result

    def flush(self):
        self.clear_images()
