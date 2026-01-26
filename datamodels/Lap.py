from dataclasses import dataclass
from helpers.Constants import MISSING

@dataclass
class Lap:

    lapNumber: int
    lapTime: float
    lapSpeed: float
    runningPosition: int

    def __init__(self, context: dict):

        self.lapNumber = context.get("Lap", MISSING)
        self.lapTime = context.get("LapTime", MISSING)
        self.lapSpeed = context.get("LapSpeed", MISSING)
        self.runningPosition = context.get("RunningPos", MISSING)