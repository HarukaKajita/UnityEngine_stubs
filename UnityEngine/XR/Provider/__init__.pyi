import clr, abc
from UnityEngine import IntegratedSubsystem

class XRStats(abc.ABC):
    @staticmethod
    def TryGetStat(xrSubsystem: IntegratedSubsystem, tag: str, value: clr.Reference[float]) -> bool: ...

