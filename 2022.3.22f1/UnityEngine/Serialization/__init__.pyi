import typing, clr
from System import Attribute, Array_1
from UnityEngine import Object
from System.Runtime.Serialization import ISurrogateSelector, ISerializationSurrogate, StreamingContext

class FormerlySerializedAsAttribute(Attribute):
    def __init__(self, oldName: str) -> None: ...
    @property
    def oldName(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ManagedReferenceUtility:
    def __init__(self) -> None: ...
    RefIdNull : int
    RefIdUnknown : int
    @staticmethod
    def GetManagedReference(obj: Object, id: int) -> typing.Any: ...
    @staticmethod
    def GetManagedReferenceIdForObject(obj: Object, scriptObj: typing.Any) -> int: ...
    @staticmethod
    def GetManagedReferenceIds(obj: Object) -> Array_1[int]: ...
    @staticmethod
    def SetManagedReferenceIdForObject(obj: Object, scriptObj: typing.Any, refId: int) -> bool: ...


class UnitySurrogateSelector(ISurrogateSelector):
    def __init__(self) -> None: ...
    def ChainSelector(self, selector: ISurrogateSelector) -> None: ...
    def GetNextSelector(self) -> ISurrogateSelector: ...
    def GetSurrogate(self, type: typing.Type[typing.Any], context: StreamingContext, selector: clr.Reference[ISurrogateSelector]) -> ISerializationSurrogate: ...

