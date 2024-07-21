import typing, abc
from System import Attribute

class AlwaysLinkAssemblyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class GarbageCollector(abc.ABC):
    @classmethod
    @property
    def GCMode(cls) -> GarbageCollector.Mode: ...
    @classmethod
    @GCMode.setter
    def GCMode(cls, value: GarbageCollector.Mode) -> GarbageCollector.Mode: ...
    @classmethod
    @property
    def incrementalTimeSliceNanoseconds(cls) -> int: ...
    @classmethod
    @incrementalTimeSliceNanoseconds.setter
    def incrementalTimeSliceNanoseconds(cls, value: int) -> int: ...
    @classmethod
    @property
    def isIncremental(cls) -> bool: ...
    @staticmethod
    def CollectIncremental(nanoseconds: int = ...) -> bool: ...

    class Mode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Disabled : GarbageCollector.Mode # 0
        Enabled : GarbageCollector.Mode # 1
        Manual : GarbageCollector.Mode # 2



class PreserveAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequireAttributeUsagesAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequireDerivedAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequiredInterfaceAttribute(Attribute):
    def __init__(self, interfaceType: typing.Type[typing.Any]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequiredMemberAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RequireImplementorsAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

