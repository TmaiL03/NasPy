from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Constants import MISSING

@dataclass
class PitStop(Tupleable):
    vehicleNumber: str
    driverName: str
    vehicleManufacturer: str
    leaderLap: int
    lapCount: int
    pitInFlagStatus: int
    pitOutFlagStatus: int
    pitInRaceTime: float
    pitOutRaceTime: float
    totalDuration: float
    boxStopRaceTime: float
    boxLeaveRaceTime: float
    pitStopDuration: float
    inTravelDuration: float
    outTravelDuration: float
    pitStopType: str
    leftFrontTireChanged: bool
    leftRearTireChanged: bool
    rightFrontTireChanged: bool
    rightRearTireChanged: bool
    previousLapTime: float
    nextLapTime: float
    pitInRank: int
    pitOutRank: int
    positionsGainedLost: int

    def __init__(self, context: dict):
        self.vehicleNumber = context.get("vehicle_number", MISSING)
        self.driverName = context.get("driver_name", MISSING)
        self.vehicleManufacturer = context.get("vehicle_manufacturer", MISSING)
        self.leaderLap = context.get("leader_lap", MISSING)
        self.lapCount = context.get("lap_count", MISSING)
        self.pitInFlagStatus = context.get("pit_in_flag_status", MISSING)
        self.pitOutFlagStatus = context.get("pit_out_flag_status", MISSING)
        self.pitInRaceTime = context.get("pit_in_race_time", MISSING)
        self.pitOutRaceTime = context.get("pit_out_race_time", MISSING)
        self.totalDuration = context.get("total_duration", MISSING)
        self.boxStopRaceTime = context.get("box_stop_race_time", MISSING)
        self.boxLeaveRaceTime = context.get("box_leave_race_time", MISSING)
        self.pitStopDuration = context.get("pit_stop_duration", MISSING)
        self.inTravelDuration = context.get("in_travel_duration", MISSING)
        self.outTravelDuration = context.get("out_travel_duration", MISSING)
        self.pitStopType = context.get("pit_stop_type", MISSING)
        self.leftFrontTireChanged = context.get("left_front_tire_changed", MISSING)
        self.leftRearTireChanged = context.get("left_rear_tire_changed", MISSING)
        self.rightFrontTireChanged = context.get("right_front_tire_changed", MISSING)
        self.rightRearTireChanged = context.get("right_rear_tire_changed", MISSING)
        self.previousLapTime = context.get("previous_lap_time", MISSING)
        self.nextLapTime = context.get("next_lap_time", MISSING)
        self.pitInRank = context.get("pit_in_rank", MISSING)
        self.pitOutRank = context.get("pit_out_rank", MISSING)
        self.positionsGainedLost = context.get("positions_gained_lost", MISSING)

    def toTuple(self) -> tuple:

        return (
            self.vehicleNumber,
            self.driverName,
            self.vehicleManufacturer,
            self.leaderLap,
            self.lapCount,
            self.pitInFlagStatus,
            self.pitOutFlagStatus,
            self.pitInRaceTime,
            self.pitOutRaceTime,
            self.totalDuration,
            self.boxStopRaceTime,
            self.boxLeaveRaceTime,
            self.pitStopDuration,
            self.inTravelDuration,
            self.outTravelDuration,
            self.pitStopType,
            self.leftFrontTireChanged,
            self.leftRearTireChanged,
            self.rightFrontTireChanged,
            self.rightRearTireChanged,
            self.previousLapTime,
            self.nextLapTime,
            self.pitInRank,
            self.pitOutRank,
            self.positionsGainedLost
        )