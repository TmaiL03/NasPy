from dataclasses import dataclass

from datamodels.Tupleable import Tupleable
from helpers.Parsers import *
from helpers.Constants import MISSING
from datamodels.StageFinisher import StageFinisher

@dataclass
class Stage(Tupleable):
    stageNumber: int
    results: list

    def __init__(self, context: dict):
        self.stageNumber = context.get("stage_number", MISSING)
        self.results = buildList(StageFinisher, context.get("results", MISSING))

    def toTuple(self) -> tuple:

        return (
            self.stageNumber,
        )