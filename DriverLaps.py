from dataclasses import dataclass
from Parsers import *
from Constants import MISSING
from Lap import Lap

@dataclass
class DriverLaps:

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