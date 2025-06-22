'''
Holds NASCAR race performance data and all associated classes and methods for accessing and parsing it.
'''

from urllib.request import urlopen
import json, datetime, time

class Race:

    def __init__(self, raceSeason: int, seriesID: int, round: int, includeExhibitions: bool = False):
        
        self._raceSeason: int = raceSeason
        self._seriesID: int = seriesID
        self._round: int = round

        # Fetching annual data from race_list_basic.json.
        url: str = f"https://cf.nascar.com/cacher/{raceSeason}/race_list_basic.json"
        response: json = urlopen(url)
        races: list = json.loads(response.read())
        seriesRaces: list = races[f"series_{seriesID}"]
        raceIndex: int = 0


        # If exhibitions are not included, find the nth occurrence in for which "race_type_id" is 1.
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

        #region Fetching and assigning initial races values.
        # Locating specific race information basic on other provided parameters.
        self._raceID: int = seriesRaces[raceIndex]["race_id"]
        self._raceName: str = seriesRaces[raceIndex]["race_name"]
        self._raceTypeID: int = seriesRaces[raceIndex]["race_type_id"]
        self._restrictorPlate: bool = seriesRaces[raceIndex]["restrictor_plate"]
        self._trackID: int = seriesRaces[raceIndex]["track_id"]
        self._trackName: str = seriesRaces[raceIndex]["track_name"]
        self._dateScheduled: datetime = seriesRaces[raceIndex]["date_scheduled"]
        self._raceDate: datetime = seriesRaces[raceIndex]["race_date"]
        self._qualifyingDate: datetime = seriesRaces[raceIndex]["qualifying_date"]
        self._tuneInDate: datetime = seriesRaces[raceIndex]["tunein_date"]
        self._scheduledDistance: float = seriesRaces[raceIndex]["scheduled_distance"]
        self._actualDistance: float = seriesRaces[raceIndex]["actual_distance"]
        self._scheduledLaps: int = seriesRaces[raceIndex]["scheduled_laps"]
        self._actualLaps: int = seriesRaces[raceIndex]["actual_laps"]
        self._stage1Laps: int = seriesRaces[raceIndex]["stage_1_laps"]
        self._stage2Laps: int = seriesRaces[raceIndex]["stage_2_laps"]
        self._stage3Laps: int = seriesRaces[raceIndex]["stage_3_laps"]
        self._carCount: int = seriesRaces[raceIndex]["number_of_cars_in_field"]
        self._poleWinnerDriverID: int = seriesRaces[raceIndex]["pole_winner_driver_id"]
        self._poleWinnerSpeed: float = seriesRaces[raceIndex]["pole_winner_speed"]
        self._numberOfLeadChanges: int = seriesRaces[raceIndex]["number_of_lead_changes"]
        self._numberOfLeaders: int = seriesRaces[raceIndex]["number_of_leaders"]
        self._numberOfCautions: int = seriesRaces[raceIndex]["number_of_cautions"]
        self._numberOfCautionLaps: int = seriesRaces[raceIndex]["number_of_caution_laps"]
        self._averageSpeed: float = seriesRaces[raceIndex]["average_speed"]
        self._totalRaceTime: time = seriesRaces[raceIndex]["total_race_time"]
        self._marginOfVictory: float = seriesRaces[raceIndex]["margin_of_victory"]
        self._racePurse: float = seriesRaces[raceIndex]["race_purse"]
        self._raceComments: str = seriesRaces[raceIndex]["race_comments"]
        self._attendance: int = seriesRaces[raceIndex]["attendance"]
        self._infractions: list = seriesRaces[raceIndex]["infractions"]
        self._schedule: list = seriesRaces[raceIndex]["schedule"]
        self._radioBroadcaster: str = seriesRaces[raceIndex]["radio_broadcaster"]
        self._tvBroadcaster: str = seriesRaces[raceIndex]["television_broadcaster"]
        self._satelliteRadioBroadcaster: str = seriesRaces[raceIndex]["satellite_radio_broadcaster"]
        self._masterRaceID: int = seriesRaces[raceIndex]["master_race_id"]
        self._inspectionComplete: bool = seriesRaces[raceIndex]["inspection_complete"]
        self._playoffRound: int = seriesRaces[raceIndex]["playoff_round"]
        self._isQualifyingRace: bool = seriesRaces[raceIndex]["is_qualifying_race"]
        self._qualifyingRaceNo: int = seriesRaces[raceIndex]["qualifying_race_no"]
        self._qualifyingRaceID: int = seriesRaces[raceIndex]["qualifying_race_id"]
        self._hasQualifying: bool = seriesRaces[raceIndex]["has_qualifying"]
        self._winnerDriverID: int = seriesRaces[raceIndex]["winner_driver_id"]
        self._poleWinnerLaptime: time = seriesRaces[raceIndex]["pole_winner_laptime"]
        # self._performance: Performance
        #endregion

    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

    #region Getter method properties for data retrieval from race_list_basic.json.

    @property
    def raceID(self) -> int:
        return self._raceID
    
    @property
    def raceName(self) -> str:
        return self._raceName
    
    @property
    def raceTypeID(self) -> int:
        return self._raceTypeID
    
    @property
    def restrictorPlate(self) -> bool:
        return self._restrictorPlate
    
    @property
    def trackID(self) -> int:
        return self._trackID
    
    @property
    def trackName(self) -> str:
        return self._trackName
    
    @property
    def dateScheduled(self) -> datetime:
        return self._dateScheduled
    
    @property
    def raceDate(self) -> datetime:
        return self._raceDate
    
    @property
    def qualifyingDate(self) -> datetime:
        return self._qualifyingDate
    
    @property
    def tuneInDate(self) -> datetime:
        return self._tuneInDate
    
    @property
    def scheduledDistance(self) -> float:
        return self._scheduledDistance
    
    @property
    def actualDistance(self) -> float:
        return self._actualDistance

    @property
    def scheduledLaps(self) -> int:
        return self._scheduledLaps
    
    @property
    def actualLaps(self) -> int:
        return self._actualLaps
    
    @property
    def stage1Laps(self) -> int:
        return self._stage1Laps
    
    @property
    def stage2Laps(self) -> int:
        return self._stage2Laps
    
    @property
    def stage3Laps(self) -> int:
        return self._stage3Laps
    
    @property
    def carCount(self) -> int:
        return self._carCount
    
    @property
    def poleWinnerDriverID(self) -> int:
        return self._poleWinnerDriverID
    
    @property
    def poleWinnerSpeed(self) -> float:
        return self._poleWinnerSpeed
    
    @property
    def numberOfLeadChanges(self) -> int:
        return self._numberOfLeadChanges
    
    @property
    def numberOfCautions(self) -> int:
        return self._numberOfCautions
    
    @property
    def numberOfCautionLaps(self) -> int:
        return self._numberOfCautionLaps
    
    @property
    def averageSpeed(self) -> float:
        return self._averageSpeed
    
    @property
    def totalRacetime(self) -> time:
        return self._totalRaceTime
    
    @property
    def marginOfVictory(self) -> float:
        return self._marginOfVictory
    
    @property
    def racePurse(self) -> float:
        return self._racePurse
    
    @property
    def raceComments(self) -> str:
        return self._raceComments
        
    @property
    def attendance(self) -> int:
        return self._attendance
    
    @property
    def infractions(self) -> list:
        return self._infractions

    @property
    def schedule(self) -> list:
        return self._schedule
    
    @property
    def radioBroadcaster(self) -> str:
        return self._radioBroadcaster
    
    @property
    def tvBroadcaster(self) -> str:
        return self._tvBroadcaster
    
    @property
    def satelliteRadioBroadcaster(self) -> str:
        return self._satelliteRadioBroadcaster
    
    @property
    def masterRaceID(self) -> int:
        return self._masterRaceID

    @property
    def inspectionComplete(self) -> bool:
        return self._inspectionComplete
    
    @property
    def playoffRound(self) -> int:
        return self._playoffRound
    
    @property
    def isQualifyingRace(self) -> bool:
        return self._isQualifyingRace
    
    @property
    def qualifyingRaceNo(self) -> int:
        return self._qualifyingRaceNo
    
    @property
    def qualifyingRaceID(self) -> int:
        return self._qualifyingRaceID
    
    @property
    def hasQualifying(self) -> bool:
        return self._hasQualifying
    
    @property
    def winnerDriverID(self) -> int:
        return self._winnerDriverID
    
    @property
    def poleWinnerLaptime(self) -> time:
        return self._poleWinnerLaptime
    
    # The following property is commented out because the Performance class has yet to be implemented.
    
    # @property
    # def performance(self):
    #     return self._performance

    #endregion

if __name__ == "__main__":

    # Test instantiation of Race object.
    race = Race(2023, 2, 1)

    print(race.raceID)
    print(race.raceName)