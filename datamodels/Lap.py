from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Constants import MISSING

@dataclass
class Lap(Tupleable):

    lapNumber: int
    lapTime: float
    lapSpeed: float
    runningPosition: int

    def __init__(self, context: dict):

        self.lapNumber = context.get("Lap", MISSING)
        self.lapTime = context.get("LapTime", MISSING)
        self.lapSpeed = context.get("LapSpeed", MISSING)
        self.runningPosition = context.get("RunningPos", MISSING)

    def toTuple(self) -> tuple:

        return (
            self.lapNumber,
            self.lapTime,
            self.lapSpeed,
            self.runningPosition
        )