import abc
from System import Array_1
from UnityEngine import Color

class VisionUtility(abc.ABC):
    @staticmethod
    def GetColorBlindSafePalette(palette: Array_1[Color], minimumLuminance: float, maximumLuminance: float) -> int: ...

