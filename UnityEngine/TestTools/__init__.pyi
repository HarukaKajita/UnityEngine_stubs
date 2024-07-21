import typing, abc
from System import Array_1, Attribute
from System.Reflection import MethodBase

class Coverage(abc.ABC):
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @enabled.setter
    def enabled(cls, value: bool) -> bool: ...
    @staticmethod
    def GetSequencePointsFor(method: MethodBase) -> Array_1[CoveredSequencePoint]: ...
    @staticmethod
    def GetStatsForAllCoveredMethods() -> Array_1[CoveredMethodStats]: ...
    @staticmethod
    def ResetAll() -> None: ...
    @staticmethod
    def ResetFor(method: MethodBase) -> None: ...
    # Skipped GetStatsFor due to it being static, abstract and generic.

    GetStatsFor : GetStatsFor_MethodGroup
    class GetStatsFor_MethodGroup:
        @typing.overload
        def __call__(self, methods: Array_1[MethodBase]) -> Array_1[CoveredMethodStats]:...
        @typing.overload
        def __call__(self, method: MethodBase) -> CoveredMethodStats:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any]) -> Array_1[CoveredMethodStats]:...



class CoveredMethodStats:
    method : MethodBase
    totalSequencePoints : int
    uncoveredSequencePoints : int
    def ToString(self) -> str: ...


class CoveredSequencePoint:
    column : int
    filename : str
    hitCount : int
    ilOffset : int
    line : int
    method : MethodBase


class ExcludeFromCoverageAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

