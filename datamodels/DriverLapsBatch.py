from dataclasses import dataclass
from helpers.Parsers import *
from helpers.Constants import MISSING
from datamodels.Lap import Lap

@dataclass
class DriverLapsBatch:

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