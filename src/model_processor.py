from typing import List

from src.defect_entity import DefectEntity
from src.image_entity import ImageEntity


class ModelProcessor:
    def __init__(self):
        self.model = lambda x: x

    def process_image(self, image_entity: ImageEntity) -> List[DefectEntity]:
        prediction = self.model(image_entity)
        return []

    def retrain(self):
        pass
