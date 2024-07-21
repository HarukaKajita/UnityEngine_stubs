import typing, abc
from System import Array_1

class ForcedCrashCategory(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    AccessViolation : ForcedCrashCategory # 0
    FatalError : ForcedCrashCategory # 1
    Abort : ForcedCrashCategory # 2
    PureVirtualFunction : ForcedCrashCategory # 3
    MonoAbort : ForcedCrashCategory # 4


class PlayerConnection(abc.ABC):
    @classmethod
    @property
    def connected(cls) -> bool: ...
    @staticmethod
    def SendFile(remoteFilePath: str, data: Array_1[int]) -> None: ...


class Utils(abc.ABC):
    @staticmethod
    def ForceCrash(crashCategory: ForcedCrashCategory) -> None: ...
    @staticmethod
    def NativeAssert(message: str) -> None: ...
    @staticmethod
    def NativeError(message: str) -> None: ...
    @staticmethod
    def NativeWarning(message: str) -> None: ...
    @staticmethod
    def ValidateHeap() -> None: ...

