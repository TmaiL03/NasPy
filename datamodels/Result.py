from dataclasses import dataclass
from Helpers.Constants import MISSING

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
        self.diffTime = context.get("diff_time", MISSING)  # Returned value in milliseconds.

        # Introduced for round <tbd> of the <tbd> season (need to go back to identify when this key was introduced).
        self.pitBox = context.get("pit_box", MISSING)