import datetime, time
from dataclasses import dataclass
from typing import Tuple

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING
from datamodels.Feed import Feed
from datamodels.Event import Event
from datamodels.PitStop import PitStop
from datamodels.DriverLaps import DriverLaps
from datamodels.Session import Session

@dataclass
class Race(Tupleable):
    season: int
    seriesID: int
    round: int
    raceID: int
    raceName: str
    raceTypeID: int
    restrictorPlate: bool
    trackID: int
    trackName: str
    dateScheduled: datetime.datetime
    raceDate: datetime.datetime
    qualifyingDate: datetime.datetime
    tuneInDate: datetime.datetime
    scheduledDistance: float
    actualDistance: float
    scheduledLaps: int
    actualLaps: int
    stage1Laps: int
    stage2Laps: int
    stage3Laps: int
    carCount: int
    poleWinnerDriverID: int
    poleWinnerSpeed: float
    numberOfLeadChanges: int
    numberOfLeaders: int
    numberOfCautions: int
    numberOfCautionLaps: int
    averageSpeed: float
    totalRaceTime: time.struct_time
    marginOfVictory: float
    racePurse: float
    raceComments: str
    attendance: int
    infractions: list
    schedule: list
    radioBroadcaster: str
    tvBroadcaster: str
    satelliteRadioBroadcaster: str
    masterRaceID: int
    inspectionComplete: bool
    playoffRound: int
    isQualifyingRace: bool
    qualifyingRaceNo: int
    qualifyingRaceID: int
    hasQualifying: bool
    winnerDriverID: int
    poleWinnerLaptime: time.struct_time
    feed: "Feed"
    pitStops: list
    driverLaps: list
    sessions: list

    def __init__(self, season: int, seriesID: int, round: int, includeExhibitions: bool = False):

        self.season = season
        self.seriesID = seriesID
        self.round = round

        seriesRaces: list = parseRaceListBasicURL(season, seriesID)
        raceIndex: int = 0

        # If exhibitions are not included, find the nth race for which "race_type_id" is 1.
        if not includeExhibitions:

            pointsRaceCounter: int = 0

            for race in seriesRaces:

                if race["race_type_id"] == 1:
                    pointsRaceCounter += 1
                else:
                    pass

                if pointsRaceCounter == round:
                    raceIndex = seriesRaces.index(race)
                    break
        else:
            raceIndex = round - 1

        # region Fetching and assigning initial info values.
        self.raceID = seriesRaces[raceIndex].get("race_id", MISSING)
        self.raceName = seriesRaces[raceIndex].get("race_name", MISSING)
        self.raceTypeID = seriesRaces[raceIndex].get("race_type_id", MISSING)
        self.restrictorPlate = seriesRaces[raceIndex].get("restrictor_plate", MISSING)
        self.trackID = seriesRaces[raceIndex].get("track_id", MISSING)
        self.trackName = seriesRaces[raceIndex].get("track_name", MISSING)
        self.dateScheduled = seriesRaces[raceIndex].get("date_scheduled", MISSING)
        self.raceDate = seriesRaces[raceIndex].get("race_date", MISSING)
        self.qualifyingDate = seriesRaces[raceIndex].get("qualifying_date", MISSING)

        # Introduced during the 2021 season.
        self.tuneInDate = seriesRaces[raceIndex].get("tunein_date", MISSING)

        self.scheduledDistance = seriesRaces[raceIndex].get("scheduled_distance", MISSING)
        self.actualDistance = seriesRaces[raceIndex].get("actual_distance", MISSING)
        self.scheduledLaps = seriesRaces[raceIndex].get("scheduled_laps", MISSING)
        self.actualLaps = seriesRaces[raceIndex].get("actual_laps", MISSING)
        self.stage1Laps = seriesRaces[raceIndex].get("stage_1_laps", MISSING)
        self.stage2Laps = seriesRaces[raceIndex].get("stage_2_laps", MISSING)
        self.stage3Laps = seriesRaces[raceIndex].get("stage_3_laps", MISSING)
        self.carCount = seriesRaces[raceIndex].get("number_of_cars_in_field", MISSING)
        self.poleWinnerDriverID = seriesRaces[raceIndex].get("pole_winner_driver_id", MISSING)
        self.poleWinnerSpeed = seriesRaces[raceIndex].get("pole_winner_speed", MISSING)
        self.numberOfLeadChanges = seriesRaces[raceIndex].get("number_of_lead_changes", MISSING)
        self.numberOfLeaders = seriesRaces[raceIndex].get("number_of_leaders", MISSING)
        self.numberOfCautions = seriesRaces[raceIndex].get("number_of_cautions", MISSING)
        self.numberOfCautionLaps = seriesRaces[raceIndex].get("number_of_caution_laps", MISSING)
        self.averageSpeed = seriesRaces[raceIndex].get("average_speed", MISSING)
        self.totalRaceTime = seriesRaces[raceIndex].get("total_race_time", MISSING)

        # Introduced during the 2018 season.
        self.marginOfVictory = seriesRaces[raceIndex].get("margin_of_victory", MISSING)

        self.racePurse = seriesRaces[raceIndex].get("race_purse", MISSING)
        self.raceComments = seriesRaces[raceIndex].get("race_comments", MISSING)
        self.attendance = seriesRaces[raceIndex].get("attendance", MISSING)

        # Introduced during the 2020 season.
        self.infractions = seriesRaces[raceIndex].get("infractions", MISSING)

        # Introduced during the 2021 season.
        self.schedule = buildList(Event, seriesRaces[raceIndex].get("schedule", MISSING))

        self.radioBroadcaster = seriesRaces[raceIndex].get("radio_broadcaster", MISSING)
        self.tvBroadcaster = seriesRaces[raceIndex].get("television_broadcaster", MISSING)

        # Introduced during the 2022 season.
        self.satelliteRadioBroadcaster = seriesRaces[raceIndex].get("satellite_radio_broadcaster", MISSING)

        self.masterRaceID = seriesRaces[raceIndex].get("master_race_id", MISSING)

        # Introduced during the 2019 season.
        self.inspectionComplete = seriesRaces[raceIndex].get("inspection_complete", MISSING)

        # Introduced during 2020 season.
        self.playoffRound = seriesRaces[raceIndex].get("playoff_round", MISSING)

        # Introduced during the 2021 season.
        self.isQualifyingRace = seriesRaces[raceIndex].get("is_qualifying_race", MISSING)

        # Introduced during the 2021 season.
        self.qualifyingRaceNo = seriesRaces[raceIndex].get("qualifying_race_no", MISSING)

        # Introduced during the 2021 season.
        self.qualifyingRaceID = seriesRaces[raceIndex].get("qualifying_race_id", MISSING)

        # Introduced during the 2021 season.
        self.hasQualifying = seriesRaces[raceIndex].get("has_qualifying", MISSING)

        # Introduced during the 2020 season.
        self.winnerDriverID = seriesRaces[raceIndex].get("winner_driver_id", MISSING)

        self.poleWinnerLaptime = seriesRaces[raceIndex].get("pole_winner_laptime", MISSING)
        self.feed = Feed(self.season, self.seriesID, self.raceID)
        self.pitStops = buildList(PitStop, parseLivePitDataURL(self.seriesID, self.raceID))
        self.driverLaps = buildList(DriverLaps, parseLapTimesURL(self.season, self.seriesID, self.raceID))
        self.sessions = buildList(Session, parseWeekendFeedURL(self.season, self.seriesID, self.raceID, "weekend_runs"))

        # endregion

    def toTuple(self) -> Tuple:
        return (self.season,
                self.seriesID,
                self.round,
                self.raceID,
                self.raceName,
                self.raceTypeID,
                self.restrictorPlate,
                self.trackID,
                self.trackName,
                self.dateScheduled,
                self.raceDate,
                self.qualifyingDate,
                self.tuneInDate,
                self.scheduledDistance,
                self.actualDistance,
                self.scheduledLaps,
                self.actualLaps,
                self.stage1Laps,
                self.stage2Laps,
                self.stage3Laps,
                self.carCount,
                self.poleWinnerDriverID,
                self.poleWinnerSpeed,
                self.numberOfLeadChanges,
                self.numberOfLeaders,
                self.numberOfCautions,
                self.numberOfCautionLaps,
                self.averageSpeed,
                self.totalRaceTime,
                self.marginOfVictory,
                self.racePurse,
                self.raceComments,
                self.attendance,
                str(self.infractions),
                self.radioBroadcaster,
                self.tvBroadcaster,
                self.satelliteRadioBroadcaster,
                self.masterRaceID,
                self.inspectionComplete,
                self.playoffRound,
                self.isQualifyingRace,
                self.qualifyingRaceNo,
                self.qualifyingRaceID,
                self.hasQualifying,
                self.winnerDriverID,
                self.poleWinnerLaptime)