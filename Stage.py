from dataclasses import dataclass
from Parsers import *
from Constants import MISSING
from StageFinisher import StageFinisher

@dataclass
class Stage:
    stageNumber: int
    results: list

    def __init__(self, context: dict):
        self.stageNumber = context.get("stage_number", MISSING)
        self.results = buildList(StageFinisher, context.get("results", MISSING))