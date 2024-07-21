import typing, abc
from System import Array_1

class MacroEvaluator(abc.ABC):
    @staticmethod
    def Eval(macro: str) -> str: ...


class MethodEvaluator(abc.ABC):
    @staticmethod
    def Eval(assemblyFile: str, typeName: str, methodName: str, paramTypes: Array_1[typing.Type[typing.Any]], args: Array_1[typing.Any]) -> typing.Any: ...
    @staticmethod
    def ExecuteExternalCode(parcel: str) -> typing.Any: ...

