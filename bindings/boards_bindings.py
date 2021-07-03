from databind.core import datamodel
from typing import List, Optional, Any


@datamodel
class Pref:
    permissionLevel: str
    hideVotes: bool
    voting: str
    comments: str
    invitations: str
    selfJoin: bool
    cardCovers: bool
    isTemplate: bool
    cardAging: Optional[str] = None
    calendarFeedEnabled: bool
    background: str
    backgroundImage: Optional[str]
    backgroundImageScaled: Optional[str]
    backgroundTile: bool
    backgroundBrightness: str
    backgroundColor: str
    backgroundBottomColor: str
    backgroundTopColor: str
    canBePublic: bool
    canBeEnterprise: bool
    canBeOrg: bool
    canBePrivate: bool
    canInvite: bool


@datamodel
class LabelNames:
    green: str
    yellow: str
    orange: str
    red: str
    purple: str
    blue: str
    sky: str
    lime: str
    pink: str
    black: str


@datamodel
class Membership:
    id: str
    idMember: str
    memberType: str
    unconfirmed: bool
    deactivated: bool


@datamodel
class BoardResponseBinding:
    id: str
    name: str
    desc: str
    descData: Optional[str]
    closed: bool
    idOrganization: str
    idEnterprise: Optional[str]
    pinned: Optional[bool]
    url: str
    shortUrl: str
    prefs: Pref
    labelNames: LabelNames


@datamodel
class MyBoardResponseBinding(BoardResponseBinding):
    dateClosed: Optional[str]
    limits: Optional[str]
    shortLink: str
    powerUps: List[Any]
    dateLastActivity: str
    idTags: List[Any]
    datePluginDisable: str
    creationMethod: str
    ixUpdate: str
    enterpriseOwned: bool
    idBoardSource: str
    idMemberCreator: str
    starred: bool
    subscribed: bool
    dateLastView: str
    templateGallery: str
    premiumFeatures: List[Any]
    memberships: List[Membership]


@datamodel
class BoardRequestBinding:
    name: str = None
