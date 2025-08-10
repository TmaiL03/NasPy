from urllib.request import urlopen
import json
from functools import cache
from Constants import MISSING
from typing import Type, Any

@cache
def parseWeekendFeedURL(raceSeason: int, seriesID: int, raceID: int) -> list:
    
    url: str = f"https://cf.nascar.com/cacher/{raceSeason}/{seriesID}/{raceID}/weekend-feed.json"
    response: json = urlopen(url)
    weekendData: list = json.loads(response.read())
    raceInfo: dict = weekendData["weekend_race"][0]

    return raceInfo

@cache
def parseLivePitDataURL(seriesID: int, raceID: int) -> list:

    url: str = f"https://cf.nascar.com/cacher/live/series_{seriesID}/{raceID}/live-pit-data.json"
    response: json = urlopen(url)
    pitData: list = json.loads(response.read())

    return pitData

# Used for building lists of data objects of the specified class type using the provided context.
def buildList(cls: Type[Any], dataCollection: dict | list | object) -> list | object:

    if dataCollection is MISSING:
        return MISSING
    
    else:
        objectList: list = []

        for dataObject in dataCollection:
            objectList.append(cls(dataObject))
        
        return objectList