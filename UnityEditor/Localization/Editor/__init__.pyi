import typing, abc
from System import Attribute, IDisposable
from UnityEngine import Behaviour

class Localization(abc.ABC):
    @staticmethod
    def Tr(str: str) -> str: ...


class LocalizationAttribute(Attribute):
    def __init__(self, locGroupName: str = ...) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class LocalizationGroup(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, behaviour: Behaviour) -> None: ...
    @typing.overload
    def __init__(self, obj: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any]) -> None: ...
    @property
    def locGroupName(self) -> str: ...
    def Dispose(self) -> None: ...

