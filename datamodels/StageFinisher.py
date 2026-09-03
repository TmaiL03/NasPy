from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Constants import MISSING

@dataclass
class StageFinisher(Tupleable):
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

    def toTuple(self) -> tuple:
        return (
            self.driverFullName,
            self.driverID,
            self.carNumber,
            self.finishingPosition,
            self.stagePoints
        )