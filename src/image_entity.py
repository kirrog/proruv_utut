from typing import List

from src.defect_entity import DefectEntity


class ImageEntity:
    img_data: bytes
    img_id: str
    img_name: str
    img_comment: str
    img_defect_list: List[DefectEntity]

    def __init__(self,
                 img_data: bytes,
                 img_id: str,
                 img_name: str,
                 img_comment: str,
                 img_defect_list: List[DefectEntity]):
        self.img_data = img_data
        self.img_id = img_id
        self.img_name = img_name
        self.img_comment = img_comment
        self.img_defect_list = img_defect_list
