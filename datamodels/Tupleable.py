from abc import ABC, abstractmethod
from typing import Tuple


class Tupleable(ABC):

    @abstractmethod
    def toTuple(self) -> Tuple:
        pass