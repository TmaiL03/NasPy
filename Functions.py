from urllib.request import urlopen
import json
from functools import cache

'''
Ensures that a new JSON object is only being instantiated if one does not already exist.
'''

@cache
def parseWeekendFeedURL(raceSeason: int, seriesID: int, raceID: int) -> list:
    
    url: str = f"https://cf.nascar.com/cacher/{raceSeason}/{seriesID}/{raceID}/weekend-feed.json"
    response: json = urlopen(url)
    weekendData: list = json.loads(response.read())
    raceInfo: dict = weekendData["weekend_race"][0]

    return raceInfo