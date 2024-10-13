import json
from typing import List

from src.db_controller import DBController
from src.defect_entity import DefectEntity, DefectType
from src.image_entity import ImageEntity
from src.model_processor import ModelProcessor


class ImageController:
    image_collection: List[ImageEntity]
    db_controller: DBController
    model_processor: ModelProcessor

    def __init__(self, db_controller: DBController, model_processor: ModelProcessor):
        self.image_collection = []
        self.db_controller = db_controller
        self.model_processor = model_processor

    def get_image_list(self) -> List[str]:
        return self.db_controller.get_image_list()

    def add_image(self, img_data, image_data):
        img_id = image_data["img_id"]
        img_name = image_data["img_name"]
        img_comment = image_data["img_comment"]
        img_defect_list = json.loads(image_data["img_defect_list"])
        for img_defect in img_defect_list:
            img_defect_type = img_defect["defect_type"]
            img_defect_datetime = img_defect["datetime"]
            DefectEntity(DefectType(img_defect_type), img_defect_datetime)
        new_entity = ImageEntity(img_data,
                                 img_id,
                                 img_name,
                                 img_comment,
                                 img_defect_list)
        self.image_collection.append(new_entity)
        self.db_controller.dump_image(new_entity)
        return img_id

    def process_img(self, img_id):
        pass

    def dump_results(self):
        pass

    def get_image(self, image_id) -> ImageEntity:
        return self.db_controller.get_image(image_id)

    def add_bounding_box(self, img_id, bounding_boxes):
        pass

    def update_bounding_box(self, img_id, bounding_boxes):
        pass
