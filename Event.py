import datetime, time
from dataclasses import dataclass
from Constants import MISSING

@dataclass
class Event:

    eventName: str
    notes: str
    startTime: datetime.datetime
    runType: int

    def __init__(self, context: dict):

        self.eventName = context.get("event_name", MISSING)
        self.notes = context.get("notes", MISSING)
        self.startTime = context.get("start_time_utc", MISSING)
        self.runType = context.get("run_type", MISSING)