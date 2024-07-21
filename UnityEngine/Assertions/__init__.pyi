import typing, abc
from System.Collections.Generic import IEqualityComparer_1
from UnityEngine import Object
from System import Exception
from System.Collections import IDictionary
from System.Reflection import MethodBase

class Assert(abc.ABC):
    raiseExceptions : bool
    @staticmethod
    def Equals(obj1: typing.Any, obj2: typing.Any) -> bool: ...
    @staticmethod
    def ReferenceEquals(obj1: typing.Any, obj2: typing.Any) -> bool: ...
    # Skipped AreApproximatelyEqual due to it being static, abstract and generic.

    AreApproximatelyEqual : AreApproximatelyEqual_MethodGroup
    class AreApproximatelyEqual_MethodGroup:
        @typing.overload
        def __call__(self, expected: float, actual: float) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, tolerance: float) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, message: str) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, tolerance: float, message: str) -> None:...

    # Skipped AreEqual due to it being static, abstract and generic.

    AreEqual : AreEqual_MethodGroup
    class AreEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[AreEqual_1_T1]) -> AreEqual_1[AreEqual_1_T1]: ...

        AreEqual_1_T1 = typing.TypeVar('AreEqual_1_T1')
        class AreEqual_1(typing.Generic[AreEqual_1_T1]):
            AreEqual_1_T = Assert.AreEqual_MethodGroup.AreEqual_1_T1
            @typing.overload
            def __call__(self, expected: AreEqual_1_T, actual: AreEqual_1_T) -> None:...
            @typing.overload
            def __call__(self, expected: AreEqual_1_T, actual: AreEqual_1_T, message: str) -> None:...
            @typing.overload
            def __call__(self, expected: AreEqual_1_T, actual: AreEqual_1_T, message: str, comparer: IEqualityComparer_1[AreEqual_1_T]) -> None:...

        @typing.overload
        def __call__(self, expected: int, actual: int) -> None:...
        # Method AreEqual(expected : Byte, actual : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: str, actual: str) -> None:...
        # Method AreEqual(expected : Int16, actual : Int16) was skipped since it collides with above method
        # Method AreEqual(expected : UInt16, actual : UInt16) was skipped since it collides with above method
        # Method AreEqual(expected : Int32, actual : Int32) was skipped since it collides with above method
        # Method AreEqual(expected : UInt32, actual : UInt32) was skipped since it collides with above method
        # Method AreEqual(expected : Int64, actual : Int64) was skipped since it collides with above method
        # Method AreEqual(expected : UInt64, actual : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: int, actual: int, message: str) -> None:...
        # Method AreEqual(expected : Byte, actual : Byte, message : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: str, actual: str, message: str) -> None:...
        # Method AreEqual(expected : Int16, actual : Int16, message : String) was skipped since it collides with above method
        # Method AreEqual(expected : UInt16, actual : UInt16, message : String) was skipped since it collides with above method
        # Method AreEqual(expected : Int32, actual : Int32, message : String) was skipped since it collides with above method
        # Method AreEqual(expected : UInt32, actual : UInt32, message : String) was skipped since it collides with above method
        # Method AreEqual(expected : Int64, actual : Int64, message : String) was skipped since it collides with above method
        # Method AreEqual(expected : UInt64, actual : UInt64, message : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: Object, actual: Object, message: str) -> None:...

    # Skipped AreNotApproximatelyEqual due to it being static, abstract and generic.

    AreNotApproximatelyEqual : AreNotApproximatelyEqual_MethodGroup
    class AreNotApproximatelyEqual_MethodGroup:
        @typing.overload
        def __call__(self, expected: float, actual: float) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, tolerance: float) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, message: str) -> None:...
        @typing.overload
        def __call__(self, expected: float, actual: float, tolerance: float, message: str) -> None:...

    # Skipped AreNotEqual due to it being static, abstract and generic.

    AreNotEqual : AreNotEqual_MethodGroup
    class AreNotEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[AreNotEqual_1_T1]) -> AreNotEqual_1[AreNotEqual_1_T1]: ...

        AreNotEqual_1_T1 = typing.TypeVar('AreNotEqual_1_T1')
        class AreNotEqual_1(typing.Generic[AreNotEqual_1_T1]):
            AreNotEqual_1_T = Assert.AreNotEqual_MethodGroup.AreNotEqual_1_T1
            @typing.overload
            def __call__(self, expected: AreNotEqual_1_T, actual: AreNotEqual_1_T) -> None:...
            @typing.overload
            def __call__(self, expected: AreNotEqual_1_T, actual: AreNotEqual_1_T, message: str) -> None:...
            @typing.overload
            def __call__(self, expected: AreNotEqual_1_T, actual: AreNotEqual_1_T, message: str, comparer: IEqualityComparer_1[AreNotEqual_1_T]) -> None:...

        @typing.overload
        def __call__(self, expected: int, actual: int) -> None:...
        # Method AreNotEqual(expected : Byte, actual : Byte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: str, actual: str) -> None:...
        # Method AreNotEqual(expected : Int16, actual : Int16) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt16, actual : UInt16) was skipped since it collides with above method
        # Method AreNotEqual(expected : Int32, actual : Int32) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt32, actual : UInt32) was skipped since it collides with above method
        # Method AreNotEqual(expected : Int64, actual : Int64) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt64, actual : UInt64) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: int, actual: int, message: str) -> None:...
        # Method AreNotEqual(expected : Byte, actual : Byte, message : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: str, actual: str, message: str) -> None:...
        # Method AreNotEqual(expected : Int16, actual : Int16, message : String) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt16, actual : UInt16, message : String) was skipped since it collides with above method
        # Method AreNotEqual(expected : Int32, actual : Int32, message : String) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt32, actual : UInt32, message : String) was skipped since it collides with above method
        # Method AreNotEqual(expected : Int64, actual : Int64, message : String) was skipped since it collides with above method
        # Method AreNotEqual(expected : UInt64, actual : UInt64, message : String) was skipped since it collides with above method
        @typing.overload
        def __call__(self, expected: Object, actual: Object, message: str) -> None:...

    # Skipped IsFalse due to it being static, abstract and generic.

    IsFalse : IsFalse_MethodGroup
    class IsFalse_MethodGroup:
        @typing.overload
        def __call__(self, condition: bool) -> None:...
        @typing.overload
        def __call__(self, condition: bool, message: str) -> None:...

    # Skipped IsNotNull due to it being static, abstract and generic.

    IsNotNull : IsNotNull_MethodGroup
    class IsNotNull_MethodGroup:
        def __getitem__(self, t:typing.Type[IsNotNull_1_T1]) -> IsNotNull_1[IsNotNull_1_T1]: ...

        IsNotNull_1_T1 = typing.TypeVar('IsNotNull_1_T1')
        class IsNotNull_1(typing.Generic[IsNotNull_1_T1]):
            IsNotNull_1_T = Assert.IsNotNull_MethodGroup.IsNotNull_1_T1
            @typing.overload
            def __call__(self, value: IsNotNull_1_T) -> None:...
            @typing.overload
            def __call__(self, value: IsNotNull_1_T, message: str) -> None:...

        def __call__(self, value: Object, message: str) -> None:...

    # Skipped IsNull due to it being static, abstract and generic.

    IsNull : IsNull_MethodGroup
    class IsNull_MethodGroup:
        def __getitem__(self, t:typing.Type[IsNull_1_T1]) -> IsNull_1[IsNull_1_T1]: ...

        IsNull_1_T1 = typing.TypeVar('IsNull_1_T1')
        class IsNull_1(typing.Generic[IsNull_1_T1]):
            IsNull_1_T = Assert.IsNull_MethodGroup.IsNull_1_T1
            @typing.overload
            def __call__(self, value: IsNull_1_T) -> None:...
            @typing.overload
            def __call__(self, value: IsNull_1_T, message: str) -> None:...

        def __call__(self, value: Object, message: str) -> None:...

    # Skipped IsTrue due to it being static, abstract and generic.

    IsTrue : IsTrue_MethodGroup
    class IsTrue_MethodGroup:
        @typing.overload
        def __call__(self, condition: bool) -> None:...
        @typing.overload
        def __call__(self, condition: bool, message: str) -> None:...



class AssertionException(Exception):
    def __init__(self, message: str, userMessage: str) -> None: ...
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

