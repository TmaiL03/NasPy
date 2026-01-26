from dataclasses import dataclass
from Constants import MISSING

@dataclass
class Caution:

    raceID: int
    startLap: int
    endLap: int
    reason: str
    comment: str
    beneficiary: str
    flagState: int

    def __init__(self, context: dict):

        self.raceID = context.get("race_id", MISSING)
        self.startLap = context.get("start_lap", MISSING)
        self.endLap = context.get("end_lap", MISSING)
        self.reason = context.get("reason", MISSING)
        self.comment = context.get("comment", MISSING)
        self.beneficiary = context.get("beneficiary_car_number", MISSING)
        self.flagState = context.get("flag_state", MISSING)