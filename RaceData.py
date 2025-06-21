'''
Holds NASCAR race performance data and all associated classes and methods for accessing and parsing it.
'''

from urllib.request import urlopen
import json, datetime, time

class Race:

    def __init__(self, raceSeason: int, seriesID: int, round: int):
        
        self._raceSeason: int = raceSeason
        self._seriesID: int = seriesID
        self._round: int = round

        # Fetching annual data from race_list_basic.json.
        url: str = f"https://cf.nascar.com/cacher/{raceSeason}/race_list_basic.json"
        response: json = urlopen(url)
        data: dict = json.loads(response.read())
        
        # Locating specific race information basic on other provided parameters.
        self._raceID: int = data[f"series_{seriesID}"][round - 1]["race_id"]
        self._raceName: str = data[f"series_{seriesID}"][round - 1]["race_name"]
        self._raceTypeID: int = data[f"series_{seriesID}"][round - 1]["race_type_id"]
        self._restrictorPlate: bool = data[f"series_{seriesID}"][round - 1]["restrictor_plate"]
        self._trackID: int = data[f"series_{seriesID}"][round - 1]["track_id"]
        self._trackName: str = data[f"series_{seriesID}"][round - 1]["track_name"]
        self._dateScheduled: datetime = data[f"series_{seriesID}"][round - 1]["date_scheduled"]
        self._raceDate: datetime = data[f"series_{seriesID}"][round - 1]["race_date"]
        self._qualifyingDate: datetime = data[f"series_{seriesID}"][round - 1]["qualifying_date"]
        self._tuneInDate: datetime = data[f"series_{seriesID}"][round - 1]["tunein_date"]
        self._scheduledDistance: float = data[f"series_{seriesID}"][round - 1]["scheduled_distance"]
        self._actualDistance: float = data[f"series_{seriesID}"][round - 1]["actual_distance"]
        self._scheduledLaps: int = data[f"series_{seriesID}"][round - 1]["scheduled_laps"]
        self._actualLaps: int = data[f"series_{seriesID}"][round - 1]["actual_laps"]
        self._stage1Laps: int = data[f"series_{seriesID}"][round - 1]["stage_1_laps"]
        self._stage2Laps: int = data[f"series_{seriesID}"][round - 1]["stage_2_laps"]
        self._stage3Laps: int = data[f"series_{seriesID}"][round - 1]["stage_3_laps"]
        self._carCount: int = data[f"series_{seriesID}"][round - 1]["number_of_cars_in_field"]
        self._poleWinnerDriverID: int = data[f"series_{seriesID}"][round - 1]["pole_winner_driver_id"]
        self._poleWinnerSpeed: float = data[f"series_{seriesID}"][round - 1]["pole_winner_speed"]
        self._numberOfLeadChanges: int = data[f"series_{seriesID}"][round - 1]["number_of_lead_changes"]
        self._numberOfLeaders: int = data[f"series_{seriesID}"][round - 1]["number_of_leaders"]
        self._numberOfCautions: int = data[f"series_{seriesID}"][round - 1]["number_of_cautions"]
        self._numberOfCautionLaps: int = data[f"series_{seriesID}"][round - 1]["number_of_caution_laps"]
        self._averageSpeed: float = data[f"series_{seriesID}"][round - 1]["average_speed"]
        self._totalRaceTime: time = data[f"series_{seriesID}"][round - 1]["total_race_time"]
        self._marginOfVictory: float = data[f"series_{seriesID}"][round - 1]["margin_of_victory"]
        self._racePurse: float = data[f"series_{seriesID}"][round - 1]["race_purse"]
        self._raceComments: str = data[f"series_{seriesID}"][round - 1]["race_comments"]
        self._attendance: int = data[f"series_{seriesID}"][round - 1]["attendance"]
        self._infractions: list = data[f"series_{seriesID}"][round - 1]["infractions"]
        self._schedule: list = data[f"series_{seriesID}"][round - 1]["schedule"]
        self._radioBroadcaster: str = data[f"series_{seriesID}"][round - 1]["radio_broadcaster"]
        self._tvBroadcaster: str = data[f"series_{seriesID}"][round - 1]["television_broadcaster"]
        self._satelliteRadioBroadcaster: str = data[f"series_{seriesID}"][round - 1]["satellite_radio_broadcaster"]
        self._masterRaceID: int = data[f"series_{seriesID}"][round - 1]["master_race_id"]
        self._inspectionComplete: bool = data[f"series_{seriesID}"][round - 1]["inspection_complete"]
        self._playoffRound: int = data[f"series_{seriesID}"][round - 1]["playoff_round"]
        # self._info: Info
        # self._performance: Performance

    ###########################################################################
    #                                                                         #
    #                              Getter Methods                             #
    #                                                                         #
    ###########################################################################

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
    
    # The following properties are commented out because the Info and Performance classes have yet to be implemented.

    # @property
    # def info(self):
    #     return self._info
    
    # @property
    # def performance(self):
    #     return self._performance

if __name__ == "__main__":

    # Test instantiation of Race object.
    race = Race(2023, 1, 4)

    from inspect import getmembers
    print(getmembers(race))