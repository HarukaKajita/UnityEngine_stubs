import typing

class MarkerFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Default : MarkerFlags # 0
    Script : MarkerFlags # 2
    AvailabilityEditor : MarkerFlags # 4
    AvailabilityNonDevelopment : MarkerFlags # 8
    Warning : MarkerFlags # 16
    ScriptInvoke : MarkerFlags # 32
    ScriptDeepProfiler : MarkerFlags # 64
    Counter : MarkerFlags # 128
    SampleGPU : MarkerFlags # 256


class ProfilerMarkerDataType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    InstanceId : ProfilerMarkerDataType # 1
    Int32 : ProfilerMarkerDataType # 2
    UInt32 : ProfilerMarkerDataType # 3
    Int64 : ProfilerMarkerDataType # 4
    UInt64 : ProfilerMarkerDataType # 5
    Float : ProfilerMarkerDataType # 6
    Double : ProfilerMarkerDataType # 7
    String16 : ProfilerMarkerDataType # 9
    Blob8 : ProfilerMarkerDataType # 11
    GfxResourceId : ProfilerMarkerDataType # 12

