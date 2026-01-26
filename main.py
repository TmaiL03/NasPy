import time

from datamodels.Caution import Caution
from datamodels.DriverLaps import DriverLaps
from datamodels.Event import Event
from datamodels.Lap import Lap
from datamodels.LapNote import LapNote
from datamodels.Leader import Leader
from datamodels.Race import Race
from datamodels.Result import Result
from datamodels.Session import Session
from datamodels.SessionResult import SessionResult
from datamodels.Stage import Stage
from datamodels.StageFinisher import StageFinisher

if __name__ == "__main__":

    # Test instantiation of Race object and nested objects.
    race: Race  = Race(2025, 1, 1)
    # print(race.raceID)

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

    # Obtaining the first DriverLaps instance given the provided race information.
    driverLaps: list = race.driverLaps

    # Obtaining the first DriverLaps instance of the list.
    specificDriverLaps: DriverLaps = driverLaps[1]

    # Obtaining the second Lap instance for the first DriverLaps instance in the list. (To avoid the null values of Lap 0).
    lap: Lap = specificDriverLaps.laps[1]

    # Obtaining the first Session instance of the provided Race instance.
    session: Session = race.sessions[0]

    # Obtaining the first SessionResult instance of the provided Session instance.
    sessionResult: SessionResult = session.results[0]
    
    # Obtaining the LapNote instance for lap 1 of the provided Race instance.
    lapNote: LapNote = LapNote(race.season, race.seriesID, race.raceID, 2)

    # Data retrieval datamodels.
    retrievalTimes: list = []
    for x in range(10):

        startTime = time.time()
        for year in range(2018, 2026):

            for round in range(36):

                # Testing data retrieval for Race objects.
                try:
                    testRace = Race(year, 1, round + 1)
                    print(f"{year} {testRace.raceName} successfully retrieved!")

                    # Testing data retrieval for PitStops objects.
                    try:
                        testPitStops = race.pitStops
                        print(f"Pit stops for {year} {testRace.raceName} successfully retrieved!")
                    
                    except Exception as ex:
                        print(f"{type(ex).__name__}: {ex.args}. Pit stops for ({year}, {round + 1}) were not retrieved.")
                    
                    try:
                        lapNote: LapNote = LapNote(year, 1, testRace.raceID, 0)
                    
                    except Exception as ex:
                        print(f"{type(ex).__name__}: {ex.args}. Lap note for ({year}, {round + 1}, 0) was not retrieved.")

                except Exception as ex:
                    print(f"{type(ex).__name__}: {ex.args}. Race ({year}, {round + 1}) was not retrieved.")

        endTime = time.time()
        print(f"Data retrieval took {endTime - startTime} seconds.")
        retrievalTimes.append(endTime - startTime)
    
    # print(retrievalTimes)

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
    # for pit in race.pitStops:
    #     print(pit.driverName)
    
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
    # print(race.pitStops[0].vehicleNumber)
    # print(race.pitStops[0].driverName)
    # print(race.pitStops[0].vehicleManufacturer)
    # print(race.pitStops[0].leaderLap)
    # print(race.pitStops[0].lapCount)
    # print(race.pitStops[0].pitInFlagStatus)
    # print(race.pitStops[0].pitOutFlagStatus)
    # print(race.pitStops[0].pitInRaceTime)
    # print(race.pitStops[0].pitOutRaceTime)
    # print(race.pitStops[0].totalDuration)
    # print(race.pitStops[0].boxStopRaceTime)
    # print(race.pitStops[0].boxLeaveRaceTime)
    # print(race.pitStops[0].pitStopDuration) 
    # print(race.pitStops[0].inTravelDuration)
    # print(race.pitStops[0].outTravelDuration)
    # print(race.pitStops[0].pitStopType)
    # print(race.pitStops[0].leftFrontTireChanged)
    # print(race.pitStops[0].leftRearTireChanged)
    # print(race.pitStops[0].rightFrontTireChanged)
    # print(race.pitStops[0].rightRearTireChanged)
    # print(race.pitStops[0].previousLapTime)
    # print(race.pitStops[0].nextLapTime)
    # print(race.pitStops[0].pitInRank)
    # print(race.pitStops[0].pitOutRank)
    # print(race.pitStops[0].positionsGainedLost)

    #endregion

    #region DriverLaps data retrieval properties.
    # print(specificDriverLaps.carNumber)
    # print(specificDriverLaps.fullName)
    # print(specificDriverLaps.manufacturer)
    # print(specificDriverLaps.runningPosition)
    # print(specificDriverLaps.driverID)

    #endregion

    #region Lap data retrieval properties.
    # print(lap.lapNumber)
    # print(lap.lapTime)
    # print(lap.lapSpeed)
    # print(lap.runningPosition)

    #endregion

    #region Session data retrieval properties.
    # print(session.weekendRunID)
    # print(session.raceID)
    # print(session.timingRunID)
    # print(session.runType)
    # print(session.runName)
    # print(session.runDate)
    # print(session.runDateUTC)

    #endregion

    #region SessionResult data retrieval properties.
    # print(sessionResult.runID)
    # print(sessionResult.carNumber)
    # print(sessionResult.vehicleNumber)
    # print(sessionResult.manufacturer)
    # print(sessionResult.driverID)
    # print(sessionResult.driverName)
    # print(sessionResult.finishingPosition)
    # print(sessionResult.bestLapTime)
    # print(sessionResult.bestLapSpeed)
    # print(sessionResult.bestLapNumber)
    # print(sessionResult.lapsCompleted)
    # print(sessionResult.comment)
    # print(sessionResult.deltaLeader)
    # print(sessionResult.disqualified)
    
    #endregion

    #region LapNote data retrieval properties.
    print(lapNote.flagState)
    print(lapNote.note)
    print(lapNote.noteID)
    print(lapNote.driverIDs)

    #endregion