import typing, abc
from System import Action_2, Action_3
from UnityEngine.Profiling.Experimental import DebugScreenCapture

class CaptureFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ManagedObjects : CaptureFlags # 1
    NativeObjects : CaptureFlags # 2
    NativeAllocations : CaptureFlags # 4
    NativeAllocationSites : CaptureFlags # 8
    NativeStackTraces : CaptureFlags # 16


class MemoryProfiler(abc.ABC):
    @staticmethod
    def TakeTempSnapshot(finishCallback: Action_2[str, bool], captureFlags: CaptureFlags = ...) -> None: ...
    # Skipped TakeSnapshot due to it being static, abstract and generic.

    TakeSnapshot : TakeSnapshot_MethodGroup
    class TakeSnapshot_MethodGroup:
        @typing.overload
        def __call__(self, path: str, finishCallback: Action_2[str, bool], captureFlags: CaptureFlags = ...) -> None:...
        @typing.overload
        def __call__(self, path: str, finishCallback: Action_2[str, bool], screenshotCallback: Action_3[str, bool, DebugScreenCapture], captureFlags: CaptureFlags = ...) -> None:...



class MetaData:
    def __init__(self) -> None: ...
    content : str
    platform : str

