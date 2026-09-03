import datetime
from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING
from datamodels.SessionResult import SessionResult

@dataclass
class Session(Tupleable):

    weekendRunID: int
    raceID: int
    timingRunID: int
    runType: int
    runName: str
    runDate: datetime.datetime
    runDateUTC: datetime.datetime
    results: list

    def __init__(self, context: dict):

        self.weekendRunID = context.get("weekend_run_id", MISSING)
        self.raceID = context.get("race_id", MISSING)
        self.timingRunID = context.get("timing_run_id", MISSING)
        self.runType = context.get("run_type", MISSING)
        self.runName = context.get("run_name", MISSING)
        self.runDate = context.get("run_date", MISSING)
        self.runDateUTC = context.get("run_date_utc", MISSING)
        self.results = buildList(SessionResult, context.get("results", MISSING))

    def toTuple(self) -> tuple:

        return (
            self.weekendRunID,
            self.raceID,
            self.timingRunID,
            self.runType,
            self.runName,
            self.runDate,
            self.runDateUTC
        )