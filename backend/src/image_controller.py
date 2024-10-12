from typing import List

from backend.src.db_controller import DBController
from backend.src.image_entity import ImageEntity
from backend.src.model_processor import ModelProcessor


class ImageController:
    image_collection: List[ImageEntity]
    db_controller: DBController
    model_processor: ModelProcessor

    def __init__(self, db_controller: DBController, model_processor:ModelProcessor):
        self.image_collection = []
        self.db_controller = db_controller
        self.model_processor = model_processor

    def get_image_list(self):
        pass

    def add_image(self, image_data):
        pass

    def process_img(self, img_id):
        pass

    def dump_results(self):
        pass

    def get_image(self, image_id):
        pass

    def add_bounding_box(self, img_id, bounding_boxes):
        pass

    def update_bounding_box(self, img_id, bounding_boxes):
        pass
