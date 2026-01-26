from dataclasses import dataclass
from helpers.Constants import MISSING

@dataclass
class SessionResult:
    runID: int
    carNumber: str
    vehicleNumber: str
    manufacturer: str
    driverID: int
    driverName: str
    finishingPosition: int
    bestLapTime: float
    bestLapSpeed: float
    bestLapNumber: int
    lapsCompleted: int
    comment: str
    deltaLeader: float
    disqualified: bool

    def __init__(self, context: dict):
        self.runID = context.get("run_id", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.vehicleNumber = context.get("vehicle_number", MISSING)
        self.manufacturer = context.get("manufacturer", MISSING)
        self.driverID = context.get("driver_id", MISSING)
        self.driverName = context.get("driver_name", MISSING)
        self.finishingPosition = context.get("finishing_position", MISSING)
        self.bestLapTime = context.get("best_lap_time", MISSING)
        self.bestLapSpeed = context.get("best_lap_speed", MISSING)
        self.bestLapNumber = context.get("best_lap_number", MISSING)
        self.lapsCompleted = context.get("laps_completed", MISSING)
        self.comment = context.get("comment", MISSING)
        self.deltaLeader = context.get("delta_leader", MISSING)
        self.disqualified = context.get("disqualified", MISSING)