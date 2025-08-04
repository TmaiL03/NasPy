'''
Holds NASCAR race performance data and all associated classes and methods for accessing and parsing it.
'''

from urllib.request import urlopen
import json, datetime, time
from dataclasses import dataclass
from typing import Type, Any
from Functions import parseWeekendFeedURL, parseLivePitDataURL

@dataclass
class Race:

    season: int
    seriesID: int
    round: int
    raceID: int
    raceName: str
    racecTypeID: int
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

    def __init__(self, season: int, seriesID: int, round: int, includeExhibitions: bool = False):
        
        _sentinel: object = object()

        self.season = season
        self.seriesID = seriesID
        self.round = round

        url: str = f"https://cf.nascar.com/cacher/{season}/race_list_basic.json"
        response: json = urlopen(url)
        races: list = json.loads(response.read())
        seriesRaces: list = races[f"series_{seriesID}"]
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

        #region Fetching and assigning initial info values.
        self.raceID = seriesRaces[raceIndex].get("race_id", _sentinel)
        self.raceName = seriesRaces[raceIndex].get("race_name", _sentinel)
        self.raceTypeID = seriesRaces[raceIndex].get("race_type_id", _sentinel)
        self.restrictorPlate = seriesRaces[raceIndex].get("restrictor_plate", _sentinel)
        self.trackID = seriesRaces[raceIndex].get("track_id", _sentinel)
        self.trackName = seriesRaces[raceIndex].get("track_name", _sentinel)
        self.dateScheduled = seriesRaces[raceIndex].get("date_scheduled", _sentinel)
        self.raceDate = seriesRaces[raceIndex].get("race_date", _sentinel)
        self.qualifyingDate = seriesRaces[raceIndex].get("qualifying_date", _sentinel)

        # Introduced during the 2021 season.
        self.tuneInDate = seriesRaces[raceIndex].get("tunein_date", _sentinel)
        
        self.scheduledDistance = seriesRaces[raceIndex].get("scheduled_distance", _sentinel)
        self.actualDistance = seriesRaces[raceIndex].get("actual_distance", _sentinel)
        self.scheduledLaps = seriesRaces[raceIndex].get("scheduled_laps", _sentinel)
        self.actualLaps = seriesRaces[raceIndex].get("actual_laps", _sentinel)
        self.stage1Laps = seriesRaces[raceIndex].get("stage_1_laps", _sentinel)
        self.stage2Laps = seriesRaces[raceIndex].get("stage_2_laps", _sentinel)
        self.stage3Laps = seriesRaces[raceIndex].get("stage_3_laps", _sentinel)
        self.carCount = seriesRaces[raceIndex].get("number_of_cars_in_field", _sentinel)
        self.poleWinnerDriverID = seriesRaces[raceIndex].get("pole_winner_driver_id", _sentinel)
        self.poleWinnerSpeed = seriesRaces[raceIndex].get("pole_winner_speed", _sentinel)
        self.numberOfLeadChanges = seriesRaces[raceIndex].get("number_of_lead_changes", _sentinel)
        self.numberOfLeaders = seriesRaces[raceIndex].get("number_of_leaders", _sentinel)
        self.numberOfCautions = seriesRaces[raceIndex].get("number_of_cautions", _sentinel)
        self.numberOfCautionLaps = seriesRaces[raceIndex].get("number_of_caution_laps", _sentinel)
        self.averageSpeed = seriesRaces[raceIndex].get("average_speed", _sentinel)
        self.totalRaceTime = seriesRaces[raceIndex].get("total_race_time", _sentinel)

        # Introduced during the 2018 season.
        self.marginOfVictory = seriesRaces[raceIndex].get("margin_of_victory", _sentinel)
        
        self.racePurse = seriesRaces[raceIndex].get("race_purse", _sentinel)
        self.raceComments = seriesRaces[raceIndex].get("race_comments", _sentinel)
        self.attendance = seriesRaces[raceIndex].get("attendance", _sentinel)

        # Introduced during the 2020 season.
        self.infractions = seriesRaces[raceIndex].get("infractions", _sentinel)
        
        # Introduced during the 2021 season.
        self.schedule = seriesRaces[raceIndex].get("schedule", _sentinel)
        
        self.radioBroadcaster = seriesRaces[raceIndex].get("radio_broadcaster", _sentinel)
        self.tvBroadcaster = seriesRaces[raceIndex].get("television_broadcaster", _sentinel)

        # Introduced during the 2022 season.
        self.satelliteRadioBroadcaster = seriesRaces[raceIndex].get("satellite_radio_broadcaster", _sentinel)
        
        self.masterRaceID = seriesRaces[raceIndex].get("master_race_id", _sentinel)
        
        # Introduced during the 2019 season.
        self.inspectionComplete = seriesRaces[raceIndex].get("inspection_complete", _sentinel)
        
        # Introduced during 2020 season.
        self.playoffRound = seriesRaces[raceIndex].get("playoff_round", _sentinel)
        
        # Introduced during the 2021 season.
        self.isQualifyingRace = seriesRaces[raceIndex].get("is_qualifying_race", _sentinel)
        
        # Introduced during the 2021 season.
        self.qualifyingRaceNo = seriesRaces[raceIndex].get("qualifying_race_no", _sentinel)
        
        # Introduced during the 2021 season.
        self.qualifyingRaceID = seriesRaces[raceIndex].get("qualifying_race_id", _sentinel)
        
        # Introduced during the 2021 season.
        self.hasQualifying = seriesRaces[raceIndex].get("has_qualifying", _sentinel)
        
        # Introduced during the 2020 season.
        self.winnerDriverID = seriesRaces[raceIndex].get("winner_driver_id", _sentinel)
        
        self.poleWinnerLaptime = seriesRaces[raceIndex].get("pole_winner_laptime", _sentinel)
        self.feed = Feed(self.season, self.seriesID, self.raceID)

        #endregion

@dataclass
class Feed:

    def __init__(self, raceSeason: int, seriesID: int, raceID: int):
        
        self._raceInfo: dict = parseWeekendFeedURL(raceSeason, seriesID, raceID)

        # Introduced for round 7 of 2020 season, then for each race thereafter starting with the last two rounds of the same year.
        try:
            self._stage4Laps: int = self._raceInfo["stage_4_laps"]
        except KeyError:
            self._stage4Laps: int = None
        
        self._results: list = self.buildList(Result, self._raceInfo["results"])
        self._cautionSegments: list = self.buildList(Caution, self._raceInfo["caution_segments"])
        self._raceLeaders: list = self.buildList(Leader, self._raceInfo["race_leaders"])

        # Introduced during 2020 season (will need to handle specific logic for races prior to).
        try:
            # Instantiation will use a list of Stage objects once implemented.
            self._stages: list = self.buildList(Stage, self._raceInfo["stage_results"])
        except KeyError:
            self._stages: list = None

        # Introduced for round 7 of the 2020 season.
        try:
            self._pitReports: list = self._raceInfo["pit_reports"]
        except KeyError:
            self._pitReports: list = None
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def stage4Laps(self) -> int:
        return self._stage4Laps

    # May adjust such that the programmer can indicate the finishing position for which data should be retrieved.
    @property
    def results(self) -> list:
        return self._results

    @property
    def cautionSegments(self) -> list:
        return self._cautionSegments
    
    @property
    def raceLeaders(self) -> list:
        return self._raceLeaders

    @property
    def stages(self) -> list:
        return self._stages

    @property
    def pitReports(self) -> list:
        return self._pitReports
    
    #endregion

    # Used for building lists of several different object types including Results, Cautions, Leaders, and Stages.
    def buildList(self, cls: Type[Any], dataDict: dict) -> list:

        objectList: list = []

        for dataObject in dataDict:
            objectList.append(cls(dataObject))
        
        return objectList

@dataclass
class Result:

    def __init__(self, context: dict):
               
        self._resultID: int = context["result_id"]
        self._finishingPos: int = context["finishing_position"]
        self._startingPos: int = context["starting_position"]
        self._carNumber: str = context["car_number"]
        self._driverFullName: str = context["driver_fullname"]
        self._driverID: int = context["driver_id"]

        # Introduced at round 20 of 2021 season.
        try:
            self._driverHometown: str = context["driver_hometown"]
        except KeyError:
            self._driverHometown: str = None
        
        self._hometownCity: str = context["hometown_city"]
        self._hometownState: str = context["hometown_state"]

        # Introduced for round 17 of the 2021 season.
        try:
            self._hometownCountry: str = context["hometown_country"]
        except KeyError:
            self._hometownCountry: str = None
        
        self._teamID: int = context["team_id"]
        self._teamName: str = context["team_name"]
        self._qualifyingOrder: int = context["qualifying_order"]
        self._qualifyingPos: int = context["qualifying_position"]
        self._qualifyingSpeed: float = context["qualifying_speed"]
        self._lapsLed: int = context["laps_led"]
        self._timesLed: int = context["times_led"]
        self._carMake: str = context["car_make"]
        self._carModel: str = context["car_model"]
        self._sponsor: str = context["sponsor"]
        self._pointsEarned: int = context["points_earned"]

        # Introduced for round 5 of the 2019 season.
        try:
            self._playoffPointsEarned: int = context["playoff_points_earned"]
        except KeyError:
            self._playoffPointsEarned: int = None

        self._lapsCompleted: int = context["laps_completed"]
        self._finishingStatus: str = context["finishing_status"]
        self._winnings: float = context["winnings"]
        self._seriesID: int = context["series_id"]
        self._raceSeason: int = context["race_season"]
        self._raceID: int = context["race_id"]
        self._ownerFullName: str = context["owner_fullname"]

        # Introduced for round 15 of the 2021 season.
        try:
            self._crewChiefID: int = context["crew_chief_id"]
        except KeyError:
            self._crewChiefID: int = None
        
        self._crewChiefFullName: str = context["crew_chief_fullname"]
        self._pointsPos: int = context["points_position"]
        self._pointsDelta: int = context["points_delta"]
        self._ownerID: int = context["owner_id"]
        self._officialCarNumber: str = context["official_car_number"]

        # Introduced during the 2020 season.
        try:
            self._disqualified: bool = context["disqualified"]
        except KeyError:
            self._disqualified: bool = None
        
        # Introduced during the 2020 season (Not for the Clash, but for the Duels).
        try:
            self._diffLaps: int = context["diff_laps"]
        except KeyError:
            self._diffLaps: int = None    
        
        # Introduced during the 2020 season (Not for the Clash, but for the Duels).
        try:
            self._diffTime: time = context["diff_time"] # Returned value in milliseconds.
        except KeyError:
            self._diffTime: time = None
        
        # Introduced for round <tbd> of the <tbd> season (need to go back to identify when this key was introduced).
        try:
            self._pitBox: int = context["pit_box"]
        except KeyError:
            self._pitBox: int = None
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def resultID(self) -> int:
        return self._resultID
    
    @property
    def finishingPos(self) -> int:
        return self._finishingPos
    
    @property
    def startingPos(self) -> int:
        return self._startingPos
    
    @property
    def carNumber(self) -> str:
        return self._carNumber
    
    @property
    def driverFullName(self) -> str:
        return self._driverFullName
    
    @property
    def driverID(self) -> int:
        return self._driverID
    
    @property
    def driverHometown(self) -> str:
        return self._driverHometown
    
    @property
    def hometownCity(self) -> str:
        return self._hometownCity
    
    @property
    def hometownState(self) -> str:
        return self._hometownState
    
    @property
    def hometownCountry(self) -> str:
        return self._hometownCountry
    
    @property
    def teamID(self) -> int:
        return self._teamID
    
    @property
    def teamName(self) -> str:
        return self._teamName
    
    @property
    def qualifyingOrder(self) -> int:
        return self._qualifyingOrder
    
    @property
    def qualifyingPos(self) -> int:
        return self._qualifyingPos
    
    @property
    def qualifyingSpeed(self) -> float:
        return self._qualifyingSpeed
    
    @property
    def lapsLed(self) -> int:
        return self._lapsLed
    
    @property
    def timesLed(self) -> int:
        return self._timesLed
    
    @property
    def carMake(self) -> str:
        return self._carMake
    
    @property
    def carModel(self) -> str:
        return self._carModel
    
    @property
    def sponsor(self) -> str:
        return self._sponsor
    
    @property
    def pointsEarned(self) -> int:
        return self._pointsEarned
    
    @property
    def playoffPointsEarned(self) -> int:
        return self._playoffPointsEarned
    
    @property
    def lapsCompleted(self) -> int:
        return self._lapsCompleted
    
    @property
    def finishingStatus(self) -> str:
        return self._finishingStatus
    
    @property
    def winnings(self) -> float:
        return self._winnings
    
    @property
    def seriesID(self) -> int:
        return self._seriesID
    
    @property
    def raceSeason(self) -> int:
        return self._raceSeason
    
    @property
    def raceID(self) -> int:
        return self._raceID
    
    @property
    def ownerFullName(self) -> str:
        return self._ownerFullName
    
    @property
    def crewChiefID(self) -> int:
        return self._crewChiefID
    
    @property
    def crewChiefFullName(self) -> str:
        return self._crewChiefFullName
    
    @property
    def pointsPos(self) -> int:
        return self._pointsPos
    
    @property
    def pointsDelta(self) -> int:
        return self._pointsDelta
    
    @property
    def ownerID(self) -> int:
        return self._ownerID
    
    @property
    def officialCarNumber(self) -> str:
        return self._officialCarNumber
    
    @property
    def disqualified(self) -> bool:
        return self._disqualified
    
    @property
    def diffLaps(self) -> int:
        return self._diffLaps
    
    @property
    def diffTime(self) -> int:
        return self._diffTime
    
    @property
    def pitBox(self) -> int:
        return self._pitBox
    
    #endregion

@dataclass
class Caution:

    def __init__(self, context: dict):

        self._raceID: int = context["race_id"]
        self._startLap: int = context["start_lap"]
        self._endLap: int = context["end_lap"]
        self._reason: str = context["reason"]
        self._comment: str = context["comment"]
        self._beneficiary: str = context["beneficiary_car_number"]
        self._flagState: int = context["flag_state"]
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def raceID(self) -> int:
        return self._raceID

    @property
    def startLap(self) -> int:
        return self._startLap
    
    @property
    def endLap(self) -> int:
        return self._endLap
    
    @property
    def reason(self) -> str:
        return self._reason
    
    @property
    def comment(self) -> str:
        return self._comment
    
    @property
    def beneficiary(self) -> str:
        return self._beneficiary
    
    @property
    def flagState(self) -> int:
        return self._flagState
    
    #endregion

@dataclass
class Leader:

    def __init__(self, context: dict):

        self._startLap: int = context["start_lap"]
        self._endLap: int = context["end_lap"]
        self._carNumber: str = context["car_number"]
        self._raceID: int = context["race_id"]
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def startLap(self) -> int:
        return self._startLap
    
    @property
    def endLap(self) -> int:
        return self._endLap
    
    @property
    def carNumber(self) -> str:
        return self._carNumber
    
    @property
    def raceID(self) -> int:
        return self._raceID

    #endregion

@dataclass
class Stage:
    
    def __init__(self, context: dict):

        self._stageNumber: int = context["stage_number"]
        self._results: list = self.buildList(StageFinisher, context["results"])
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def stageNumber(self) -> int:
        return self._stageNumber
    
    @property
    def results(self) -> list:
        return self._results
    
    #endregion

    # NOTE: The following function is a duplicate of the one from Feed, both could be abstracted into parent class.
    # Used for building lists of several different object types including Results, Cautions, and Leaders.
    def buildList(self, cls: Type[Any], dataDict: dict) -> list:

        objectList: list = []

        for dataObject in dataDict:
            objectList.append(cls(dataObject))
        
        return objectList

@dataclass
class StageFinisher:

    def __init__(self, context: dict):

        self._driverFullName: str = context["driver_fullname"]
        self._driverID: int = context["driver_id"]
        self._carNumber: str = context["car_number"]
        self._finishingPos: int = context["finishing_position"]
        self._stagePts: int = context["stage_points"]
    
    #region Getter method properties for data retrieval from weekend-feed.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def driverFullName(self) -> str:
        return self._driverFullName
    
    @property
    def driverID(self) -> int:
        return self._driverID
    
    @property
    def carNumber(self) -> str:
        return self._carNumber
    
    @property
    def finishingPos(self) -> int:
        return self._finishingPos
    
    @property
    def stagePts(self) -> int:
        return self._stagePts

    #endregion

class PitStops:

    def __init__(self, seriesID: int, raceID: int):

        self._pitStops: list = self.buildList(PitStop, parseLivePitDataURL(seriesID, raceID))
    
    #region Getter method properties for data retrieval from live-pit-data.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def pitStops(self) -> list:
        return self._pitStops
    
    # NOTE: The following function is a duplicate of the one from Feed + Stage, both could be abstracted into parent class.
    # Used for building lists of several different object types including Results, Cautions, and Leaders.
    def buildList(self, cls: Type[Any], dataList: list) -> list:

        objectList: list = []

        for dataObject in dataList:
            objectList.append(cls(dataObject))
        
        return objectList

@dataclass
class PitStop:

    def __init__(self, context: dict):
        
        self._vehicleNumber: str = context["vehicle_number"]
        self._driverName: str = context["driver_name"]
        self._vehicleManufacturer: str = context["vehicle_manufacturer"]
        self._leaderLap: int = context["leader_lap"]
        self._lapCount: int = context["lap_count"]
        self._pitInFlagStatus: int = context["pit_in_flag_status"]
        self._pitOutFlagStatus: int = context["pit_out_flag_status"]
        self._pitInRaceTime: float = context["pit_in_race_time"]
        self._pitOutRaceTime: float = context["pit_out_race_time"]
        self._totalDuration: float = context["total_duration"]
        self._boxStopRaceTime: float = context["box_stop_race_time"]
        self._boxLeaveRaceTime: float = context["box_leave_race_time"]
        self._pitStopDuration: float = context["pit_stop_duration"]
        self._inTravelDuration: float = context["in_travel_duration"]
        self._outTravelDuration: float = context["out_travel_duration"]
        self._pitStopType: str = context["pit_stop_type"]
        self._leftFrontTireChanged: bool = context["left_front_tire_changed"]
        self._leftRearTireChanged: bool = context["left_rear_tire_changed"]
        self._rightFrontTireChanged: bool = context["right_front_tire_changed"]
        self._rightRearTireChanged: bool = context["right_rear_tire_changed"]
        self._previousLapTime: float = context["previous_lap_time"]
        self._nextLapTime: float = context["next_lap_time"]
        self._pitInRank: int = context["pit_in_rank"]
        self._pitOutRank: int = context["pit_out_rank"]
        self._positions_gained_lost: int = context["positions_gained_lost"]
    
    #region Getter method properties for data retrieval from live-pit-data.json.
    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    @property
    def vehicleNumber(self) -> str:
        return self._vehicleNumber
    
    @property
    def driverName(self) -> str:
        return self._driverName
    
    @property
    def vehicleManufacturer(self) -> str:
        return self._vehicleManufacturer
    
    @property
    def leaderLap(self) -> int:
        return self._leaderLap
    
    @property
    def lapCount(self) -> int:
        return self._lapCount
    
    @property
    def pitInFlagStatus(self) -> int:
        return self._pitInFlagStatus
    
    @property
    def pitOutFlagStatus(self) -> int:
        return self._pitOutFlagStatus
    
    @property
    def pitInRaceTime(self) -> float:
        return self._pitInRaceTime
    
    @property
    def pitOutRaceTime(self) -> float:
        return self._pitOutRaceTime
    
    @property
    def totalDuration(self) -> float:
        return self._totalDuration
    
    @property
    def boxStopRaceTime(self) -> float:
        return self._boxStopRaceTime
    
    @property
    def boxLeaveRaceTime(self) -> float:
        return self._boxLeaveRaceTime
    
    @property
    def pitStopDuration(self) -> float:
        return self._pitStopDuration
    
    @property
    def inTravelDuration(self) -> float:
        return self._inTravelDuration
    
    @property
    def outTravelDuration(self) -> float:
        return self._outTravelDuration
    
    @property
    def pitStopType(self) -> str:
        return self._pitStopType
    
    @property
    def leftFrontTireChanged(self) -> bool:
        return self._leftFrontTireChanged
    
    @property
    def leftRearTireChanged(self) -> bool:
        return self._leftRearTireChanged
    
    @property
    def rightFrontTireChanged(self) -> bool:
        return self._rightFrontTireChanged
    
    @property
    def rightRearTireChanged(self) -> bool:
        return self._rightRearTireChanged
    
    @property
    def previousLapTime(self) -> float:
        return self._previousLapTime
    
    @property
    def nextLapTime(self) -> float:
        return self._nextLapTime
    
    @property
    def pitInRank(self) -> int:
        return self._pitInRank
    
    @property
    def pitOutRank(self) -> int:
        return self._pitOutRank
    
    @property
    def positionsGainedLost(self) -> int:
        return self._positions_gained_lost
    
    #endregion


if __name__ == "__main__":

    # Test instantiation of Race object and nested objects.
    race = Race(2025, 1, 1)

    # Obtaining first place information from the provided Race instance.
    result: Result = race.feed.results[0]

    # Obtaining first caution segment of the provided Race instance.
    caution: Caution = race.feed.cautionSegments[0]

    # Obtaining the first leader of the provided Race instance.
    leader: Leader = race.feed.raceLeaders[0]

    # Obtaining the first stage of the provided Race instance.
    stage: Stage = race.feed.stages[0]

    # Obtaining the stage winner of the provided Stage instance.
    stageFinisher: StageFinisher = stage.results[0]

    # Obtaining the pit stops for the provided Race instance (May integrate pit stop data into Race object directly).
    stops: PitStops = PitStops(race.seriesID, race.raceID)

    # Data retrieval test.
    startTime = time.time()
    for year in range(2017, 2026):

        for round in range(36):

            # Testing data retrieval for Race objects.
            try:
                testRace = Race(year, 1, round + 1)
                print(f"{year} {testRace.raceName} successfully retrieved!")

                # Testing data retrieval for PitStops objects.
                try:
                    testPitStops = PitStops(testRace.seriesID, testRace.raceID)
                    print(f"Pit stops for {year} {testRace.raceName} successfully retrieved!")
                
                except Exception as ex:
                    print(f"{type(ex).__name__}: {ex.args}. Pit stops for ({year}, {round + 1}) were not retrieved.")

            except Exception as ex:
                print(f"{type(ex).__name__}: {ex.args}. Race ({year}, {round + 1}) was not retrieved.")

    endTime = time.time()
    print(f"Data retrieval took {endTime - startTime} seconds.")

    #region Race data retrieval properties.
    # print(race.season)
    # print(race.round)
    # print(race.seriesID)
    # print(race.raceID)
    # print(race.raceName)
    # print(race.raceTypeID)
    # print(race.restrictorPlate)
    # print(race.trackID)
    # print(race.trackName)
    # print(race.dateScheduled)
    # print(race.raceDate)
    # print(race.qualifyingDate)
    # print(race.tuneInDate)
    # print(race.scheduledDistance)
    # print(race.actualDistance)
    # print(race.scheduledLaps)
    # print(race.actualLaps)
    # print(race.stage1Laps)
    # print(race.stage2Laps)
    # print(race.stage3Laps)
    # print(race.carCount)
    # print(race.poleWinnerDriverID)
    # print(race.poleWinnerSpeed)
    # print(race.numberOfLeadChanges)
    # print(race.numberOfLeaders)
    # print(race.numberOfCautions)
    # print(race.numberOfCautionLaps)
    # print(race.averageSpeed)
    # print(race.totalRaceTime)
    # print(race.marginOfVictory)
    # print(race.racePurse)
    # print(race.raceComments)
    # print(race.attendance)
    # print(race.infractions)
    # print(race.schedule)
    # print(race.radioBroadcaster)
    # print(race.tvBroadcaster)
    # print(race.satelliteRadioBroadcaster)
    # print(race.masterRaceID)
    # print(race.inspectionComplete)
    # print(race.playoffRound)
    # print(race.isQualifyingRace)
    # print(race.qualifyingRaceNo)
    # print(race.qualifyingRaceID)
    # print(race.hasQualifying)
    # print(race.winnerDriverID)
    # print(race.poleWinnerLaptime)
    
    #endregion

    #region Feed data retrieval properties.
    # print(race.feed.stage4Laps)
    # print(race.feed.results)
    # print(race.feed.cautionSegments)
    # print(race.feed.raceLeaders)
    # print(race.feed.stageResults)
    # print(race.feed.pitReports)

    #endregion

    #region Result data retrieval properties.
    # print(result.resultID)
    # print(result.finishingPos)
    # print(result.startingPos)
    # print(result.carNumber)
    # print(result.driverFullName)
    # print(result.driverID)
    # print(result.driverHometown)
    # print(result.hometownCity)
    # print(result.hometownState)
    # print(result.hometownCountry)
    # print(result.teamID)
    # print(result.teamName)
    # print(result.qualifyingOrder)
    # print(result.qualifyingPos)
    # print(result.qualifyingSpeed)
    # print(result.lapsLed)
    # print(result.timesLed)
    # print(result.carMake)
    # print(result.carModel)
    # print(result.sponsor)
    # print(result.pointsEarned)
    # print(result.playoffPointsEarned)
    # print(result.lapsCompleted)
    # print(result.finishingStatus)
    # print(result.winnings)
    # print(result.seriesID)
    # print(result.raceSeason)
    # print(result.raceID)
    # print(result.ownerFullName)
    # print(result.crewChiefID)
    # print(result.crewChiefFullName)
    # print(result.pointsPos)
    # print(result.pointsDelta)
    # print(result.ownerID)
    # print(result.officialCarNumber)
    # print(result.disqualified)
    # print(result.diffLaps)
    # print(result.diffTime)
    # print(result.pitBox)

    #endregion

    #region Caution data retrieval properties.
    # print(caution.raceID)
    # print(caution.startLap)
    # print(caution.endLap)
    # print(caution.reason)
    # print(caution.comment)
    # print(caution.beneficiary)
    # print(caution.flagState)

    #endregion

    #region Leader data retrieval properties.
    # print(leader.startLap)
    # print(leader.endLap)
    # print(leader.carNumber)
    # print(leader.raceID)

    #endregion

    #region Stage data retrieval properties.
    # print(stage.stageNumber)
    # for driver in stage.results:
    #     print(driver.driverFullName)
    
    #endregion

    #region StageFinisher data retrieval properties.
    # print(stageFinisher.driverFullName)
    # print(stageFinisher.driverID)
    # print(stageFinisher.carNumber)
    # print(stageFinisher.finishingPos)
    # print(stageFinisher.stagePts)

    #endregion

    #region PitStop data retrival properties.
    # print(stops.pitStops[0].vehicleNumber)
    # print(stops.pitStops[0].driverName)
    # print(stops.pitStops[0].vehicleManufacturer)
    # print(stops.pitStops[0].leaderLap)
    # print(stops.pitStops[0].lapCount)
    # print(stops.pitStops[0].pitInFlagStatus)
    # print(stops.pitStops[0].pitOutFlagStatus)
    # print(stops.pitStops[0].pitInRaceTime)
    # print(stops.pitStops[0].pitOutRaceTime)
    # print(stops.pitStops[0].totalDuration)
    # print(stops.pitStops[0].boxStopRaceTime)
    # print(stops.pitStops[0].boxLeaveRaceTime)
    # print(stops.pitStops[0].pitStopDuration) 
    # print(stops.pitStops[0].inTravelDuration)
    # print(stops.pitStops[0].outTravelDuration)
    # print(stops.pitStops[0].pitStopType)
    # print(stops.pitStops[0].leftFrontTireChanged)
    # print(stops.pitStops[0].leftRearTireChanged)
    # print(stops.pitStops[0].rightFrontTireChanged)
    # print(stops.pitStops[0].rightRearTireChanged)
    # print(stops.pitStops[0].previousLapTime)
    # print(stops.pitStops[0].nextLapTime)
    # print(stops.pitStops[0].pitInRank)
    # print(stops.pitStops[0].pitOutRank)
    # print(stops.pitStops[0].positionsGainedLost)

    #endregion