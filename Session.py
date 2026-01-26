import datetime
from dataclasses import dataclass
from Parsers import *
from Constants import MISSING
from SessionResult import SessionResult

@dataclass
class Session:

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