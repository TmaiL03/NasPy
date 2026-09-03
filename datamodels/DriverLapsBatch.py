from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING
from datamodels.Lap import Lap

@dataclass
class DriverLapsBatch(Tupleable):

    carNumber: str
    fullName: str
    manufacturer: str
    runningPosition: int
    driverID: int
    laps: list

    def __init__(self, context: dict):

        self.carNumber = context.get("Number", MISSING)
        self.fullName = context.get("FullName", MISSING)
        self.manufacturer = context.get("Manufacturer", MISSING)
        self.runningPosition = context.get("RunningPos", MISSING)
        self.driverID = context.get("NASCARDriverID", MISSING)
        self.laps = buildList(Lap, context.get("Laps", MISSING))

    def toTuple(self) -> tuple:

        return (
            self.carNumber,
            self.fullName,
            self.manufacturer,
            self.runningPosition,
            self.driverID
        )