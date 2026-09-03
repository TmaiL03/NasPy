import datetime
from dataclasses import dataclass
from typing import Tuple

from datamodels.Tupleable import Tupleable
from helpers.Constants import MISSING

@dataclass
class Event(Tupleable):

    eventName: str
    notes: str
    startTime: datetime.datetime
    runType: int

    def __init__(self, context: dict):

        self.eventName = context.get("event_name", MISSING)
        self.notes = context.get("notes", MISSING)
        self.startTime = context.get("start_time_utc", MISSING)
        self.runType = context.get("run_type", MISSING)

    def toTuple(self) -> Tuple:

        return (
            self.eventName,
            self.notes,
            self.startTime,
            self.runType
        )