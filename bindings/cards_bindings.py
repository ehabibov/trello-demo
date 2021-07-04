from typing import List
from databind.core import datamodel
from api.labels import Label


@datamodel
class LabelResponseBinding:
    id: str
    idBoard: str
    name: str
    color: str


@datamodel
class CardResponseBinding:
    id: str
    name: str
    desc: str
    labels: List[LabelResponseBinding] = None


@datamodel
class CardActionsData:
    text: str


@datamodel
class CardActionsResponseBinding:
    id: str
    data: CardActionsData


@datamodel
class CardsRequestBinding:
    idList: str = None
    name: str = None
    desc: str = None

    def with_list_id(self, id_list):
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

    def with_comment(self, text):
        self.text = text
        return self


@datamodel
class CardLabelRequestBinding:
    color: str = None

    def with_color(self, label: Label):
        self.color = label.value
        return self
