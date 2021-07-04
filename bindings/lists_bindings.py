from typing import List
from databind.core import datamodel


@datamodel
class ListRequestBinding:
    name: str = None
    idBoard: str = None


@datamodel
class CreatedListResponseBinding:
    id: str
    name: str
    closed: bool
    pos: int
    idBoard: str
    limits: List


@datamodel
class ListCardsRequestBinding:
    id: str
