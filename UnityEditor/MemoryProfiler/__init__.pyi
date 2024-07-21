import typing, abc
import UnityEditor.Profiling.Memory.Experimental
from System import Array_1
from UnityEngine import HideFlags

class Connection:
    def __init__(self, from_: int, to: int) -> None: ...
    @property
    def from(self) -> int: ...
    @from.setter
    def from(self, value: int) -> int: ...
    @property
    def to(self) -> int: ...
    @to.setter
    def to(self, value: int) -> int: ...


class FieldDescription:
    def __init__(self, name: str, offset: int, typeIndex: int, isStatic: bool) -> None: ...
    @property
    def isStatic(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def offset(self) -> int: ...
    @property
    def typeIndex(self) -> int: ...


class MemorySection:
    def __init__(self, bytes: Array_1[int], startAddress: int) -> None: ...
    @property
    def bytes(self) -> Array_1[int]: ...
    @property
    def startAddress(self) -> int: ...


class MemorySnapshot(abc.ABC):
    @staticmethod
    def RequestNewSnapshot() -> None: ...


class PackedGCHandle:
    def __init__(self, target: int) -> None: ...
    @property
    def target(self) -> int: ...


class PackedMemorySnapshot:
    def __init__(self, snapshot: UnityEditor.Profiling.Memory.Experimental.PackedMemorySnapshot) -> None: ...
    @property
    def connections(self) -> Array_1[Connection]: ...
    @property
    def gcHandles(self) -> Array_1[PackedGCHandle]: ...
    @property
    def managedHeapSections(self) -> Array_1[MemorySection]: ...
    @property
    def nativeObjects(self) -> Array_1[PackedNativeUnityEngineObject]: ...
    @property
    def nativeTypes(self) -> Array_1[PackedNativeType]: ...
    @property
    def typeDescriptions(self) -> Array_1[TypeDescription]: ...
    @property
    def virtualMachineInformation(self) -> VirtualMachineInformation: ...


class PackedNativeType:
    def __init__(self, name: str, nativeBaseTypeArrayIndex: int) -> None: ...
    @property
    def baseClassId(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def nativeBaseTypeArrayIndex(self) -> int: ...


class PackedNativeUnityEngineObject:
    def __init__(self, name: str, instanceId: int, size: int, nativeTypeArrayIndex: int, hideFlags: HideFlags, flags: PackedNativeUnityEngineObject.ObjectFlags, nativeObjectAddress: int) -> None: ...
    @property
    def classId(self) -> int: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @property
    def instanceId(self) -> int: ...
    @property
    def isDontDestroyOnLoad(self) -> bool: ...
    @property
    def isManager(self) -> bool: ...
    @property
    def isPersistent(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def nativeObjectAddress(self) -> int: ...
    @property
    def nativeTypeArrayIndex(self) -> int: ...
    @property
    def size(self) -> int: ...

    class ObjectFlags(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        IsDontDestroyOnLoad : PackedNativeUnityEngineObject.ObjectFlags # 1
        IsPersistent : PackedNativeUnityEngineObject.ObjectFlags # 2
        IsManager : PackedNativeUnityEngineObject.ObjectFlags # 4



class TypeDescription:
    def __init__(self, name: str, assembly: str, fields: Array_1[FieldDescription], staticFieldBytes: Array_1[int], baseOrElementTypeIndes: int, size: int, typeInfoAddress: int, typeIndex: int, flags: TypeDescription.TypeFlags) -> None: ...
    @property
    def arrayRank(self) -> int: ...
    @property
    def assembly(self) -> str: ...
    @property
    def baseOrElementTypeIndex(self) -> int: ...
    @property
    def fields(self) -> Array_1[FieldDescription]: ...
    @property
    def isArray(self) -> bool: ...
    @property
    def isValueType(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def size(self) -> int: ...
    @property
    def staticFieldBytes(self) -> Array_1[int]: ...
    @property
    def typeIndex(self) -> int: ...
    @property
    def typeInfoAddress(self) -> int: ...

    class TypeFlags(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        kNone : TypeDescription.TypeFlags # 0
        kValueType : TypeDescription.TypeFlags # 1
        kArray : TypeDescription.TypeFlags # 2
        kArrayRankMask : TypeDescription.TypeFlags # -65536



class VirtualMachineInformation:
    @property
    def allocationGranularity(self) -> int: ...
    @property
    def arrayBoundsOffsetInHeader(self) -> int: ...
    @property
    def arrayHeaderSize(self) -> int: ...
    @property
    def arraySizeOffsetInHeader(self) -> int: ...
    @property
    def heapFormatVersion(self) -> int: ...
    @property
    def objectHeaderSize(self) -> int: ...
    @property
    def pointerSize(self) -> int: ...

