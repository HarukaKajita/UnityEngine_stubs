import typing, clr, abc
from Unity.Jobs import JobHandle
from Unity.Collections import Allocator, NativeArray_1, NativeSlice_1, NativeLeakDetectionMode
from System import Attribute, Array
from System.Reflection import FieldInfo

class AtomicSafetyErrorType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Deallocated : AtomicSafetyErrorType # 0
    DeallocatedFromJob : AtomicSafetyErrorType # 1
    NotAllocatedFromJob : AtomicSafetyErrorType # 2


class AtomicSafetyHandle:
    @staticmethod
    def CheckDeallocateAndThrow(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def CheckExistsAndThrow(handle: clr.Reference[AtomicSafetyHandle]) -> None: ...
    @staticmethod
    def CheckGetSecondaryDataPointerAndThrow(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def CheckReadAndThrow(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def CheckWriteAndBumpSecondaryVersion(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def CheckWriteAndThrow(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def Create() -> AtomicSafetyHandle: ...
    @staticmethod
    def EnforceAllBufferJobsHaveCompleted(handle: AtomicSafetyHandle) -> EnforceJobResult: ...
    @staticmethod
    def EnforceAllBufferJobsHaveCompletedAndDisableReadWrite(handle: AtomicSafetyHandle) -> EnforceJobResult: ...
    @staticmethod
    def EnforceAllBufferJobsHaveCompletedAndRelease(handle: AtomicSafetyHandle) -> EnforceJobResult: ...
    @staticmethod
    def GetAllowReadOrWriteAccess(handle: AtomicSafetyHandle) -> bool: ...
    @staticmethod
    def GetNestedContainer(handle: AtomicSafetyHandle) -> bool: ...
    @staticmethod
    def GetReaderArray(handle: AtomicSafetyHandle, maxCount: int, output: int) -> int: ...
    @staticmethod
    def GetReaderName(handle: AtomicSafetyHandle, readerIndex: int) -> str: ...
    @staticmethod
    def GetTempMemoryHandle() -> AtomicSafetyHandle: ...
    @staticmethod
    def GetTempUnsafePtrSliceHandle() -> AtomicSafetyHandle: ...
    @staticmethod
    def GetWriter(handle: AtomicSafetyHandle) -> JobHandle: ...
    @staticmethod
    def GetWriterName(handle: AtomicSafetyHandle) -> str: ...
    @staticmethod
    def IsDefaultValue(handle: clr.Reference[AtomicSafetyHandle]) -> bool: ...
    @staticmethod
    def IsHandleValid(handle: clr.Reference[AtomicSafetyHandle]) -> bool: ...
    @staticmethod
    def IsTempMemoryHandle(handle: AtomicSafetyHandle) -> bool: ...
    @staticmethod
    def IsValidNonDefaultHandle(handle: clr.Reference[AtomicSafetyHandle]) -> bool: ...
    @staticmethod
    def PrepareUndisposable(handle: clr.Reference[AtomicSafetyHandle]) -> None: ...
    @staticmethod
    def Release(handle: AtomicSafetyHandle) -> None: ...
    @staticmethod
    def SetAllowReadOrWriteAccess(handle: AtomicSafetyHandle, allowReadWriteAccess: bool) -> None: ...
    @staticmethod
    def SetAllowSecondaryVersionWriting(handle: AtomicSafetyHandle, allowWriting: bool) -> None: ...
    @staticmethod
    def SetBumpSecondaryVersionOnScheduleWrite(handle: AtomicSafetyHandle, value: bool) -> None: ...
    @staticmethod
    def SetCustomErrorMessage(staticSafetyId: int, errorType: AtomicSafetyErrorType, messageBytes: clr.Reference[int], byteCount: int) -> None: ...
    @staticmethod
    def SetNestedContainer(handle: AtomicSafetyHandle, isNestedContainer: bool) -> None: ...
    @staticmethod
    def SetStaticSafetyId(handle: clr.Reference[AtomicSafetyHandle], staticSafetyId: int) -> None: ...
    @staticmethod
    def UseSecondaryVersion(handle: clr.Reference[AtomicSafetyHandle]) -> None: ...
    @staticmethod
    def ValidateNonDefaultHandle(handle: clr.Reference[AtomicSafetyHandle]) -> None: ...
    # Skipped NewStaticSafetyId due to it being static, abstract and generic.

    NewStaticSafetyId : NewStaticSafetyId_MethodGroup
    class NewStaticSafetyId_MethodGroup:
        def __getitem__(self, t:typing.Type[NewStaticSafetyId_1_T1]) -> NewStaticSafetyId_1[NewStaticSafetyId_1_T1]: ...

        NewStaticSafetyId_1_T1 = typing.TypeVar('NewStaticSafetyId_1_T1')
        class NewStaticSafetyId_1(typing.Generic[NewStaticSafetyId_1_T1]):
            NewStaticSafetyId_1_T = AtomicSafetyHandle.NewStaticSafetyId_MethodGroup.NewStaticSafetyId_1_T1
            def __call__(self) -> int:...

        def __call__(self, ownerTypeNameBytes: clr.Reference[int], byteCount: int) -> int:...



class DisposeSentinel:
    @staticmethod
    def Clear(sentinel: clr.Reference[DisposeSentinel]) -> None: ...
    @staticmethod
    def Create(safety: clr.Reference[AtomicSafetyHandle], sentinel: clr.Reference[DisposeSentinel], callSiteStackDepth: int, allocator: Allocator) -> None: ...
    @staticmethod
    def Dispose(safety: clr.Reference[AtomicSafetyHandle], sentinel: clr.Reference[DisposeSentinel]) -> None: ...


class EnforceJobResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    AllJobsAlreadySynced : EnforceJobResult # 0
    DidSyncRunningJobs : EnforceJobResult # 1
    HandleWasAlreadyDeallocated : EnforceJobResult # 2


class NativeArrayUnsafeUtility(abc.ABC):
    # Skipped ConvertExistingDataToNativeArray due to it being static, abstract and generic.

    ConvertExistingDataToNativeArray : ConvertExistingDataToNativeArray_MethodGroup
    class ConvertExistingDataToNativeArray_MethodGroup:
        def __getitem__(self, t:typing.Type[ConvertExistingDataToNativeArray_1_T1]) -> ConvertExistingDataToNativeArray_1[ConvertExistingDataToNativeArray_1_T1]: ...

        ConvertExistingDataToNativeArray_1_T1 = typing.TypeVar('ConvertExistingDataToNativeArray_1_T1')
        class ConvertExistingDataToNativeArray_1(typing.Generic[ConvertExistingDataToNativeArray_1_T1]):
            ConvertExistingDataToNativeArray_1_T = NativeArrayUnsafeUtility.ConvertExistingDataToNativeArray_MethodGroup.ConvertExistingDataToNativeArray_1_T1
            def __call__(self, dataPointer: clr.Reference[None], length: int, allocator: Allocator) -> NativeArray_1[ConvertExistingDataToNativeArray_1_T]:...


    # Skipped GetAtomicSafetyHandle due to it being static, abstract and generic.

    GetAtomicSafetyHandle : GetAtomicSafetyHandle_MethodGroup
    class GetAtomicSafetyHandle_MethodGroup:
        def __getitem__(self, t:typing.Type[GetAtomicSafetyHandle_1_T1]) -> GetAtomicSafetyHandle_1[GetAtomicSafetyHandle_1_T1]: ...

        GetAtomicSafetyHandle_1_T1 = typing.TypeVar('GetAtomicSafetyHandle_1_T1')
        class GetAtomicSafetyHandle_1(typing.Generic[GetAtomicSafetyHandle_1_T1]):
            GetAtomicSafetyHandle_1_T = NativeArrayUnsafeUtility.GetAtomicSafetyHandle_MethodGroup.GetAtomicSafetyHandle_1_T1
            def __call__(self, array: NativeArray_1[GetAtomicSafetyHandle_1_T]) -> AtomicSafetyHandle:...


    # Skipped GetUnsafeBufferPointerWithoutChecks due to it being static, abstract and generic.

    GetUnsafeBufferPointerWithoutChecks : GetUnsafeBufferPointerWithoutChecks_MethodGroup
    class GetUnsafeBufferPointerWithoutChecks_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUnsafeBufferPointerWithoutChecks_1_T1]) -> GetUnsafeBufferPointerWithoutChecks_1[GetUnsafeBufferPointerWithoutChecks_1_T1]: ...

        GetUnsafeBufferPointerWithoutChecks_1_T1 = typing.TypeVar('GetUnsafeBufferPointerWithoutChecks_1_T1')
        class GetUnsafeBufferPointerWithoutChecks_1(typing.Generic[GetUnsafeBufferPointerWithoutChecks_1_T1]):
            GetUnsafeBufferPointerWithoutChecks_1_T = NativeArrayUnsafeUtility.GetUnsafeBufferPointerWithoutChecks_MethodGroup.GetUnsafeBufferPointerWithoutChecks_1_T1
            def __call__(self, nativeArray: NativeArray_1[GetUnsafeBufferPointerWithoutChecks_1_T]) -> clr.Reference[None]:...


    # Skipped GetUnsafePtr due to it being static, abstract and generic.

    GetUnsafePtr : GetUnsafePtr_MethodGroup
    class GetUnsafePtr_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUnsafePtr_1_T1]) -> GetUnsafePtr_1[GetUnsafePtr_1_T1]: ...

        GetUnsafePtr_1_T1 = typing.TypeVar('GetUnsafePtr_1_T1')
        class GetUnsafePtr_1(typing.Generic[GetUnsafePtr_1_T1]):
            GetUnsafePtr_1_T = NativeArrayUnsafeUtility.GetUnsafePtr_MethodGroup.GetUnsafePtr_1_T1
            def __call__(self, nativeArray: NativeArray_1[GetUnsafePtr_1_T]) -> clr.Reference[None]:...


    # Skipped GetUnsafeReadOnlyPtr due to it being static, abstract and generic.

    GetUnsafeReadOnlyPtr : GetUnsafeReadOnlyPtr_MethodGroup
    class GetUnsafeReadOnlyPtr_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUnsafeReadOnlyPtr_1_T1]) -> GetUnsafeReadOnlyPtr_1[GetUnsafeReadOnlyPtr_1_T1]: ...

        GetUnsafeReadOnlyPtr_1_T1 = typing.TypeVar('GetUnsafeReadOnlyPtr_1_T1')
        class GetUnsafeReadOnlyPtr_1(typing.Generic[GetUnsafeReadOnlyPtr_1_T1]):
            GetUnsafeReadOnlyPtr_1_T = NativeArrayUnsafeUtility.GetUnsafeReadOnlyPtr_MethodGroup.GetUnsafeReadOnlyPtr_1_T1
            @typing.overload
            def __call__(self, nativeArray: NativeArray_1[GetUnsafeReadOnlyPtr_1_T]) -> clr.Reference[None]:...
            @typing.overload
            def __call__(self, nativeArray: NativeArray_1.ReadOnly_1[GetUnsafeReadOnlyPtr_1_T]) -> clr.Reference[None]:...


    # Skipped SetAtomicSafetyHandle due to it being static, abstract and generic.

    SetAtomicSafetyHandle : SetAtomicSafetyHandle_MethodGroup
    class SetAtomicSafetyHandle_MethodGroup:
        def __getitem__(self, t:typing.Type[SetAtomicSafetyHandle_1_T1]) -> SetAtomicSafetyHandle_1[SetAtomicSafetyHandle_1_T1]: ...

        SetAtomicSafetyHandle_1_T1 = typing.TypeVar('SetAtomicSafetyHandle_1_T1')
        class SetAtomicSafetyHandle_1(typing.Generic[SetAtomicSafetyHandle_1_T1]):
            SetAtomicSafetyHandle_1_T = NativeArrayUnsafeUtility.SetAtomicSafetyHandle_MethodGroup.SetAtomicSafetyHandle_1_T1
            def __call__(self, array: clr.Reference[NativeArray_1[SetAtomicSafetyHandle_1_T]], safety: AtomicSafetyHandle) -> None:...




class NativeContainerAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerIsAtomicWriteOnlyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerIsReadOnlyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerNeedsThreadIndexAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerSupportsDeallocateOnJobCompletionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerSupportsDeferredConvertListToArray(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeContainerSupportsMinMaxWriteRestrictionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeDisableContainerSafetyRestrictionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeDisableUnsafePtrRestrictionAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeSetClassTypeToNullOnScheduleAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeSetThreadIndexAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class NativeSliceUnsafeUtility(abc.ABC):
    # Skipped ConvertExistingDataToNativeSlice due to it being static, abstract and generic.

    ConvertExistingDataToNativeSlice : ConvertExistingDataToNativeSlice_MethodGroup
    class ConvertExistingDataToNativeSlice_MethodGroup:
        def __getitem__(self, t:typing.Type[ConvertExistingDataToNativeSlice_1_T1]) -> ConvertExistingDataToNativeSlice_1[ConvertExistingDataToNativeSlice_1_T1]: ...

        ConvertExistingDataToNativeSlice_1_T1 = typing.TypeVar('ConvertExistingDataToNativeSlice_1_T1')
        class ConvertExistingDataToNativeSlice_1(typing.Generic[ConvertExistingDataToNativeSlice_1_T1]):
            ConvertExistingDataToNativeSlice_1_T = NativeSliceUnsafeUtility.ConvertExistingDataToNativeSlice_MethodGroup.ConvertExistingDataToNativeSlice_1_T1
            def __call__(self, dataPointer: clr.Reference[None], stride: int, length: int) -> NativeSlice_1[ConvertExistingDataToNativeSlice_1_T]:...


    # Skipped GetAtomicSafetyHandle due to it being static, abstract and generic.

    GetAtomicSafetyHandle : GetAtomicSafetyHandle_MethodGroup
    class GetAtomicSafetyHandle_MethodGroup:
        def __getitem__(self, t:typing.Type[GetAtomicSafetyHandle_1_T1]) -> GetAtomicSafetyHandle_1[GetAtomicSafetyHandle_1_T1]: ...

        GetAtomicSafetyHandle_1_T1 = typing.TypeVar('GetAtomicSafetyHandle_1_T1')
        class GetAtomicSafetyHandle_1(typing.Generic[GetAtomicSafetyHandle_1_T1]):
            GetAtomicSafetyHandle_1_T = NativeSliceUnsafeUtility.GetAtomicSafetyHandle_MethodGroup.GetAtomicSafetyHandle_1_T1
            def __call__(self, slice: NativeSlice_1[GetAtomicSafetyHandle_1_T]) -> AtomicSafetyHandle:...


    # Skipped GetUnsafePtr due to it being static, abstract and generic.

    GetUnsafePtr : GetUnsafePtr_MethodGroup
    class GetUnsafePtr_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUnsafePtr_1_T1]) -> GetUnsafePtr_1[GetUnsafePtr_1_T1]: ...

        GetUnsafePtr_1_T1 = typing.TypeVar('GetUnsafePtr_1_T1')
        class GetUnsafePtr_1(typing.Generic[GetUnsafePtr_1_T1]):
            GetUnsafePtr_1_T = NativeSliceUnsafeUtility.GetUnsafePtr_MethodGroup.GetUnsafePtr_1_T1
            def __call__(self, nativeSlice: NativeSlice_1[GetUnsafePtr_1_T]) -> clr.Reference[None]:...


    # Skipped GetUnsafeReadOnlyPtr due to it being static, abstract and generic.

    GetUnsafeReadOnlyPtr : GetUnsafeReadOnlyPtr_MethodGroup
    class GetUnsafeReadOnlyPtr_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUnsafeReadOnlyPtr_1_T1]) -> GetUnsafeReadOnlyPtr_1[GetUnsafeReadOnlyPtr_1_T1]: ...

        GetUnsafeReadOnlyPtr_1_T1 = typing.TypeVar('GetUnsafeReadOnlyPtr_1_T1')
        class GetUnsafeReadOnlyPtr_1(typing.Generic[GetUnsafeReadOnlyPtr_1_T1]):
            GetUnsafeReadOnlyPtr_1_T = NativeSliceUnsafeUtility.GetUnsafeReadOnlyPtr_MethodGroup.GetUnsafeReadOnlyPtr_1_T1
            def __call__(self, nativeSlice: NativeSlice_1[GetUnsafeReadOnlyPtr_1_T]) -> clr.Reference[None]:...


    # Skipped SetAtomicSafetyHandle due to it being static, abstract and generic.

    SetAtomicSafetyHandle : SetAtomicSafetyHandle_MethodGroup
    class SetAtomicSafetyHandle_MethodGroup:
        def __getitem__(self, t:typing.Type[SetAtomicSafetyHandle_1_T1]) -> SetAtomicSafetyHandle_1[SetAtomicSafetyHandle_1_T1]: ...

        SetAtomicSafetyHandle_1_T1 = typing.TypeVar('SetAtomicSafetyHandle_1_T1')
        class SetAtomicSafetyHandle_1(typing.Generic[SetAtomicSafetyHandle_1_T1]):
            SetAtomicSafetyHandle_1_T = NativeSliceUnsafeUtility.SetAtomicSafetyHandle_MethodGroup.SetAtomicSafetyHandle_1_T1
            def __call__(self, slice: clr.Reference[NativeSlice_1[SetAtomicSafetyHandle_1_T]], safety: AtomicSafetyHandle) -> None:...




class UnsafeUtility(abc.ABC):
    @staticmethod
    def CheckForLeaks() -> int: ...
    @staticmethod
    def CopyObjectAddressToPtr(target: typing.Any, dstPtr: clr.Reference[None]) -> None: ...
    @staticmethod
    def ForgiveLeaks() -> int: ...
    @staticmethod
    def Free(memory: clr.Reference[None], allocator: Allocator) -> None: ...
    @staticmethod
    def FreeTracked(memory: clr.Reference[None], allocator: Allocator) -> None: ...
    @staticmethod
    def GetFieldOffset(field: FieldInfo) -> int: ...
    @staticmethod
    def GetLeakDetectionMode() -> NativeLeakDetectionMode: ...
    @staticmethod
    def IsValidAllocator(allocator: Allocator) -> bool: ...
    @staticmethod
    def Malloc(size: int, alignment: int, allocator: Allocator) -> clr.Reference[None]: ...
    @staticmethod
    def MallocTracked(size: int, alignment: int, allocator: Allocator, callstacksToSkip: int) -> clr.Reference[None]: ...
    @staticmethod
    def MemClear(destination: clr.Reference[None], size: int) -> None: ...
    @staticmethod
    def MemCmp(ptr1: clr.Reference[None], ptr2: clr.Reference[None], size: int) -> int: ...
    @staticmethod
    def MemCpy(destination: clr.Reference[None], source: clr.Reference[None], size: int) -> None: ...
    @staticmethod
    def MemCpyReplicate(destination: clr.Reference[None], source: clr.Reference[None], size: int, count: int) -> None: ...
    @staticmethod
    def MemCpyStride(destination: clr.Reference[None], destinationStride: int, source: clr.Reference[None], sourceStride: int, elementSize: int, count: int) -> None: ...
    @staticmethod
    def MemMove(destination: clr.Reference[None], source: clr.Reference[None], size: int) -> None: ...
    @staticmethod
    def MemSet(destination: clr.Reference[None], value: int, size: int) -> None: ...
    @staticmethod
    def PinGCArrayAndGetDataAddress(target: Array, gcHandle: clr.Reference[int]) -> clr.Reference[None]: ...
    @staticmethod
    def PinGCObjectAndGetAddress(target: typing.Any, gcHandle: clr.Reference[int]) -> clr.Reference[None]: ...
    @staticmethod
    def ReleaseGCObject(gcHandle: int) -> None: ...
    @staticmethod
    def SetLeakDetectionMode(value: NativeLeakDetectionMode) -> None: ...
    # Skipped AddressOf due to it being static, abstract and generic.

    AddressOf : AddressOf_MethodGroup
    class AddressOf_MethodGroup:
        def __getitem__(self, t:typing.Type[AddressOf_1_T1]) -> AddressOf_1[AddressOf_1_T1]: ...

        AddressOf_1_T1 = typing.TypeVar('AddressOf_1_T1')
        class AddressOf_1(typing.Generic[AddressOf_1_T1]):
            AddressOf_1_T = UnsafeUtility.AddressOf_MethodGroup.AddressOf_1_T1
            def __call__(self, output: clr.Reference[AddressOf_1_T]) -> clr.Reference[None]:...


    # Skipped AlignOf due to it being static, abstract and generic.

    AlignOf : AlignOf_MethodGroup
    class AlignOf_MethodGroup:
        def __getitem__(self, t:typing.Type[AlignOf_1_T1]) -> AlignOf_1[AlignOf_1_T1]: ...

        AlignOf_1_T1 = typing.TypeVar('AlignOf_1_T1')
        class AlignOf_1(typing.Generic[AlignOf_1_T1]):
            AlignOf_1_T = UnsafeUtility.AlignOf_MethodGroup.AlignOf_1_T1
            def __call__(self) -> int:...


    # Skipped ArrayElementAsRef due to it being static, abstract and generic.

    ArrayElementAsRef : ArrayElementAsRef_MethodGroup
    class ArrayElementAsRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ArrayElementAsRef_1_T1]) -> ArrayElementAsRef_1[ArrayElementAsRef_1_T1]: ...

        ArrayElementAsRef_1_T1 = typing.TypeVar('ArrayElementAsRef_1_T1')
        class ArrayElementAsRef_1(typing.Generic[ArrayElementAsRef_1_T1]):
            ArrayElementAsRef_1_T = UnsafeUtility.ArrayElementAsRef_MethodGroup.ArrayElementAsRef_1_T1
            def __call__(self, ptr: clr.Reference[None], index: int) -> clr.Reference[ArrayElementAsRef_1_T]:...


    # Skipped As due to it being static, abstract and generic.

    As : As_MethodGroup
    class As_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[As_2_T1], typing.Type[As_2_T2]]) -> As_2[As_2_T1, As_2_T2]: ...

        As_2_T1 = typing.TypeVar('As_2_T1')
        As_2_T2 = typing.TypeVar('As_2_T2')
        class As_2(typing.Generic[As_2_T1, As_2_T2]):
            As_2_U = UnsafeUtility.As_MethodGroup.As_2_T1
            As_2_T = UnsafeUtility.As_MethodGroup.As_2_T2
            def __call__(self, from_: clr.Reference[As_2_U]) -> clr.Reference[As_2_T]:...


    # Skipped AsRef due to it being static, abstract and generic.

    AsRef : AsRef_MethodGroup
    class AsRef_MethodGroup:
        def __getitem__(self, t:typing.Type[AsRef_1_T1]) -> AsRef_1[AsRef_1_T1]: ...

        AsRef_1_T1 = typing.TypeVar('AsRef_1_T1')
        class AsRef_1(typing.Generic[AsRef_1_T1]):
            AsRef_1_T = UnsafeUtility.AsRef_MethodGroup.AsRef_1_T1
            def __call__(self, ptr: clr.Reference[None]) -> clr.Reference[AsRef_1_T]:...


    # Skipped CopyPtrToStructure due to it being static, abstract and generic.

    CopyPtrToStructure : CopyPtrToStructure_MethodGroup
    class CopyPtrToStructure_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyPtrToStructure_1_T1]) -> CopyPtrToStructure_1[CopyPtrToStructure_1_T1]: ...

        CopyPtrToStructure_1_T1 = typing.TypeVar('CopyPtrToStructure_1_T1')
        class CopyPtrToStructure_1(typing.Generic[CopyPtrToStructure_1_T1]):
            CopyPtrToStructure_1_T = UnsafeUtility.CopyPtrToStructure_MethodGroup.CopyPtrToStructure_1_T1
            def __call__(self, ptr: clr.Reference[None], output: clr.Reference[CopyPtrToStructure_1_T]) -> None:...


    # Skipped CopyStructureToPtr due to it being static, abstract and generic.

    CopyStructureToPtr : CopyStructureToPtr_MethodGroup
    class CopyStructureToPtr_MethodGroup:
        def __getitem__(self, t:typing.Type[CopyStructureToPtr_1_T1]) -> CopyStructureToPtr_1[CopyStructureToPtr_1_T1]: ...

        CopyStructureToPtr_1_T1 = typing.TypeVar('CopyStructureToPtr_1_T1')
        class CopyStructureToPtr_1(typing.Generic[CopyStructureToPtr_1_T1]):
            CopyStructureToPtr_1_T = UnsafeUtility.CopyStructureToPtr_MethodGroup.CopyStructureToPtr_1_T1
            def __call__(self, input: clr.Reference[CopyStructureToPtr_1_T], ptr: clr.Reference[None]) -> None:...


    # Skipped EnumEquals due to it being static, abstract and generic.

    EnumEquals : EnumEquals_MethodGroup
    class EnumEquals_MethodGroup:
        def __getitem__(self, t:typing.Type[EnumEquals_1_T1]) -> EnumEquals_1[EnumEquals_1_T1]: ...

        EnumEquals_1_T1 = typing.TypeVar('EnumEquals_1_T1')
        class EnumEquals_1(typing.Generic[EnumEquals_1_T1]):
            EnumEquals_1_T = UnsafeUtility.EnumEquals_MethodGroup.EnumEquals_1_T1
            def __call__(self, lhs: EnumEquals_1_T, rhs: EnumEquals_1_T) -> bool:...


    # Skipped EnumToInt due to it being static, abstract and generic.

    EnumToInt : EnumToInt_MethodGroup
    class EnumToInt_MethodGroup:
        def __getitem__(self, t:typing.Type[EnumToInt_1_T1]) -> EnumToInt_1[EnumToInt_1_T1]: ...

        EnumToInt_1_T1 = typing.TypeVar('EnumToInt_1_T1')
        class EnumToInt_1(typing.Generic[EnumToInt_1_T1]):
            EnumToInt_1_T = UnsafeUtility.EnumToInt_MethodGroup.EnumToInt_1_T1
            def __call__(self, enumValue: EnumToInt_1_T) -> int:...


    # Skipped IsBlittable due to it being static, abstract and generic.

    IsBlittable : IsBlittable_MethodGroup
    class IsBlittable_MethodGroup:
        def __getitem__(self, t:typing.Type[IsBlittable_1_T1]) -> IsBlittable_1[IsBlittable_1_T1]: ...

        IsBlittable_1_T1 = typing.TypeVar('IsBlittable_1_T1')
        class IsBlittable_1(typing.Generic[IsBlittable_1_T1]):
            IsBlittable_1_T = UnsafeUtility.IsBlittable_MethodGroup.IsBlittable_1_T1
            def __call__(self) -> bool:...

        def __call__(self, type: typing.Type[typing.Any]) -> bool:...

    # Skipped IsNativeContainerType due to it being static, abstract and generic.

    IsNativeContainerType : IsNativeContainerType_MethodGroup
    class IsNativeContainerType_MethodGroup:
        def __getitem__(self, t:typing.Type[IsNativeContainerType_1_T1]) -> IsNativeContainerType_1[IsNativeContainerType_1_T1]: ...

        IsNativeContainerType_1_T1 = typing.TypeVar('IsNativeContainerType_1_T1')
        class IsNativeContainerType_1(typing.Generic[IsNativeContainerType_1_T1]):
            IsNativeContainerType_1_T = UnsafeUtility.IsNativeContainerType_MethodGroup.IsNativeContainerType_1_T1
            def __call__(self) -> bool:...


    # Skipped IsUnmanaged due to it being static, abstract and generic.

    IsUnmanaged : IsUnmanaged_MethodGroup
    class IsUnmanaged_MethodGroup:
        def __getitem__(self, t:typing.Type[IsUnmanaged_1_T1]) -> IsUnmanaged_1[IsUnmanaged_1_T1]: ...

        IsUnmanaged_1_T1 = typing.TypeVar('IsUnmanaged_1_T1')
        class IsUnmanaged_1(typing.Generic[IsUnmanaged_1_T1]):
            IsUnmanaged_1_T = UnsafeUtility.IsUnmanaged_MethodGroup.IsUnmanaged_1_T1
            def __call__(self) -> bool:...

        def __call__(self, type: typing.Type[typing.Any]) -> bool:...

    # Skipped IsValidNativeContainerElementType due to it being static, abstract and generic.

    IsValidNativeContainerElementType : IsValidNativeContainerElementType_MethodGroup
    class IsValidNativeContainerElementType_MethodGroup:
        def __getitem__(self, t:typing.Type[IsValidNativeContainerElementType_1_T1]) -> IsValidNativeContainerElementType_1[IsValidNativeContainerElementType_1_T1]: ...

        IsValidNativeContainerElementType_1_T1 = typing.TypeVar('IsValidNativeContainerElementType_1_T1')
        class IsValidNativeContainerElementType_1(typing.Generic[IsValidNativeContainerElementType_1_T1]):
            IsValidNativeContainerElementType_1_T = UnsafeUtility.IsValidNativeContainerElementType_MethodGroup.IsValidNativeContainerElementType_1_T1
            def __call__(self) -> bool:...

        def __call__(self, type: typing.Type[typing.Any]) -> bool:...

    # Skipped ReadArrayElement due to it being static, abstract and generic.

    ReadArrayElement : ReadArrayElement_MethodGroup
    class ReadArrayElement_MethodGroup:
        def __getitem__(self, t:typing.Type[ReadArrayElement_1_T1]) -> ReadArrayElement_1[ReadArrayElement_1_T1]: ...

        ReadArrayElement_1_T1 = typing.TypeVar('ReadArrayElement_1_T1')
        class ReadArrayElement_1(typing.Generic[ReadArrayElement_1_T1]):
            ReadArrayElement_1_T = UnsafeUtility.ReadArrayElement_MethodGroup.ReadArrayElement_1_T1
            def __call__(self, source: clr.Reference[None], index: int) -> ReadArrayElement_1_T:...


    # Skipped ReadArrayElementWithStride due to it being static, abstract and generic.

    ReadArrayElementWithStride : ReadArrayElementWithStride_MethodGroup
    class ReadArrayElementWithStride_MethodGroup:
        def __getitem__(self, t:typing.Type[ReadArrayElementWithStride_1_T1]) -> ReadArrayElementWithStride_1[ReadArrayElementWithStride_1_T1]: ...

        ReadArrayElementWithStride_1_T1 = typing.TypeVar('ReadArrayElementWithStride_1_T1')
        class ReadArrayElementWithStride_1(typing.Generic[ReadArrayElementWithStride_1_T1]):
            ReadArrayElementWithStride_1_T = UnsafeUtility.ReadArrayElementWithStride_MethodGroup.ReadArrayElementWithStride_1_T1
            def __call__(self, source: clr.Reference[None], index: int, stride: int) -> ReadArrayElementWithStride_1_T:...


    # Skipped SizeOf due to it being static, abstract and generic.

    SizeOf : SizeOf_MethodGroup
    class SizeOf_MethodGroup:
        def __getitem__(self, t:typing.Type[SizeOf_1_T1]) -> SizeOf_1[SizeOf_1_T1]: ...

        SizeOf_1_T1 = typing.TypeVar('SizeOf_1_T1')
        class SizeOf_1(typing.Generic[SizeOf_1_T1]):
            SizeOf_1_T = UnsafeUtility.SizeOf_MethodGroup.SizeOf_1_T1
            def __call__(self) -> int:...

        def __call__(self, type: typing.Type[typing.Any]) -> int:...

    # Skipped WriteArrayElement due to it being static, abstract and generic.

    WriteArrayElement : WriteArrayElement_MethodGroup
    class WriteArrayElement_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteArrayElement_1_T1]) -> WriteArrayElement_1[WriteArrayElement_1_T1]: ...

        WriteArrayElement_1_T1 = typing.TypeVar('WriteArrayElement_1_T1')
        class WriteArrayElement_1(typing.Generic[WriteArrayElement_1_T1]):
            WriteArrayElement_1_T = UnsafeUtility.WriteArrayElement_MethodGroup.WriteArrayElement_1_T1
            def __call__(self, destination: clr.Reference[None], index: int, value: WriteArrayElement_1_T) -> None:...


    # Skipped WriteArrayElementWithStride due to it being static, abstract and generic.

    WriteArrayElementWithStride : WriteArrayElementWithStride_MethodGroup
    class WriteArrayElementWithStride_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteArrayElementWithStride_1_T1]) -> WriteArrayElementWithStride_1[WriteArrayElementWithStride_1_T1]: ...

        WriteArrayElementWithStride_1_T1 = typing.TypeVar('WriteArrayElementWithStride_1_T1')
        class WriteArrayElementWithStride_1(typing.Generic[WriteArrayElementWithStride_1_T1]):
            WriteArrayElementWithStride_1_T = UnsafeUtility.WriteArrayElementWithStride_MethodGroup.WriteArrayElementWithStride_1_T1
            def __call__(self, destination: clr.Reference[None], index: int, stride: int, value: WriteArrayElementWithStride_1_T) -> None:...




class WriteAccessRequiredAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

