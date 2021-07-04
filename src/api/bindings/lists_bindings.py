from typing import List
from databind.core import datamodel


@datamodel
class CreatedListResponseBinding:
    id: str
    name: str
    closed: bool
    pos: int
    idBoard: str
    limits: List


@datamodel
class ListResponseBinding:
    id: str
    name: str
    closed: bool
    pos: int
    idBoard: str
    subscribed: bool


@datamodel
class ListCardsRequestBinding:
    id: str


@datamodel
class ListRequestBinding:
    name: str = None
    idBoard: str = None

    def with_board_id(self, id_board):
        self.idBoard = id_board
        return self

    def with_name(self, name):
        self.name = name
        return self