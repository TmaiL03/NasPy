from dataclasses import dataclass
from Helpers.Constants import MISSING

@dataclass
class StageFinisher:
    driverFullName: str
    driverID: int
    carNumber: str
    finishingPosition: int
    stagePoints: int

    def __init__(self, context: dict):
        self.driverFullName = context.get("driver_fullname", MISSING)
        self.driverID = context.get("driver_id", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.finishingPosition = context.get("finishing_position", MISSING)
        self.stagePoints = context.get("stage_points", MISSING)