from urllib.error import HTTPError
from urllib.request import urlopen
import json
from functools import cache
from Constants import MISSING
from typing import Type, Any

@cache
def parseRaceListBasicURL(raceSeason: int, seriesID: int) -> list:

    try:
        url: str = f"https://cf.nascar.com/cacher/{raceSeason}/race_list_basic.json"
        response: json = urlopen(url)
        races: list = json.loads(response.read())
        seriesRaces: list = races[f"series_{seriesID}"]

        return seriesRaces
    
    except HTTPError as ex:
        raise Exception(f"Unable to retrieve data for season '{raceSeason}' from {url}.")

@cache
def parseWeekendFeedURL(raceSeason: int, seriesID: int, raceID: int, key: str = "weekend_race") -> list:
    
    try:
        url: str = f"https://cf.nascar.com/cacher/{raceSeason}/{seriesID}/{raceID}/weekend-feed.json"
        response: json = urlopen(url)
        weekendData: list = json.loads(response.read())

        if(key == "weekend_race"):
            raceInfo: dict = weekendData[key][0]
        else:
            raceInfo: dict = weekendData[key]
        
        return raceInfo
        
    except HTTPError as ex:
        print(f"HTTPError: {ex}. Unable to retrieve '{key}' from {url}.")
        
        return MISSING
    
    except KeyError as ex:
        print(f"KeyError: {ex}. The key '{key}' was not found in the JSON data of {url}.")
        
        return MISSING

@cache
def parseLivePitDataURL(seriesID: int, raceID: int) -> list:

    try:
        url: str = f"https://cf.nascar.com/cacher/live/series_{seriesID}/{raceID}/live-pit-data.json"
        response: json = urlopen(url)
        pitData: list = json.loads(response.read())

        return pitData

    except HTTPError as ex:
        print(f"HTTPError: {ex}. Unable to retrieve data from {url}.")
        
        return MISSING

@cache
def parseLapTimesURL(raceSeason: int, seriesID: int, raceID: int) -> list:

    try:
        url: str = f"https://cf.nascar.com/cacher/{raceSeason}/{seriesID}/{raceID}/lap-times.json"
        response: json = urlopen(url)
        lapTimesData: list = json.loads(response.read())
        lapTimes: list = lapTimesData["laps"]
        
        return lapTimes
    
    except HTTPError as ex:
        print(f"HTTPError: {ex}. Unable to retrieve data from {url}.")
        
        return MISSING
    
    except KeyError as ex:
        print(f"KeyError: {ex}. The key 'laps' was not found in the JSON data of {url}.")
        
        return MISSING
    
@cache
def parseLapNotesURL(raceSeason: int, seriesID: int, raceID: int) -> dict:

    url: str = f"https://cf.nascar.com/cacher/{raceSeason}/{seriesID}/{raceID}/lap-notes.json"
    response: json = urlopen(url)
    lapNotesData: dict = json.loads(response.read())
    lapNotes: dict = lapNotesData["laps"]

    return lapNotes

# Used for building lists of data objects of the specified class type using the provided context.
def buildList(cls: Type[Any], dataCollection: dict | list | object) -> list | object:

    if dataCollection is MISSING:
        return MISSING
    
    else:
        objectList: list = []

        for dataObject in dataCollection:
            objectList.append(cls(dataObject))
        
        return objectList