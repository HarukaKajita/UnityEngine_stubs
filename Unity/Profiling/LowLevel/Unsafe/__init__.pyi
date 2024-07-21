import typing, clr, abc
from UnityEngine import Color32
from Unity.Profiling import ProfilerCategory, ProfilerMarkerDataUnit, ProfilerCategoryColor, ProfilerFlowEventType, ProfilerCounterOptions
from Unity.Profiling.LowLevel import ProfilerMarkerDataType, MarkerFlags
from System.Collections.Generic import List_1

class ProfilerCategoryDescription:
    Color : Color32
    Flags : int
    Id : int
    NameUtf8 : clr.Reference[int]
    NameUtf8Len : int
    @property
    def Name(self) -> str: ...


class ProfilerMarkerData:
    Ptr : clr.Reference[None]
    Size : int
    Type : int


class ProfilerRecorderDescription:
    @property
    def Category(self) -> ProfilerCategory: ...
    @property
    def DataType(self) -> ProfilerMarkerDataType: ...
    @property
    def Flags(self) -> MarkerFlags: ...
    @property
    def Name(self) -> str: ...
    @property
    def NameUtf8(self) -> clr.Reference[int]: ...
    @property
    def NameUtf8Len(self) -> int: ...
    @property
    def UnitType(self) -> ProfilerMarkerDataUnit: ...


class ProfilerRecorderHandle:
    @property
    def Valid(self) -> bool: ...
    @staticmethod
    def GetAvailable(outRecorderHandleList: List_1[ProfilerRecorderHandle]) -> None: ...
    @staticmethod
    def GetDescription(handle: ProfilerRecorderHandle) -> ProfilerRecorderDescription: ...


class ProfilerUnsafeUtility(abc.ABC):
    CategoryAi : int
    CategoryAllocation : int
    CategoryAnimation : int
    CategoryAudio : int
    CategoryFileIO : int
    CategoryGUI : int
    CategoryInput : int
    CategoryInternal : int
    CategoryLighting : int
    CategoryLightning : int
    CategoryLoading : int
    CategoryNetwork : int
    CategoryOther : int
    CategoryParticles : int
    CategoryPhysics : int
    CategoryPhysics2D : int
    CategoryRender : int
    CategoryScripts : int
    CategoryVideo : int
    CategoryVirtualTexturing : int
    CategoryVr : int
    @classmethod
    @property
    def Timestamp(cls) -> int: ...
    @classmethod
    @property
    def TimestampToNanosecondsConversionRatio(cls) -> ProfilerUnsafeUtility.TimestampConversionRatio: ...
    @staticmethod
    def BeginSample(markerPtr: int) -> None: ...
    @staticmethod
    def BeginSampleWithMetadata(markerPtr: int, metadataCount: int, metadata: clr.Reference[None]) -> None: ...
    @staticmethod
    def CreateCategory(name: clr.Reference[str], nameLen: int, colorIndex: ProfilerCategoryColor) -> int: ...
    @staticmethod
    def CreateFlow(categoryId: int) -> int: ...
    @staticmethod
    def EndSample(markerPtr: int) -> None: ...
    @staticmethod
    def FlowEvent(flowId: int, flowEventType: ProfilerFlowEventType) -> None: ...
    @staticmethod
    def FlushCounterValue(counterValuePtr: clr.Reference[None]) -> None: ...
    @staticmethod
    def GetCategoryByName(name: clr.Reference[str], nameLen: int) -> int: ...
    @staticmethod
    def GetCategoryDescription(categoryId: int) -> ProfilerCategoryDescription: ...
    @staticmethod
    def SingleSampleWithMetadata(markerPtr: int, metadataCount: int, metadata: clr.Reference[None]) -> None: ...
    # Skipped CreateCounterValue due to it being static, abstract and generic.

    CreateCounterValue : CreateCounterValue_MethodGroup
    class CreateCounterValue_MethodGroup:
        @typing.overload
        def __call__(self, counterPtr: clr.Reference[int], name: str, categoryId: int, flags: MarkerFlags, dataType: int, dataUnit: int, dataSize: int, counterOptions: ProfilerCounterOptions) -> clr.Reference[None]:...
        @typing.overload
        def __call__(self, counterPtr: clr.Reference[int], name: clr.Reference[str], nameLen: int, categoryId: int, flags: MarkerFlags, dataType: int, dataUnit: int, dataSize: int, counterOptions: ProfilerCounterOptions) -> clr.Reference[None]:...

    # Skipped CreateMarker due to it being static, abstract and generic.

    CreateMarker : CreateMarker_MethodGroup
    class CreateMarker_MethodGroup:
        @typing.overload
        def __call__(self, name: str, categoryId: int, flags: MarkerFlags, metadataCount: int) -> int:...
        @typing.overload
        def __call__(self, name: clr.Reference[str], nameLen: int, categoryId: int, flags: MarkerFlags, metadataCount: int) -> int:...

    # Skipped SetMarkerMetadata due to it being static, abstract and generic.

    SetMarkerMetadata : SetMarkerMetadata_MethodGroup
    class SetMarkerMetadata_MethodGroup:
        @typing.overload
        def __call__(self, markerPtr: int, index: int, name: str, type: int, unit: int) -> None:...
        @typing.overload
        def __call__(self, markerPtr: int, index: int, name: clr.Reference[str], nameLen: int, type: int, unit: int) -> None:...


    class TimestampConversionRatio:
        Denominator : int
        Numerator : int


