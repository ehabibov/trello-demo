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


@datamodel
class CardsRequestBinding:
    idList: str = None
    name: str = None
    desc: str = None

    def with_idlist(self, id_list):
        self.idList = id_list
        return self

    def with_name(self, name):
        self.name = name
        return self

    def with_desc(self, desc):
        self.desc = desc
        return self


@datamodel
class CardCommentRequestBinding:
    text: str = None
