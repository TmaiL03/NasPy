from dataclasses import dataclass
from Constants import MISSING

@dataclass
class Leader:

    startLap: int
    endLap: int
    carNumber: str
    raceID: int

    def __init__(self, context: dict):

        self.startLap = context.get("start_lap", MISSING)
        self.endLap = context.get("end_lap", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.raceID = context.get("race_id", MISSING)