from datetime import datetime
from enum import Enum
from typing import Optional

DefectType = Enum("DefectType", ["Scratch"])


class DefectEntity:
    defect_type: DefectType
    date_found: datetime

    def __init__(self, defect_type: DefectType, date_found: Optional[datetime]):
        self.defect_type = defect_type
        self.date_found = date_found if date_found else datetime.now()
