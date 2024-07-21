import typing
from System import Attribute

class MonoPInvokeCallbackAttribute(Attribute):
    def __init__(self, type: typing.Type[typing.Any]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

