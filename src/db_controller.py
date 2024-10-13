import pickle
from typing import List

from redis import Redis

from src.image_entity import ImageEntity


class DBController:
    def __init__(self, redis_controller: Redis):
        self.controller = redis_controller

    def get_image_list(self) -> List[str]:
        keys_list = []
        scan_res = self.controller.scan_iter()
        for key_str in scan_res:
            keys_list.append(str(key_str))
        return keys_list

    def get_image(self, image_id: str):
        image_data = self.controller.get(image_id)
        unpickled_data = pickle.loads(image_data)
        return unpickled_data

    def dump_image(self, image: ImageEntity):
        pickled_image = pickle.dumps(image)
        self.controller.set(image.img_id, pickled_image)
