from typing import List
from databind.core import datamodel


@datamodel
class Label:
    id: str
    idBoard: str
    name: str
    color: str


@datamodel
class CardResponseBinding:
    id: str
    name: str
    desc: str
    labels: List[Label] = None