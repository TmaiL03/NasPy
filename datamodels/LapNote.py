from dataclasses import dataclass
from typing import Tuple

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING

@dataclass
class LapNote(Tupleable):
    raceSeason: int
    seriesID: int
    raceID: int
    lapNumber: int
    flagState: int
    note: str
    noteID: int
    driverIDs: list

    def __init__(self, raceSeason: int, seriesID: int, raceID: int, lapNumber: int, context: dict):

        self.raceSeason = raceSeason
        self.seriesID = seriesID
        self.raceID = raceID
        self.lapNumber = lapNumber
        self.flagState = context.get("FlagState", MISSING)
        self.note = context.get("Note", MISSING)
        self.noteID = context.get("NoteID", MISSING)
        self.driverIDs = str(context.get("DriverIDs", MISSING))

    # def __init__(self, raceSeason: int, seriesID: int, raceID: int, lapNumber: int):
    #
    #     self.raceSeason = raceSeason
    #     self.seriesID = seriesID
    #     self.raceID = raceID
    #     self.lapNumber = lapNumber
    #
    #     lapData: dict = parseLapNotesURL(raceSeason, seriesID, raceID)
    #
    #     if lapData is not MISSING:
    #
    #         notes: list = lapData.get(str(lapNumber), MISSING)
    #
    #         if notes is not MISSING:
    #
    #             # Will want to implement logic to handle multiple notes for a single lap (where applicable).
    #             self.flagState = notes[0].get("FlagState", MISSING)
    #             self.note = notes[0].get("Note", MISSING)
    #             self.noteID = notes[0].get("NoteID", MISSING)
    #             self.driverIDs = notes[0].get("DriverIDs", MISSING)
    #
    #         else:
    #             self.flagState = MISSING
    #             self.note = MISSING
    #             self.noteID = MISSING
    #             self.driverIDs = MISSING
    #             print("No lap notes available for requested lap number.")

    def toTuple(self) -> Tuple:

        return (
            self.raceSeason,
            self.seriesID,
            self.raceID,
            self.lapNumber,
            self.flagState,
            self.note,
            self.noteID,
            self.driverIDs
        )