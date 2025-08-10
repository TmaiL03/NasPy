'''
Holds NASCAR race performance data and all associated classes and methods for accessing and parsing it.
'''

from urllib.request import urlopen
import json, datetime, time
from dataclasses import dataclass
from Parsers import parseWeekendFeedURL, parseLivePitDataURL, buildList
from Constants import MISSING

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

        #endregion

@dataclass
class Feed:

    raceInfo: dict
    stage4Laps: int
    results: list
    cautionSegments: list
    raceLeaders: list
    stages: list
    pitReports: list

    def __init__(self, raceSeason: int, seriesID: int, raceID: int):
        
        self.raceInfo = parseWeekendFeedURL(raceSeason, seriesID, raceID)

        # Introduced for round 7 of 2020 season, then for each race thereafter starting with the last two rounds of the same year.
        self.stage4Laps = self.raceInfo.get("stage_4_laps", MISSING)
        
        self.results = buildList(Result, self.raceInfo.get("results", MISSING))
        self.cautionSegments = buildList(Caution, self.raceInfo.get("caution_segments", MISSING))
        self.raceLeaders = buildList(Leader, self.raceInfo.get("race_leaders", MISSING))

        # Introduced during 2020 season (will need to handle specific logic for races prior to).
        self.stages = buildList(Stage, self.raceInfo.get("stage_results", MISSING))

        # Introduced for round 7 of the 2020 season.
        self.pitReports = self.raceInfo.get("pit_reports", MISSING)

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

@dataclass
class Result:

    resultID: int
    finishingPosition: int
    startingPosition: int
    carNumber: str
    driverFullname: str
    driverID: int
    driverHometown: str
    hometownCity: str
    hometownState: str
    hometownCountry: str
    teamID: int
    teamName: str
    qualifyingOrder: int
    qualifyingPosition: int
    qualifyingSpeed: float
    lapsLed: int
    timesLed: int
    carMake: str
    carModel: str
    sponsor: str
    pointsEarned: int
    playoffPointsEarned: int
    lapsCompleted: int
    finishingStatus: str
    winnings: float
    seriesID: int
    raceSeason: int
    raceID: int
    ownerFullname: str
    crewChiefID: int
    crewChiefFullname: str
    pointsPosition: int
    pointsDelta: int
    ownerID: int
    officialCarNumber: str
    disqualified: bool
    diffLaps: int
    diffTime: int
    pitBox: int

    def __init__(self, context: dict):

        self.resultID = context.get("result_id", MISSING)
        self.finishingPosition = context.get("finishing_position", MISSING)
        self.startingPosition = context.get("starting_position", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.driverFullName = context.get("driver_fullname", MISSING)
        self.driverID = context.get("driver_id", MISSING)

        # Introduced at round 20 of 2021 season.
        self.driverHometown = context.get("driver_hometown", MISSING)
        
        self.hometownCity = context.get("hometown_city", MISSING)
        self.hometownState = context.get("hometown_state", MISSING)

        # Introduced for round 17 of the 2021 season.
        self.hometownCountry = context.get("hometown_country", MISSING)
        
        self.teamID = context.get("team_id", MISSING)
        self.teamName = context.get("team_name", MISSING)
        self.qualifyingOrder = context.get("qualifying_order", MISSING)
        self.qualifyingPosition = context.get("qualifying_position", MISSING)
        self.qualifyingSpeed = context.get("qualifying_speed", MISSING)
        self.lapsLed = context.get("laps_led", MISSING)
        self.timesLed = context.get("times_led", MISSING)
        self.carMake = context.get("car_make", MISSING)
        self.carModel = context.get("car_model", MISSING)
        self.sponsor = context.get("sponsor", MISSING)
        self.pointsEarned = context.get("points_earned", MISSING)

        # Introduced for round 5 of the 2019 season.
        self.playoffPointsEarned = context.get("playoff_points_earned", MISSING)

        self.lapsCompleted = context.get("laps_completed", MISSING)
        self.finishingStatus = context.get("finishing_status", MISSING)
        self.winnings = context.get("winnings", MISSING)
        self.seriesID = context.get("series_id", MISSING)
        self.raceSeason = context.get("race_season", MISSING)
        self.raceID = context.get("race_id", MISSING)
        self.ownerFullName = context.get("owner_fullname", MISSING)

        # Introduced for round 15 of the 2021 season.
        self.crewChiefID = context.get("crew_chief_id", MISSING)
        
        self.crewChiefFullName = context.get("crew_chief_fullname", MISSING)
        self.pointsPosition = context.get("points_position", MISSING)
        self.pointsDelta = context.get("points_delta", MISSING)
        self.ownerID = context.get("owner_id", MISSING)
        self.officialCarNumber = context.get("official_car_number", MISSING)

        # Introduced during the 2020 season.
        self.disqualified = context.get("disqualified", MISSING)
        
        # Introduced during the 2020 season (Not for the Clash, but for the Duels).
        self.diffTime = context.get("diff_time", MISSING) # Returned value in milliseconds.
        
        # Introduced for round <tbd> of the <tbd> season (need to go back to identify when this key was introduced).
        self.pitBox = context.get("pit_box", MISSING)

@dataclass
class Caution:

    raceID: int
    startLap: int
    endLap: int
    reason: str
    comment: str
    beneficiary: str
    flagState: int

    def __init__(self, context: dict):

        self.raceID = context.get("race_id", MISSING)
        self.startLap = context.get("start_lap", MISSING)
        self.endLap = context.get("end_lap", MISSING)
        self.reason = context.get("reason", MISSING)
        self.comment = context.get("comment", MISSING)
        self.beneficiary = context.get("beneficiary_car_number", MISSING)
        self.flagState = context.get("flag_state", MISSING)

@dataclass
class Leader:

    startLap: int
    endLap: int
    carNumber: str
    raceID: int

    def __init__(self, context: dict):

        self.startLap = context.get("start_lap", MISSING)
        self.endLap = context.get("end_lap", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.raceID = context.get("race_id", MISSING)

@dataclass
class Stage:

    stageNumber: int
    results: list
    
    def __init__(self, context: dict):

        self.stageNumber = context.get("stage_number", MISSING)
        self.results = buildList(StageFinisher, context.get("results", MISSING))

@dataclass
class StageFinisher:

    driverFullName: str
    driverID: int
    carNumber: str
    finishingPosition: int
    stagePoints: int
    
    def __init__(self, context: dict):
        
        self.driverFullName = context.get("driver_fullname", MISSING)
        self.driverID = context.get("driver_id", MISSING)
        self.carNumber = context.get("car_number", MISSING)
        self.finishingPosition = context.get("finishing_position", MISSING)
        self.stagePoints = context.get("stage_points", MISSING)

class PitStops:

    pitStops: list

    def __init__(self, seriesID: int, raceID: int):

        self.pitStops = buildList(PitStop, parseLivePitDataURL(seriesID, raceID))

@dataclass
class PitStop:

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

if __name__ == "__main__":

    # Test instantiation of Race object and nested objects.
    race = Race(2025, 1, 1)
    print(race.raceID)

    # Obtaining first place information from the provided Race instance.
    result: Result = race.feed.results[0]

    # Obtaining first event of the provided Race Instance.
    event: Event = race.schedule[0]

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
    retrievalTimes: list = []
    for x in range(10):

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
        retrievalTimes.append(endTime - startTime)
    
    print(retrievalTimes)


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
    # print(race.feed.stages)
    # print(race.feed.pitReports)

    #endregion

    #region Event data retrieval properties.
    # print(event.eventName)
    # print(event.notes)
    # print(event.startTime)
    # print(event.runType)

    #endregion

    #region Result data retrieval properties.
    # print(result.resultID)
    # print(result.finishingPosition)
    # print(result.startingPosition)
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
    # print(result.qualifyingPosition)
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
    # print(result.pointsPosition)
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
    # print(stageFinisher.finishingPosition)
    # print(stageFinisher.stagePoints)

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