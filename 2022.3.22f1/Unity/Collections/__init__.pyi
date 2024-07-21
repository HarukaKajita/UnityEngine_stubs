import typing, clr, abc
from System import Attribute, IEquatable_1, IDisposable, Array_1, ReadOnlySpan_1, Span_1
from System.Collections.Generic import IEnumerable_1, IEnumerator_1
from Unity.Jobs import JobHandle

class Allocator(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Invalid : Allocator # 0
    None_ : Allocator # 1
    Temp : Allocator # 2
    TempJob : Allocator # 3
    Persistent : Allocator # 4
    AudioKernel : Allocator # 5
    FirstUserIndex : Allocator # 64


class DeallocateOnJobCompletionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeArray_GenericClasses(abc.ABCMeta):
    Generic_NativeArray_GenericClasses_NativeArray_1_T = typing.TypeVar('Generic_NativeArray_GenericClasses_NativeArray_1_T')
    def __getitem__(self, types : typing.Type[Generic_NativeArray_GenericClasses_NativeArray_1_T]) -> typing.Type[NativeArray_1[Generic_NativeArray_GenericClasses_NativeArray_1_T]]: ...

NativeArray : NativeArray_GenericClasses

NativeArray_1_T = typing.TypeVar('NativeArray_1_T')
class NativeArray_1(typing.Generic[NativeArray_1_T], IEnumerable_1[NativeArray_1_T], IEquatable_1[NativeArray_1[NativeArray_1_T]], IDisposable):
    @typing.overload
    def __init__(self, array: Array_1[NativeArray_1_T], allocator: Allocator) -> None: ...
    @typing.overload
    def __init__(self, array: NativeArray_1[NativeArray_1_T], allocator: Allocator) -> None: ...
    @typing.overload
    def __init__(self, length: int, allocator: Allocator, options: NativeArrayOptions = ...) -> None: ...
    @property
    def IsCreated(self) -> bool: ...
    @property
    def Item(self) -> NativeArray_1_T: ...
    @Item.setter
    def Item(self, value: NativeArray_1_T) -> NativeArray_1_T: ...
    @property
    def Length(self) -> int: ...
    def AsReadOnly(self) -> NativeArray_1.ReadOnly_1[NativeArray_1_T]: ...
    def AsReadOnlySpan(self) -> ReadOnlySpan_1[NativeArray_1_T]: ...
    def AsSpan(self) -> Span_1[NativeArray_1_T]: ...
    def GetEnumerator(self) -> NativeArray_1.Enumerator_1[NativeArray_1_T]: ...
    def GetHashCode(self) -> int: ...
    def GetSubArray(self, start: int, length: int) -> NativeArray_1[NativeArray_1_T]: ...
    def __eq__(self, left: NativeArray_1[NativeArray_1_T], right: NativeArray_1[NativeArray_1_T]) -> bool: ...
    # Operator not supported op_Implicit(source: NativeArray`1&)
    # Operator not supported op_Implicit(source: NativeArray`1&)
    def __ne__(self, left: NativeArray_1[NativeArray_1_T], right: NativeArray_1[NativeArray_1_T]) -> bool: ...
    def ToArray(self) -> Array_1[NativeArray_1_T]: ...
    # Skipped Copy due to it being static, abstract and generic.

    Copy : Copy_MethodGroup[NativeArray_1_T]
    Copy_MethodGroup_NativeArray_1_T = typing.TypeVar('Copy_MethodGroup_NativeArray_1_T')
    class Copy_MethodGroup(typing.Generic[Copy_MethodGroup_NativeArray_1_T]):
        Copy_MethodGroup_NativeArray_1_T = NativeArray_1.Copy_MethodGroup_NativeArray_1_T
        @typing.overload
        def __call__(self, src: Array_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dst: Array_1[Copy_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], dst: Array_1[Copy_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, src: Array_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dst: Array_1[Copy_MethodGroup_NativeArray_1_T], length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], dst: Array_1[Copy_MethodGroup_NativeArray_1_T], length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], length: int) -> None:...
        @typing.overload
        def __call__(self, src: Array_1[Copy_MethodGroup_NativeArray_1_T], srcIndex: int, dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dstIndex: int, length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], srcIndex: int, dst: Array_1[Copy_MethodGroup_NativeArray_1_T], dstIndex: int, length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], srcIndex: int, dst: Array_1[Copy_MethodGroup_NativeArray_1_T], dstIndex: int, length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], srcIndex: int, dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dstIndex: int, length: int) -> None:...
        @typing.overload
        def __call__(self, src: NativeArray_1.ReadOnly_1[Copy_MethodGroup_NativeArray_1_T], srcIndex: int, dst: NativeArray_1[Copy_MethodGroup_NativeArray_1_T], dstIndex: int, length: int) -> None:...

    # Skipped CopyFrom due to it being static, abstract and generic.

    CopyFrom : CopyFrom_MethodGroup[NativeArray_1_T]
    CopyFrom_MethodGroup_NativeArray_1_T = typing.TypeVar('CopyFrom_MethodGroup_NativeArray_1_T')
    class CopyFrom_MethodGroup(typing.Generic[CopyFrom_MethodGroup_NativeArray_1_T]):
        CopyFrom_MethodGroup_NativeArray_1_T = NativeArray_1.CopyFrom_MethodGroup_NativeArray_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyFrom_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, array: NativeArray_1[CopyFrom_MethodGroup_NativeArray_1_T]) -> None:...

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup[NativeArray_1_T]
    CopyTo_MethodGroup_NativeArray_1_T = typing.TypeVar('CopyTo_MethodGroup_NativeArray_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_NativeArray_1_T]):
        CopyTo_MethodGroup_NativeArray_1_T = NativeArray_1.CopyTo_MethodGroup_NativeArray_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyTo_MethodGroup_NativeArray_1_T]) -> None:...
        @typing.overload
        def __call__(self, array: NativeArray_1[CopyTo_MethodGroup_NativeArray_1_T]) -> None:...

    # Skipped Dispose due to it being static, abstract and generic.

    Dispose : Dispose_MethodGroup[NativeArray_1_T]
    Dispose_MethodGroup_NativeArray_1_T = typing.TypeVar('Dispose_MethodGroup_NativeArray_1_T')
    class Dispose_MethodGroup(typing.Generic[Dispose_MethodGroup_NativeArray_1_T]):
        Dispose_MethodGroup_NativeArray_1_T = NativeArray_1.Dispose_MethodGroup_NativeArray_1_T
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, inputDeps: JobHandle) -> JobHandle:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[NativeArray_1_T]
    Equals_MethodGroup_NativeArray_1_T = typing.TypeVar('Equals_MethodGroup_NativeArray_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_NativeArray_1_T]):
        Equals_MethodGroup_NativeArray_1_T = NativeArray_1.Equals_MethodGroup_NativeArray_1_T
        @typing.overload
        def __call__(self, other: NativeArray_1[Equals_MethodGroup_NativeArray_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Reinterpret due to it being static, abstract and generic.

    Reinterpret : Reinterpret_MethodGroup[NativeArray_1_T]
    Reinterpret_MethodGroup_NativeArray_1_T = typing.TypeVar('Reinterpret_MethodGroup_NativeArray_1_T')
    class Reinterpret_MethodGroup(typing.Generic[Reinterpret_MethodGroup_NativeArray_1_T]):
        Reinterpret_MethodGroup_NativeArray_1_T = NativeArray_1.Reinterpret_MethodGroup_NativeArray_1_T
        def __getitem__(self, t:typing.Type[Reinterpret_1_T1]) -> Reinterpret_1[Reinterpret_MethodGroup_NativeArray_1_T, Reinterpret_1_T1]: ...

        Reinterpret_1_NativeArray_1_T = typing.TypeVar('Reinterpret_1_NativeArray_1_T')
        Reinterpret_1_T1 = typing.TypeVar('Reinterpret_1_T1')
        class Reinterpret_1(typing.Generic[Reinterpret_1_NativeArray_1_T, Reinterpret_1_T1]):
            Reinterpret_1_NativeArray_1_T = NativeArray_1.Reinterpret_MethodGroup.Reinterpret_1_NativeArray_1_T
            Reinterpret_1_U = NativeArray_1.Reinterpret_MethodGroup.Reinterpret_1_T1
            @typing.overload
            def __call__(self) -> NativeArray_1[Reinterpret_1_U]:...
            @typing.overload
            def __call__(self, expectedTypeSize: int) -> NativeArray_1[Reinterpret_1_U]:...


    # Skipped ReinterpretLoad due to it being static, abstract and generic.

    ReinterpretLoad : ReinterpretLoad_MethodGroup[NativeArray_1_T]
    ReinterpretLoad_MethodGroup_NativeArray_1_T = typing.TypeVar('ReinterpretLoad_MethodGroup_NativeArray_1_T')
    class ReinterpretLoad_MethodGroup(typing.Generic[ReinterpretLoad_MethodGroup_NativeArray_1_T]):
        ReinterpretLoad_MethodGroup_NativeArray_1_T = NativeArray_1.ReinterpretLoad_MethodGroup_NativeArray_1_T
        def __getitem__(self, t:typing.Type[ReinterpretLoad_1_T1]) -> ReinterpretLoad_1[ReinterpretLoad_MethodGroup_NativeArray_1_T, ReinterpretLoad_1_T1]: ...

        ReinterpretLoad_1_NativeArray_1_T = typing.TypeVar('ReinterpretLoad_1_NativeArray_1_T')
        ReinterpretLoad_1_T1 = typing.TypeVar('ReinterpretLoad_1_T1')
        class ReinterpretLoad_1(typing.Generic[ReinterpretLoad_1_NativeArray_1_T, ReinterpretLoad_1_T1]):
            ReinterpretLoad_1_NativeArray_1_T = NativeArray_1.ReinterpretLoad_MethodGroup.ReinterpretLoad_1_NativeArray_1_T
            ReinterpretLoad_1_U = NativeArray_1.ReinterpretLoad_MethodGroup.ReinterpretLoad_1_T1
            def __call__(self, sourceIndex: int) -> ReinterpretLoad_1_U:...


    # Skipped ReinterpretStore due to it being static, abstract and generic.

    ReinterpretStore : ReinterpretStore_MethodGroup[NativeArray_1_T]
    ReinterpretStore_MethodGroup_NativeArray_1_T = typing.TypeVar('ReinterpretStore_MethodGroup_NativeArray_1_T')
    class ReinterpretStore_MethodGroup(typing.Generic[ReinterpretStore_MethodGroup_NativeArray_1_T]):
        ReinterpretStore_MethodGroup_NativeArray_1_T = NativeArray_1.ReinterpretStore_MethodGroup_NativeArray_1_T
        def __getitem__(self, t:typing.Type[ReinterpretStore_1_T1]) -> ReinterpretStore_1[ReinterpretStore_MethodGroup_NativeArray_1_T, ReinterpretStore_1_T1]: ...

        ReinterpretStore_1_NativeArray_1_T = typing.TypeVar('ReinterpretStore_1_NativeArray_1_T')
        ReinterpretStore_1_T1 = typing.TypeVar('ReinterpretStore_1_T1')
        class ReinterpretStore_1(typing.Generic[ReinterpretStore_1_NativeArray_1_T, ReinterpretStore_1_T1]):
            ReinterpretStore_1_NativeArray_1_T = NativeArray_1.ReinterpretStore_MethodGroup.ReinterpretStore_1_NativeArray_1_T
            ReinterpretStore_1_U = NativeArray_1.ReinterpretStore_MethodGroup.ReinterpretStore_1_T1
            def __call__(self, destIndex: int, data: ReinterpretStore_1_U) -> None:...



    Enumerator_GenericClasses_NativeArray_1_T = typing.TypeVar('Enumerator_GenericClasses_NativeArray_1_T')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_NativeArray_1_T], abc.ABCMeta):
        Enumerator_GenericClasses_NativeArray_1_T = NativeArray_1.Enumerator_GenericClasses_NativeArray_1_T
        def __call__(self) -> NativeArray_1.Enumerator_1[Enumerator_GenericClasses_NativeArray_1_T]: ...

    Enumerator : Enumerator_GenericClasses[NativeArray_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = NativeArray_1.Enumerator_1_T
        def __init__(self, array: clr.Reference[NativeArray_1[Enumerator_1_T]]) -> None: ...
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...
        def Reset(self) -> None: ...


    ReadOnly_GenericClasses_NativeArray_1_T = typing.TypeVar('ReadOnly_GenericClasses_NativeArray_1_T')
    class ReadOnly_GenericClasses(typing.Generic[ReadOnly_GenericClasses_NativeArray_1_T], abc.ABCMeta):
        ReadOnly_GenericClasses_NativeArray_1_T = NativeArray_1.ReadOnly_GenericClasses_NativeArray_1_T
        def __call__(self) -> NativeArray_1.ReadOnly_1[ReadOnly_GenericClasses_NativeArray_1_T]: ...

    ReadOnly : ReadOnly_GenericClasses[NativeArray_1_T]

    ReadOnly_1_T = typing.TypeVar('ReadOnly_1_T')
    class ReadOnly_1(typing.Generic[ReadOnly_1_T], IEnumerable_1[ReadOnly_1_T]):
        ReadOnly_1_T = NativeArray_1.ReadOnly_1_T
        @property
        def IsCreated(self) -> bool: ...
        @property
        def Item(self) -> ReadOnly_1_T: ...
        @property
        def Length(self) -> int: ...
        def AsReadOnlySpan(self) -> ReadOnlySpan_1[ReadOnly_1_T]: ...
        def GetEnumerator(self) -> NativeArray_1.ReadOnly_1.Enumerator_1[ReadOnly_1_T]: ...
        # Operator not supported op_Implicit(source: ReadOnly&)
        def ToArray(self) -> Array_1[ReadOnly_1_T]: ...
        # Skipped CopyTo due to it being static, abstract and generic.

        CopyTo : CopyTo_MethodGroup[ReadOnly_1_T]
        CopyTo_MethodGroup_ReadOnly_1_T = typing.TypeVar('CopyTo_MethodGroup_ReadOnly_1_T')
        class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_ReadOnly_1_T]):
            CopyTo_MethodGroup_ReadOnly_1_T = NativeArray_1.ReadOnly_1.CopyTo_MethodGroup_ReadOnly_1_T
            @typing.overload
            def __call__(self, array: Array_1[CopyTo_MethodGroup_ReadOnly_1_T]) -> None:...
            @typing.overload
            def __call__(self, array: NativeArray_1[CopyTo_MethodGroup_ReadOnly_1_T]) -> None:...

        # Skipped Reinterpret due to it being static, abstract and generic.

        Reinterpret : Reinterpret_MethodGroup[ReadOnly_1_T]
        Reinterpret_MethodGroup_ReadOnly_1_T = typing.TypeVar('Reinterpret_MethodGroup_ReadOnly_1_T')
        class Reinterpret_MethodGroup(typing.Generic[Reinterpret_MethodGroup_ReadOnly_1_T]):
            Reinterpret_MethodGroup_ReadOnly_1_T = NativeArray_1.ReadOnly_1.Reinterpret_MethodGroup_ReadOnly_1_T
            def __getitem__(self, t:typing.Type[Reinterpret_1_T1]) -> Reinterpret_1[Reinterpret_MethodGroup_ReadOnly_1_T, Reinterpret_1_T1]: ...

            Reinterpret_1_ReadOnly_1_T = typing.TypeVar('Reinterpret_1_ReadOnly_1_T')
            Reinterpret_1_T1 = typing.TypeVar('Reinterpret_1_T1')
            class Reinterpret_1(typing.Generic[Reinterpret_1_ReadOnly_1_T, Reinterpret_1_T1]):
                Reinterpret_1_ReadOnly_1_T = NativeArray_1.ReadOnly_1.Reinterpret_MethodGroup.Reinterpret_1_ReadOnly_1_T
                Reinterpret_1_U = NativeArray_1.ReadOnly_1.Reinterpret_MethodGroup.Reinterpret_1_T1
                def __call__(self) -> NativeArray_1.ReadOnly_1[Reinterpret_1_U]:...



        Enumerator_GenericClasses_ReadOnly_1_T = typing.TypeVar('Enumerator_GenericClasses_ReadOnly_1_T')
        class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_ReadOnly_1_T], abc.ABCMeta):
            Enumerator_GenericClasses_ReadOnly_1_T = NativeArray_1.ReadOnly_1.Enumerator_GenericClasses_ReadOnly_1_T
            def __call__(self) -> NativeArray_1.ReadOnly_1.Enumerator_1[Enumerator_GenericClasses_ReadOnly_1_T]: ...

        Enumerator : Enumerator_GenericClasses[ReadOnly_1_T]

        Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
        class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
            Enumerator_1_T = NativeArray_1.ReadOnly_1.Enumerator_1_T
            def __init__(self, array: clr.Reference[NativeArray_1.ReadOnly_1[Enumerator_1_T]]) -> None: ...
            @property
            def Current(self) -> Enumerator_1_T: ...
            def Dispose(self) -> None: ...
            def MoveNext(self) -> bool: ...
            def Reset(self) -> None: ...




class NativeArrayOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    UninitializedMemory : NativeArrayOptions # 0
    ClearMemory : NativeArrayOptions # 1


class NativeDisableParallelForRestrictionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeFixedLengthAttribute(Attribute):
    def __init__(self, fixedLength: int) -> None: ...
    FixedLength : int
    @property
    def TypeId(self) -> typing.Any: ...


class NativeLeakDetection(abc.ABC):
    @classmethod
    @property
    def Mode(cls) -> NativeLeakDetectionMode: ...
    @classmethod
    @Mode.setter
    def Mode(cls, value: NativeLeakDetectionMode) -> NativeLeakDetectionMode: ...


class NativeLeakDetectionMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Disabled : NativeLeakDetectionMode # 1
    Enabled : NativeLeakDetectionMode # 2
    EnabledWithStackTrace : NativeLeakDetectionMode # 3


class NativeMatchesParallelForLengthAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeSlice_GenericClasses(abc.ABCMeta):
    Generic_NativeSlice_GenericClasses_NativeSlice_1_T = typing.TypeVar('Generic_NativeSlice_GenericClasses_NativeSlice_1_T')
    def __getitem__(self, types : typing.Type[Generic_NativeSlice_GenericClasses_NativeSlice_1_T]) -> typing.Type[NativeSlice_1[Generic_NativeSlice_GenericClasses_NativeSlice_1_T]]: ...

NativeSlice : NativeSlice_GenericClasses

NativeSlice_1_T = typing.TypeVar('NativeSlice_1_T')
class NativeSlice_1(typing.Generic[NativeSlice_1_T], IEnumerable_1[NativeSlice_1_T], IEquatable_1[NativeSlice_1[NativeSlice_1_T]]):
    @typing.overload
    def __init__(self, array: NativeArray_1[NativeSlice_1_T]) -> None: ...
    @typing.overload
    def __init__(self, array: NativeArray_1[NativeSlice_1_T], start: int) -> None: ...
    @typing.overload
    def __init__(self, array: NativeArray_1[NativeSlice_1_T], start: int, length: int) -> None: ...
    @typing.overload
    def __init__(self, slice: NativeSlice_1[NativeSlice_1_T], start: int) -> None: ...
    @typing.overload
    def __init__(self, slice: NativeSlice_1[NativeSlice_1_T], start: int, length: int) -> None: ...
    @property
    def Item(self) -> NativeSlice_1_T: ...
    @Item.setter
    def Item(self, value: NativeSlice_1_T) -> NativeSlice_1_T: ...
    @property
    def Length(self) -> int: ...
    @property
    def Stride(self) -> int: ...
    def GetEnumerator(self) -> NativeSlice_1.Enumerator_1[NativeSlice_1_T]: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: NativeSlice_1[NativeSlice_1_T], right: NativeSlice_1[NativeSlice_1_T]) -> bool: ...
    # Operator not supported op_Implicit(array: NativeArray`1)
    def __ne__(self, left: NativeSlice_1[NativeSlice_1_T], right: NativeSlice_1[NativeSlice_1_T]) -> bool: ...
    def ToArray(self) -> Array_1[NativeSlice_1_T]: ...
    # Skipped CopyFrom due to it being static, abstract and generic.

    CopyFrom : CopyFrom_MethodGroup[NativeSlice_1_T]
    CopyFrom_MethodGroup_NativeSlice_1_T = typing.TypeVar('CopyFrom_MethodGroup_NativeSlice_1_T')
    class CopyFrom_MethodGroup(typing.Generic[CopyFrom_MethodGroup_NativeSlice_1_T]):
        CopyFrom_MethodGroup_NativeSlice_1_T = NativeSlice_1.CopyFrom_MethodGroup_NativeSlice_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyFrom_MethodGroup_NativeSlice_1_T]) -> None:...
        @typing.overload
        def __call__(self, slice: NativeSlice_1[CopyFrom_MethodGroup_NativeSlice_1_T]) -> None:...

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo : CopyTo_MethodGroup[NativeSlice_1_T]
    CopyTo_MethodGroup_NativeSlice_1_T = typing.TypeVar('CopyTo_MethodGroup_NativeSlice_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_NativeSlice_1_T]):
        CopyTo_MethodGroup_NativeSlice_1_T = NativeSlice_1.CopyTo_MethodGroup_NativeSlice_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyTo_MethodGroup_NativeSlice_1_T]) -> None:...
        @typing.overload
        def __call__(self, array: NativeArray_1[CopyTo_MethodGroup_NativeSlice_1_T]) -> None:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup[NativeSlice_1_T]
    Equals_MethodGroup_NativeSlice_1_T = typing.TypeVar('Equals_MethodGroup_NativeSlice_1_T')
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_NativeSlice_1_T]):
        Equals_MethodGroup_NativeSlice_1_T = NativeSlice_1.Equals_MethodGroup_NativeSlice_1_T
        @typing.overload
        def __call__(self, other: NativeSlice_1[Equals_MethodGroup_NativeSlice_1_T]) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped SliceConvert due to it being static, abstract and generic.

    SliceConvert : SliceConvert_MethodGroup[NativeSlice_1_T]
    SliceConvert_MethodGroup_NativeSlice_1_T = typing.TypeVar('SliceConvert_MethodGroup_NativeSlice_1_T')
    class SliceConvert_MethodGroup(typing.Generic[SliceConvert_MethodGroup_NativeSlice_1_T]):
        SliceConvert_MethodGroup_NativeSlice_1_T = NativeSlice_1.SliceConvert_MethodGroup_NativeSlice_1_T
        def __getitem__(self, t:typing.Type[SliceConvert_1_T1]) -> SliceConvert_1[SliceConvert_MethodGroup_NativeSlice_1_T, SliceConvert_1_T1]: ...

        SliceConvert_1_NativeSlice_1_T = typing.TypeVar('SliceConvert_1_NativeSlice_1_T')
        SliceConvert_1_T1 = typing.TypeVar('SliceConvert_1_T1')
        class SliceConvert_1(typing.Generic[SliceConvert_1_NativeSlice_1_T, SliceConvert_1_T1]):
            SliceConvert_1_NativeSlice_1_T = NativeSlice_1.SliceConvert_MethodGroup.SliceConvert_1_NativeSlice_1_T
            SliceConvert_1_U = NativeSlice_1.SliceConvert_MethodGroup.SliceConvert_1_T1
            def __call__(self) -> NativeSlice_1[SliceConvert_1_U]:...


    # Skipped SliceWithStride due to it being static, abstract and generic.

    SliceWithStride : SliceWithStride_MethodGroup[NativeSlice_1_T]
    SliceWithStride_MethodGroup_NativeSlice_1_T = typing.TypeVar('SliceWithStride_MethodGroup_NativeSlice_1_T')
    class SliceWithStride_MethodGroup(typing.Generic[SliceWithStride_MethodGroup_NativeSlice_1_T]):
        SliceWithStride_MethodGroup_NativeSlice_1_T = NativeSlice_1.SliceWithStride_MethodGroup_NativeSlice_1_T
        def __getitem__(self, t:typing.Type[SliceWithStride_1_T1]) -> SliceWithStride_1[SliceWithStride_MethodGroup_NativeSlice_1_T, SliceWithStride_1_T1]: ...

        SliceWithStride_1_NativeSlice_1_T = typing.TypeVar('SliceWithStride_1_NativeSlice_1_T')
        SliceWithStride_1_T1 = typing.TypeVar('SliceWithStride_1_T1')
        class SliceWithStride_1(typing.Generic[SliceWithStride_1_NativeSlice_1_T, SliceWithStride_1_T1]):
            SliceWithStride_1_NativeSlice_1_T = NativeSlice_1.SliceWithStride_MethodGroup.SliceWithStride_1_NativeSlice_1_T
            SliceWithStride_1_U = NativeSlice_1.SliceWithStride_MethodGroup.SliceWithStride_1_T1
            @typing.overload
            def __call__(self) -> NativeSlice_1[SliceWithStride_1_U]:...
            @typing.overload
            def __call__(self, offset: int) -> NativeSlice_1[SliceWithStride_1_U]:...



    Enumerator_GenericClasses_NativeSlice_1_T = typing.TypeVar('Enumerator_GenericClasses_NativeSlice_1_T')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_NativeSlice_1_T], abc.ABCMeta):
        Enumerator_GenericClasses_NativeSlice_1_T = NativeSlice_1.Enumerator_GenericClasses_NativeSlice_1_T
        def __call__(self) -> NativeSlice_1.Enumerator_1[Enumerator_GenericClasses_NativeSlice_1_T]: ...

    Enumerator : Enumerator_GenericClasses[NativeSlice_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = NativeSlice_1.Enumerator_1_T
        def __init__(self, array: clr.Reference[NativeSlice_1[Enumerator_1_T]]) -> None: ...
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...
        def Reset(self) -> None: ...



class NativeSliceExtensions(abc.ABC):
    # Skipped Slice due to it being static, abstract and generic.

    Slice : Slice_MethodGroup
    class Slice_MethodGroup:
        def __getitem__(self, t:typing.Type[Slice_1_T1]) -> Slice_1[Slice_1_T1]: ...

        Slice_1_T1 = typing.TypeVar('Slice_1_T1')
        class Slice_1(typing.Generic[Slice_1_T1]):
            Slice_1_T = NativeSliceExtensions.Slice_MethodGroup.Slice_1_T1
            @typing.overload
            def __call__(self, thisArray: NativeArray_1[Slice_1_T]) -> NativeSlice_1[Slice_1_T]:...
            @typing.overload
            def __call__(self, thisSlice: NativeSlice_1[Slice_1_T]) -> NativeSlice_1[Slice_1_T]:...
            @typing.overload
            def __call__(self, thisArray: NativeArray_1[Slice_1_T], start: int) -> NativeSlice_1[Slice_1_T]:...
            @typing.overload
            def __call__(self, thisSlice: NativeSlice_1[Slice_1_T], start: int) -> NativeSlice_1[Slice_1_T]:...
            @typing.overload
            def __call__(self, thisArray: NativeArray_1[Slice_1_T], start: int, length: int) -> NativeSlice_1[Slice_1_T]:...
            @typing.overload
            def __call__(self, thisSlice: NativeSlice_1[Slice_1_T], start: int, length: int) -> NativeSlice_1[Slice_1_T]:...




class ReadOnlyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class WriteOnlyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

