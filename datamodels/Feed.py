from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING

from datamodels.Result import Result
from datamodels.Caution import Caution
from datamodels.Leader import Leader
from datamodels.Stage import Stage

@dataclass
class Feed(Tupleable):
    raceInfo: dict
    stage4Laps: int
    results: list
    cautionSegments: list
    raceLeaders: list
    stages: list
    pitReports: list

    def __init__(self, raceSeason: int, seriesID: int, raceID: int):

        raceInfo = parseWeekendFeedURL(raceSeason, seriesID, raceID)

        if raceInfo is not MISSING:
            # Introduced for round 7 of 2020 season, then for each race thereafter starting with the last two rounds of the same year.
            self.stage4Laps = raceInfo.get("stage_4_laps", MISSING)

            self.results = buildList(Result, raceInfo.get("results", MISSING))
            self.cautionSegments = buildList(Caution, raceInfo.get("caution_segments", MISSING))
            self.raceLeaders = buildList(Leader, raceInfo.get("race_leaders", MISSING))

            # Introduced during 2020 season (will need to handle specific logic for races prior to).
            self.stages = buildList(Stage, raceInfo.get("stage_results", MISSING))

            # Introduced for round 7 of the 2020 season.
            self.pitReports = raceInfo.get("pit_reports", MISSING)

        else:
            self.stage4Laps = MISSING
            self.results = MISSING
            self.cautionSegments = MISSING
            self.raceLeaders = MISSING
            self.stages = MISSING
            self.pitReports = MISSING

    def toTuple(self) -> tuple:

        return (
            self.stage4Laps,
        )