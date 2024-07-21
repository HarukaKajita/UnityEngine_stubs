import typing, abc
from UnityEngine import Component, GameObject
from System.Collections import Stack
from System import Attribute

class APIUpdaterRuntimeServices:
    def __init__(self) -> None: ...
    @staticmethod
    def AddComponent(go: GameObject, sourceInfo: str, name: str) -> Component: ...


class GenericStack(Stack):
    def __init__(self) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def SyncRoot(self) -> typing.Any: ...


class GIDebugVisualisation(abc.ABC):
    @classmethod
    @property
    def cycleMode(cls) -> bool: ...
    @classmethod
    @property
    def pauseCycleMode(cls) -> bool: ...
    @classmethod
    @property
    def texType(cls) -> GITextureType: ...
    @classmethod
    @texType.setter
    def texType(cls, value: GITextureType) -> GITextureType: ...
    @staticmethod
    def CycleSkipInstances(skip: int) -> None: ...
    @staticmethod
    def CycleSkipSystems(skip: int) -> None: ...
    @staticmethod
    def PauseCycleMode() -> None: ...
    @staticmethod
    def PlayCycleMode() -> None: ...
    @staticmethod
    def ResetRuntimeInputTextures() -> None: ...
    @staticmethod
    def StopCycleMode() -> None: ...


class GITextureType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Charting : GITextureType # 0
    Albedo : GITextureType # 1
    Emissive : GITextureType # 2
    Irradiance : GITextureType # 3
    Directionality : GITextureType # 4
    Baked : GITextureType # 5
    BakedDirectional : GITextureType # 6
    InputWorkspace : GITextureType # 7
    BakedShadowMask : GITextureType # 8
    BakedAlbedo : GITextureType # 9
    BakedEmissive : GITextureType # 10
    BakedCharting : GITextureType # 11
    BakedTexelValidity : GITextureType # 12
    BakedUVOverlap : GITextureType # 13
    BakedLightmapCulling : GITextureType # 14


class MathfInternal:
    FloatMinDenormal : float
    FloatMinNormal : float
    IsFlushToZeroEnabled : bool


class MemorylessManager:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def depthMemorylessMode(cls) -> MemorylessMode: ...
    @classmethod
    @depthMemorylessMode.setter
    def depthMemorylessMode(cls, value: MemorylessMode) -> MemorylessMode: ...


class MemorylessMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unused : MemorylessMode # 0
    Forced : MemorylessMode # 1
    Automatic : MemorylessMode # 2


class TypeInferenceRuleAttribute(Attribute):
    @typing.overload
    def __init__(self, rule: TypeInferenceRules) -> None: ...
    @typing.overload
    def __init__(self, rule: str) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    def ToString(self) -> str: ...


class TypeInferenceRules(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TypeReferencedByFirstArgument : TypeInferenceRules # 0
    TypeReferencedBySecondArgument : TypeInferenceRules # 1
    ArrayOfTypeReferencedByFirstArgument : TypeInferenceRules # 2
    TypeOfFirstArgument : TypeInferenceRules # 3

