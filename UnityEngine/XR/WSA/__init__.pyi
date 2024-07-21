import typing

class RemoteDeviceVersion(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    V1 : RemoteDeviceVersion # 0
    V2 : RemoteDeviceVersion # 1

