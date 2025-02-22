import typing, clr, abc
from System import IDisposable, DateTime, Decimal, TypeCode, Attribute, EventArgs, SystemException, Exception
from System.Collections import IDictionary, IEnumerator
from System.Reflection import MethodBase

class DeserializationToken(IDisposable):
    def Dispose(self) -> None: ...


class IDeserializationCallback(typing.Protocol):
    @abc.abstractmethod
    def OnDeserialization(self, sender: typing.Any) -> None: ...


class IFormatterConverter(typing.Protocol):
    @abc.abstractmethod
    def ToBoolean(self, value: typing.Any) -> bool: ...
    @abc.abstractmethod
    def ToByte(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToChar(self, value: typing.Any) -> str: ...
    @abc.abstractmethod
    def ToDateTime(self, value: typing.Any) -> DateTime: ...
    @abc.abstractmethod
    def ToDecimal(self, value: typing.Any) -> Decimal: ...
    @abc.abstractmethod
    def ToDouble(self, value: typing.Any) -> float: ...
    @abc.abstractmethod
    def ToInt16(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToInt32(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToInt64(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToSByte(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToSingle(self, value: typing.Any) -> float: ...
    @abc.abstractmethod
    def ToString(self, value: typing.Any) -> str: ...
    @abc.abstractmethod
    def ToUInt16(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToUInt32(self, value: typing.Any) -> int: ...
    @abc.abstractmethod
    def ToUInt64(self, value: typing.Any) -> int: ...
    # Skipped Convert due to it being static, abstract and generic.

    Convert : Convert_MethodGroup
    class Convert_MethodGroup:
        @typing.overload
        def __call__(self, value: typing.Any, typeCode: TypeCode) -> typing.Any:...
        @typing.overload
        def __call__(self, value: typing.Any, type: typing.Type[typing.Any]) -> typing.Any:...



class IObjectReference(typing.Protocol):
    @abc.abstractmethod
    def GetRealObject(self, context: StreamingContext) -> typing.Any: ...


class ISafeSerializationData(typing.Protocol):
    @abc.abstractmethod
    def CompleteDeserialization(self, deserialized: typing.Any) -> None: ...


class ISerializable(typing.Protocol):
    @abc.abstractmethod
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class ISerializationSurrogate(typing.Protocol):
    @abc.abstractmethod
    def GetObjectData(self, obj: typing.Any, info: SerializationInfo, context: StreamingContext) -> None: ...
    @abc.abstractmethod
    def SetObjectData(self, obj: typing.Any, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> typing.Any: ...


class ISurrogateSelector(typing.Protocol):
    @abc.abstractmethod
    def ChainSelector(self, selector: ISurrogateSelector) -> None: ...
    @abc.abstractmethod
    def GetNextSelector(self) -> ISurrogateSelector: ...
    @abc.abstractmethod
    def GetSurrogate(self, type: typing.Type[typing.Any], context: StreamingContext, selector: clr.Reference[ISurrogateSelector]) -> ISerializationSurrogate: ...


class OnDeserializedAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class OnDeserializingAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class OnSerializedAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class OnSerializingAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class OptionalFieldAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...
    @property
    def VersionAdded(self) -> int: ...
    @VersionAdded.setter
    def VersionAdded(self, value: int) -> int: ...


class SafeSerializationEventArgs(EventArgs):
    @property
    def StreamingContext(self) -> StreamingContext: ...
    def AddSerializedState(self, serializedState: ISafeSerializationData) -> None: ...


class SerializationEntry:
    @property
    def Name(self) -> str: ...
    @property
    def ObjectType(self) -> typing.Type[typing.Any]: ...
    @property
    def Value(self) -> typing.Any: ...


class SerializationException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class SerializationInfo:
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any], converter: IFormatterConverter) -> None: ...
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any], converter: IFormatterConverter, requireSameTokenInPartialTrust: bool) -> None: ...
    @property
    def AssemblyName(self) -> str: ...
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> str: ...
    @classmethod
    @property
    def DeserializationInProgress(cls) -> bool: ...
    @property
    def FullTypeName(self) -> str: ...
    @FullTypeName.setter
    def FullTypeName(self, value: str) -> str: ...
    @property
    def IsAssemblyNameSetExplicit(self) -> bool: ...
    @IsAssemblyNameSetExplicit.setter
    def IsAssemblyNameSetExplicit(self, value: bool) -> bool: ...
    @property
    def IsFullTypeNameSetExplicit(self) -> bool: ...
    @IsFullTypeNameSetExplicit.setter
    def IsFullTypeNameSetExplicit(self, value: bool) -> bool: ...
    @property
    def MemberCount(self) -> int: ...
    @property
    def ObjectType(self) -> typing.Type[typing.Any]: ...
    def GetBoolean(self, name: str) -> bool: ...
    def GetByte(self, name: str) -> int: ...
    def GetChar(self, name: str) -> str: ...
    def GetDateTime(self, name: str) -> DateTime: ...
    def GetDecimal(self, name: str) -> Decimal: ...
    def GetDouble(self, name: str) -> float: ...
    def GetEnumerator(self) -> SerializationInfoEnumerator: ...
    def GetInt16(self, name: str) -> int: ...
    def GetInt32(self, name: str) -> int: ...
    def GetInt64(self, name: str) -> int: ...
    def GetSByte(self, name: str) -> int: ...
    def GetSingle(self, name: str) -> float: ...
    def GetString(self, name: str) -> str: ...
    def GetUInt16(self, name: str) -> int: ...
    def GetUInt32(self, name: str) -> int: ...
    def GetUInt64(self, name: str) -> int: ...
    def GetValue(self, name: str, type: typing.Type[typing.Any]) -> typing.Any: ...
    def SetType(self, type: typing.Type[typing.Any]) -> None: ...
    @staticmethod
    def StartDeserialization() -> DeserializationToken: ...
    def UpdateValue(self, name: str, value: typing.Any, type: typing.Type[typing.Any]) -> None: ...
    # Skipped AddValue due to it being static, abstract and generic.

    AddValue : AddValue_MethodGroup
    class AddValue_MethodGroup:
        @typing.overload
        def __call__(self, name: str, value: float) -> None:...
        # Method AddValue(name : String, value : Double) was skipped since it collides with above method
        @typing.overload
        def __call__(self, name: str, value: str) -> None:...
        # Method AddValue(name : String, value : SByte) was skipped since it collides with above method
        # Method AddValue(name : String, value : Byte) was skipped since it collides with above method
        # Method AddValue(name : String, value : Int16) was skipped since it collides with above method
        # Method AddValue(name : String, value : UInt16) was skipped since it collides with above method
        # Method AddValue(name : String, value : Int32) was skipped since it collides with above method
        # Method AddValue(name : String, value : UInt32) was skipped since it collides with above method
        # Method AddValue(name : String, value : Int64) was skipped since it collides with above method
        # Method AddValue(name : String, value : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, name: str, value: Decimal) -> None:...
        @typing.overload
        def __call__(self, name: str, value: DateTime) -> None:...
        # Method AddValue(name : String, value : Boolean) was skipped since it collides with above method
        @typing.overload
        def __call__(self, name: str, value: typing.Any) -> None:...
        @typing.overload
        def __call__(self, name: str, value: typing.Any, type: typing.Type[typing.Any]) -> None:...

    # Skipped ThrowIfDeserializationInProgress due to it being static, abstract and generic.

    ThrowIfDeserializationInProgress : ThrowIfDeserializationInProgress_MethodGroup
    class ThrowIfDeserializationInProgress_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, switchSuffix: str, cachedValue: clr.Reference[int]) -> None:...



class SerializationInfoEnumerator(IEnumerator):
    @property
    def Current(self) -> SerializationEntry: ...
    @property
    def Name(self) -> str: ...
    @property
    def ObjectType(self) -> typing.Type[typing.Any]: ...
    @property
    def Value(self) -> typing.Any: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class StreamingContext:
    @typing.overload
    def __init__(self, state: StreamingContextStates) -> None: ...
    @typing.overload
    def __init__(self, state: StreamingContextStates, additional: typing.Any) -> None: ...
    @property
    def Context(self) -> typing.Any: ...
    @property
    def State(self) -> StreamingContextStates: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...


class StreamingContextStates(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    CrossProcess : StreamingContextStates # 1
    CrossMachine : StreamingContextStates # 2
    File : StreamingContextStates # 4
    Persistence : StreamingContextStates # 8
    Remoting : StreamingContextStates # 16
    Other : StreamingContextStates # 32
    Clone : StreamingContextStates # 64
    CrossAppDomain : StreamingContextStates # 128
    All : StreamingContextStates # 255

