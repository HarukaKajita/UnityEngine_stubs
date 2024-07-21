import typing, clr, abc
from System import IDisposable, Guid, Array_1, Span_1
from System.Collections.Generic import List_1, IList_1
from Unity.Profiling.LowLevel import MarkerFlags, ProfilerMarkerDataType
from Unity.Collections import NativeArray_1
from Unity.Profiling import ProfilerMarkerDataUnit, ProfilerCategoryFlags, ProfilerFlowEventType
from UnityEngine import Color32
from System.Collections.ObjectModel import ReadOnlyCollection_1

class FrameDataView(IDisposable, abc.ABC):
    invalidMarkerId : int
    invalidThreadId : int
    invalidThreadIndex : int
    @property
    def frameFps(self) -> float: ...
    @property
    def frameGpuTimeMs(self) -> float: ...
    @property
    def frameGpuTimeNs(self) -> int: ...
    @property
    def frameIndex(self) -> int: ...
    @property
    def frameStartTimeMs(self) -> float: ...
    @property
    def frameStartTimeNs(self) -> int: ...
    @property
    def frameTimeMs(self) -> float: ...
    @property
    def frameTimeNs(self) -> int: ...
    @property
    def maxDepth(self) -> int: ...
    @property
    def sampleCount(self) -> int: ...
    @property
    def threadGroupName(self) -> str: ...
    @property
    def threadId(self) -> int: ...
    @property
    def threadIndex(self) -> int: ...
    @property
    def threadName(self) -> str: ...
    @property
    def valid(self) -> bool: ...
    def Dispose(self) -> None: ...
    def GetAllCategories(self, categoryInfoList: List_1[ProfilerCategoryInfo]) -> None: ...
    def GetCategoryInfo(self, id: int) -> ProfilerCategoryInfo: ...
    def GetCounterValueAsDouble(self, markerId: int) -> float: ...
    def GetCounterValueAsFloat(self, markerId: int) -> float: ...
    def GetCounterValueAsInt(self, markerId: int) -> int: ...
    def GetCounterValueAsLong(self, markerId: int) -> int: ...
    def GetCounterValuePtr(self, markerId: int) -> clr.Reference[None]: ...
    def GetFrameMetaDataCount(self, id: Guid, tag: int) -> int: ...
    def GetGfxResourceInfo(self, gfxResourceId: int, info: clr.Reference[FrameDataView.GfxResourceInfo]) -> bool: ...
    def GetMarkerCategoryIndex(self, markerId: int) -> int: ...
    def GetMarkerFlags(self, markerId: int) -> MarkerFlags: ...
    def GetMarkerId(self, markerName: str) -> int: ...
    def GetMarkerMetadataInfo(self, markerId: int) -> Array_1[FrameDataView.MarkerMetadataInfo]: ...
    def GetMarkerName(self, markerId: int) -> str: ...
    def GetMarkers(self, markerInfoList: List_1[FrameDataView.MarkerInfo]) -> None: ...
    def GetSessionMetaDataCount(self, id: Guid, tag: int) -> int: ...
    def GetUnityObjectInfo(self, instanceId: int, info: clr.Reference[FrameDataView.UnityObjectInfo]) -> bool: ...
    def GetUnityObjectNativeTypeInfo(self, nativeTypeIndex: int, info: clr.Reference[FrameDataView.UnityObjectNativeTypeInfo]) -> bool: ...
    def GetUnityObjectNativeTypeInfoCount(self) -> int: ...
    def HasCounterValue(self, markerId: int) -> bool: ...
    def ResolveMethodInfo(self, addr: int) -> FrameDataView.MethodInfo: ...
    # Skipped GetFrameMetaData due to it being static, abstract and generic.

    GetFrameMetaData : GetFrameMetaData_MethodGroup
    class GetFrameMetaData_MethodGroup:
        def __getitem__(self, t:typing.Type[GetFrameMetaData_1_T1]) -> GetFrameMetaData_1[GetFrameMetaData_1_T1]: ...

        GetFrameMetaData_1_T1 = typing.TypeVar('GetFrameMetaData_1_T1')
        class GetFrameMetaData_1(typing.Generic[GetFrameMetaData_1_T1]):
            GetFrameMetaData_1_T = FrameDataView.GetFrameMetaData_MethodGroup.GetFrameMetaData_1_T1
            @typing.overload
            def __call__(self, id: Guid, tag: int) -> NativeArray_1[GetFrameMetaData_1_T]:...
            @typing.overload
            def __call__(self, id: Guid, tag: int, index: int) -> NativeArray_1[GetFrameMetaData_1_T]:...


    # Skipped GetSessionMetaData due to it being static, abstract and generic.

    GetSessionMetaData : GetSessionMetaData_MethodGroup
    class GetSessionMetaData_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSessionMetaData_1_T1]) -> GetSessionMetaData_1[GetSessionMetaData_1_T1]: ...

        GetSessionMetaData_1_T1 = typing.TypeVar('GetSessionMetaData_1_T1')
        class GetSessionMetaData_1(typing.Generic[GetSessionMetaData_1_T1]):
            GetSessionMetaData_1_T = FrameDataView.GetSessionMetaData_MethodGroup.GetSessionMetaData_1_T1
            @typing.overload
            def __call__(self, id: Guid, tag: int) -> NativeArray_1[GetSessionMetaData_1_T]:...
            @typing.overload
            def __call__(self, id: Guid, tag: int, index: int) -> NativeArray_1[GetSessionMetaData_1_T]:...



    class GfxResourceInfo:
        @property
        def relatedAllocationRootId(self) -> int: ...
        @property
        def relatedInstanceId(self) -> int: ...


    class MarkerInfo:
        category : int
        flags : MarkerFlags
        id : int
        metadataInfo : Array_1[FrameDataView.MarkerMetadataInfo]
        name : str


    class MarkerMetadataInfo:
        name : str
        type : ProfilerMarkerDataType
        unit : ProfilerMarkerDataUnit


    class MethodInfo:
        methodName : str
        sourceFileLine : int
        sourceFileName : str


    class UnityObjectInfo:
        @property
        def allocationRootId(self) -> int: ...
        @property
        def name(self) -> str: ...
        @property
        def nativeTypeIndex(self) -> int: ...
        @property
        def relatedGameObjectInstanceId(self) -> int: ...


    class UnityObjectNativeTypeInfo:
        @property
        def baseNativeTypeIndex(self) -> int: ...
        @property
        def name(self) -> str: ...



class HierarchyFrameDataView(FrameDataView):
    columnCalls : int
    columnDontSort : int
    columnGcMemory : int
    columnName : int
    columnObjectName : int
    columnSelfPercent : int
    columnSelfTime : int
    columnStartTime : int
    columnTotalPercent : int
    columnTotalTime : int
    columnWarningCount : int
    invalidSampleId : int
    @property
    def frameFps(self) -> float: ...
    @property
    def frameGpuTimeMs(self) -> float: ...
    @property
    def frameGpuTimeNs(self) -> int: ...
    @property
    def frameIndex(self) -> int: ...
    @property
    def frameStartTimeMs(self) -> float: ...
    @property
    def frameStartTimeNs(self) -> int: ...
    @property
    def frameTimeMs(self) -> float: ...
    @property
    def frameTimeNs(self) -> int: ...
    @property
    def maxDepth(self) -> int: ...
    @property
    def sampleCount(self) -> int: ...
    @property
    def sortColumn(self) -> int: ...
    @property
    def sortColumnAscending(self) -> bool: ...
    @property
    def threadGroupName(self) -> str: ...
    @property
    def threadId(self) -> int: ...
    @property
    def threadIndex(self) -> int: ...
    @property
    def threadName(self) -> str: ...
    @property
    def valid(self) -> bool: ...
    @property
    def viewMode(self) -> HierarchyFrameDataView.ViewModes: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetItemAncestors(self, id: int, outAncestors: List_1[int]) -> None: ...
    def GetItemCallstack(self, id: int, outCallstack: List_1[int]) -> None: ...
    def GetItemCategoryIndex(self, id: int) -> int: ...
    def GetItemChildren(self, id: int, outChildren: List_1[int]) -> None: ...
    def GetItemColumnData(self, id: int, column: int) -> str: ...
    def GetItemColumnDataAsDouble(self, id: int, column: int) -> float: ...
    def GetItemColumnDataAsFloat(self, id: int, column: int) -> float: ...
    def GetItemColumnDataAsSingle(self, id: int, column: int) -> float: ...
    def GetItemDepth(self, id: int) -> int: ...
    def GetItemDescendantsThatHaveChildren(self, id: int, outChildren: List_1[int]) -> None: ...
    def GetItemInstanceID(self, id: int) -> int: ...
    def GetItemMarkerFlags(self, id: int) -> MarkerFlags: ...
    def GetItemMarkerID(self, id: int) -> int: ...
    def GetItemMarkerIDPath(self, id: int, outFullIdPath: List_1[int]) -> None: ...
    def GetItemMergedSampleCallstack(self, id: int, sampleIndex: int, outCallstack: List_1[int]) -> None: ...
    def GetItemMergedSamplesColumnData(self, id: int, column: int, outStrings: List_1[str]) -> None: ...
    def GetItemMergedSamplesColumnDataAsDoubles(self, id: int, column: int, outValues: List_1[float]) -> None: ...
    def GetItemMergedSamplesColumnDataAsFloats(self, id: int, column: int, outValues: List_1[float]) -> None: ...
    def GetItemMergedSamplesCount(self, id: int) -> int: ...
    def GetItemMergedSamplesInstanceID(self, id: int, outInstanceIds: List_1[int]) -> None: ...
    def GetItemMergedSamplesMetadata(self, id: int, sampleIndex: int, metadataIndex: int) -> str: ...
    def GetItemMergedSamplesMetadataAsFloat(self, id: int, sampleIndex: int, metadataIndex: int) -> float: ...
    def GetItemMergedSamplesMetadataAsLong(self, id: int, sampleIndex: int, metadataIndex: int) -> int: ...
    def GetItemMergedSamplesMetadataCount(self, id: int, sampleIndex: int) -> int: ...
    def GetItemMetadata(self, id: int, index: int) -> str: ...
    def GetItemMetadataAsFloat(self, id: int, index: int) -> float: ...
    def GetItemMetadataAsLong(self, id: int, index: int) -> int: ...
    def GetItemMetadataCount(self, id: int) -> int: ...
    def GetItemName(self, id: int) -> str: ...
    def GetItemPath(self, id: int) -> str: ...
    def GetItemRawFrameDataViewIndices(self, id: int, outSampleIndices: List_1[int]) -> None: ...
    def GetRootItemID(self) -> int: ...
    def HasItemChildren(self, id: int) -> bool: ...
    def ItemContainsRawFrameDataViewIndex(self, id: int, sampleIndex: int) -> bool: ...
    def ResolveItemCallstack(self, id: int) -> str: ...
    def ResolveItemMergedSampleCallstack(self, id: int, sampleIndex: int) -> str: ...
    def Sort(self, sortColumn: int, sortAscending: bool) -> None: ...

    class ViewModes(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Default : HierarchyFrameDataView.ViewModes # 0
        MergeSamplesWithTheSameName : HierarchyFrameDataView.ViewModes # 1
        HideEditorOnlySamples : HierarchyFrameDataView.ViewModes # 2



class IProfilerFrameTimeViewSampleSelectionController(typing.Protocol):
    @property
    def focusedThreadIndex(self) -> int: ...
    @focusedThreadIndex.setter
    def focusedThreadIndex(self, value: int) -> int: ...
    @property
    def sampleNameSearchFilter(self) -> str: ...
    @sampleNameSearchFilter.setter
    def sampleNameSearchFilter(self, value: str) -> str: ...
    @property
    def selection(self) -> ProfilerTimeSampleSelection: ...
    @abc.abstractmethod
    def ClearSelection(self) -> None: ...
    @abc.abstractmethod
    def SetSelection(self, selection: ProfilerTimeSampleSelection) -> bool: ...


class ProfilerCategoryInfo:
    @property
    def color(self) -> Color32: ...
    @property
    def flags(self) -> ProfilerCategoryFlags: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...


class ProfilerEditorUtility(abc.ABC):
    # Skipped SetSelection due to it being static, abstract and generic.

    SetSelection : SetSelection_MethodGroup
    class SetSelection_MethodGroup:
        @typing.overload
        def __call__(self, controller: IProfilerFrameTimeViewSampleSelectionController, markerNameOrMarkerNamePath: str, frameIndex: int = ..., threadGroupName: str = ..., threadName: str = ..., threadId: int = ...) -> bool:...
        @typing.overload
        def __call__(self, controller: IProfilerFrameTimeViewSampleSelectionController, frameIndex: int, threadGroupName: str, threadName: str, sampleMarkerId: int, markerIdPath: List_1[int] = ..., threadId: int = ...) -> bool:...
        @typing.overload
        def __call__(self, controller: IProfilerFrameTimeViewSampleSelectionController, frameIndex: int, threadGroupName: str, threadName: str, sampleName: str, markerNamePath: str = ..., threadId: int = ...) -> bool:...



class ProfilerTimeSampleSelection:
    @typing.overload
    def __init__(self, frameIndex: int, threadGroupName: str, threadName: str, threadId: int, rawSampleIndex: int, sampleName: str = ...) -> None: ...
    @typing.overload
    def __init__(self, frameIndex: int, threadGroupName: str, threadName: str, threadId: int, rawSampleIndices: IList_1[int], sampleName: str = ...) -> None: ...
    @typing.overload
    def __init__(self, selection: ProfilerTimeSampleSelection) -> None: ...
    @property
    def frameIndex(self) -> int: ...
    @frameIndex.setter
    def frameIndex(self, value: int) -> int: ...
    @property
    def markerNamePath(self) -> ReadOnlyCollection_1[str]: ...
    @property
    def markerPathDepth(self) -> int: ...
    @markerPathDepth.setter
    def markerPathDepth(self, value: int) -> int: ...
    @property
    def rawSampleIndex(self) -> int: ...
    @property
    def rawSampleIndices(self) -> ReadOnlyCollection_1[int]: ...
    @property
    def sampleDisplayName(self) -> str: ...
    @sampleDisplayName.setter
    def sampleDisplayName(self, value: str) -> str: ...
    @property
    def threadGroupName(self) -> str: ...
    @threadGroupName.setter
    def threadGroupName(self, value: str) -> str: ...
    @property
    def threadId(self) -> int: ...
    @threadId.setter
    def threadId(self, value: int) -> int: ...
    @property
    def threadName(self) -> str: ...
    @threadName.setter
    def threadName(self, value: str) -> str: ...


class RawFrameDataView(FrameDataView):
    invalidSampleIndex : int
    @property
    def frameFps(self) -> float: ...
    @property
    def frameGpuTimeMs(self) -> float: ...
    @property
    def frameGpuTimeNs(self) -> int: ...
    @property
    def frameIndex(self) -> int: ...
    @property
    def frameStartTimeMs(self) -> float: ...
    @property
    def frameStartTimeNs(self) -> int: ...
    @property
    def frameTimeMs(self) -> float: ...
    @property
    def frameTimeNs(self) -> int: ...
    @property
    def maxDepth(self) -> int: ...
    @property
    def sampleCount(self) -> int: ...
    @property
    def threadGroupName(self) -> str: ...
    @property
    def threadId(self) -> int: ...
    @property
    def threadIndex(self) -> int: ...
    @property
    def threadName(self) -> str: ...
    @property
    def valid(self) -> bool: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetFlowEvents(self, outFlowEvents: List_1[RawFrameDataView.FlowEvent]) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetSampleCallstack(self, sampleIndex: int, outCallstack: List_1[int]) -> None: ...
    def GetSampleCategoryIndex(self, sampleIndex: int) -> int: ...
    def GetSampleChildrenCount(self, sampleIndex: int) -> int: ...
    def GetSampleChildrenCountRecursive(self, sampleIndex: int) -> int: ...
    def GetSampleFlags(self, sampleIndex: int) -> MarkerFlags: ...
    def GetSampleFlowEvents(self, sampleIndex: int, outFlowEvents: List_1[RawFrameDataView.FlowEvent]) -> None: ...
    def GetSampleMarkerId(self, sampleIndex: int) -> int: ...
    def GetSampleMetadataAsDouble(self, sampleIndex: int, metadataIndex: int) -> float: ...
    def GetSampleMetadataAsFloat(self, sampleIndex: int, metadataIndex: int) -> float: ...
    def GetSampleMetadataAsInt(self, sampleIndex: int, metadataIndex: int) -> int: ...
    def GetSampleMetadataAsLong(self, sampleIndex: int, metadataIndex: int) -> int: ...
    def GetSampleMetadataAsString(self, sampleIndex: int, metadataIndex: int) -> str: ...
    def GetSampleMetadataCount(self, sampleIndex: int) -> int: ...
    def GetSampleName(self, sampleIndex: int) -> str: ...
    def GetSampleStartTimeMs(self, sampleIndex: int) -> float: ...
    def GetSampleStartTimeNs(self, sampleIndex: int) -> int: ...
    def GetSampleTimeMs(self, sampleIndex: int) -> float: ...
    def GetSampleTimeNs(self, sampleIndex: int) -> int: ...
    # Skipped GetSampleMetadataAsSpan due to it being static, abstract and generic.

    GetSampleMetadataAsSpan : GetSampleMetadataAsSpan_MethodGroup
    class GetSampleMetadataAsSpan_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSampleMetadataAsSpan_1_T1]) -> GetSampleMetadataAsSpan_1[GetSampleMetadataAsSpan_1_T1]: ...

        GetSampleMetadataAsSpan_1_T1 = typing.TypeVar('GetSampleMetadataAsSpan_1_T1')
        class GetSampleMetadataAsSpan_1(typing.Generic[GetSampleMetadataAsSpan_1_T1]):
            GetSampleMetadataAsSpan_1_T = RawFrameDataView.GetSampleMetadataAsSpan_MethodGroup.GetSampleMetadataAsSpan_1_T1
            def __call__(self, sampleIndex: int, metadataIndex: int) -> Span_1[GetSampleMetadataAsSpan_1_T]:...



    class FlowEvent:
        FlowEventType : ProfilerFlowEventType
        FlowId : int
        ParentSampleIndex : int


