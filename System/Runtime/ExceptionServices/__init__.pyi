import typing
from System import Exception, EventArgs, Attribute

class ExceptionDispatchInfo:
    @property
    def SourceException(self) -> Exception: ...
    @staticmethod
    def Capture(source: Exception) -> ExceptionDispatchInfo: ...
    @staticmethod
    def SetCurrentStackTrace(source: Exception) -> Exception: ...
    @staticmethod
    def SetRemoteStackTrace(source: Exception, stackTrace: str) -> Exception: ...
    # Skipped Throw due to it being static, abstract and generic.

    Throw : Throw_MethodGroup
    class Throw_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, source: Exception) -> None:...



class FirstChanceExceptionEventArgs(EventArgs):
    def __init__(self, exception: Exception) -> None: ...
    @property
    def Exception(self) -> Exception: ...


class HandleProcessCorruptedStateExceptionsAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

