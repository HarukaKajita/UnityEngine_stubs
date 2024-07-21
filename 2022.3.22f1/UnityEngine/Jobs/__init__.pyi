import typing, clr, abc
from Unity.Jobs import JobHandle
from UnityEngine import Vector3, Quaternion, Matrix4x4, Transform
from System import IDisposable, Array_1

class IJobParallelForTransform(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, index: int, transform: TransformAccess) -> None: ...


class IJobParallelForTransformExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobParallelForTransformExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...


    # Skipped RunReadOnly due to it being static, abstract and generic.

    RunReadOnly : RunReadOnly_MethodGroup
    class RunReadOnly_MethodGroup:
        def __getitem__(self, t:typing.Type[RunReadOnly_1_T1]) -> RunReadOnly_1[RunReadOnly_1_T1]: ...

        RunReadOnly_1_T1 = typing.TypeVar('RunReadOnly_1_T1')
        class RunReadOnly_1(typing.Generic[RunReadOnly_1_T1]):
            RunReadOnly_1_T = IJobParallelForTransformExtensions.RunReadOnly_MethodGroup.RunReadOnly_1_T1
            def __call__(self, jobData: RunReadOnly_1_T, transforms: TransformAccessArray) -> None:...


    # Skipped RunReadOnlyByRef due to it being static, abstract and generic.

    RunReadOnlyByRef : RunReadOnlyByRef_MethodGroup
    class RunReadOnlyByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[RunReadOnlyByRef_1_T1]) -> RunReadOnlyByRef_1[RunReadOnlyByRef_1_T1]: ...

        RunReadOnlyByRef_1_T1 = typing.TypeVar('RunReadOnlyByRef_1_T1')
        class RunReadOnlyByRef_1(typing.Generic[RunReadOnlyByRef_1_T1]):
            RunReadOnlyByRef_1_T = IJobParallelForTransformExtensions.RunReadOnlyByRef_MethodGroup.RunReadOnlyByRef_1_T1
            def __call__(self, jobData: clr.Reference[RunReadOnlyByRef_1_T], transforms: TransformAccessArray) -> None:...


    # Skipped Schedule due to it being static, abstract and generic.

    Schedule : Schedule_MethodGroup
    class Schedule_MethodGroup:
        def __getitem__(self, t:typing.Type[Schedule_1_T1]) -> Schedule_1[Schedule_1_T1]: ...

        Schedule_1_T1 = typing.TypeVar('Schedule_1_T1')
        class Schedule_1(typing.Generic[Schedule_1_T1]):
            Schedule_1_T = IJobParallelForTransformExtensions.Schedule_MethodGroup.Schedule_1_T1
            def __call__(self, jobData: Schedule_1_T, transforms: TransformAccessArray, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleByRef due to it being static, abstract and generic.

    ScheduleByRef : ScheduleByRef_MethodGroup
    class ScheduleByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleByRef_1_T1]) -> ScheduleByRef_1[ScheduleByRef_1_T1]: ...

        ScheduleByRef_1_T1 = typing.TypeVar('ScheduleByRef_1_T1')
        class ScheduleByRef_1(typing.Generic[ScheduleByRef_1_T1]):
            ScheduleByRef_1_T = IJobParallelForTransformExtensions.ScheduleByRef_MethodGroup.ScheduleByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleByRef_1_T], transforms: TransformAccessArray, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleReadOnly due to it being static, abstract and generic.

    ScheduleReadOnly : ScheduleReadOnly_MethodGroup
    class ScheduleReadOnly_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleReadOnly_1_T1]) -> ScheduleReadOnly_1[ScheduleReadOnly_1_T1]: ...

        ScheduleReadOnly_1_T1 = typing.TypeVar('ScheduleReadOnly_1_T1')
        class ScheduleReadOnly_1(typing.Generic[ScheduleReadOnly_1_T1]):
            ScheduleReadOnly_1_T = IJobParallelForTransformExtensions.ScheduleReadOnly_MethodGroup.ScheduleReadOnly_1_T1
            def __call__(self, jobData: ScheduleReadOnly_1_T, transforms: TransformAccessArray, batchSize: int, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleReadOnlyByRef due to it being static, abstract and generic.

    ScheduleReadOnlyByRef : ScheduleReadOnlyByRef_MethodGroup
    class ScheduleReadOnlyByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleReadOnlyByRef_1_T1]) -> ScheduleReadOnlyByRef_1[ScheduleReadOnlyByRef_1_T1]: ...

        ScheduleReadOnlyByRef_1_T1 = typing.TypeVar('ScheduleReadOnlyByRef_1_T1')
        class ScheduleReadOnlyByRef_1(typing.Generic[ScheduleReadOnlyByRef_1_T1]):
            ScheduleReadOnlyByRef_1_T = IJobParallelForTransformExtensions.ScheduleReadOnlyByRef_MethodGroup.ScheduleReadOnlyByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleReadOnlyByRef_1_T], transforms: TransformAccessArray, batchSize: int, dependsOn: JobHandle = ...) -> JobHandle:...




class TransformAccess:
    @property
    def isValid(self) -> bool: ...
    @property
    def localPosition(self) -> Vector3: ...
    @localPosition.setter
    def localPosition(self, value: Vector3) -> Vector3: ...
    @property
    def localRotation(self) -> Quaternion: ...
    @localRotation.setter
    def localRotation(self, value: Quaternion) -> Quaternion: ...
    @property
    def localScale(self) -> Vector3: ...
    @localScale.setter
    def localScale(self, value: Vector3) -> Vector3: ...
    @property
    def localToWorldMatrix(self) -> Matrix4x4: ...
    @property
    def position(self) -> Vector3: ...
    @position.setter
    def position(self, value: Vector3) -> Vector3: ...
    @property
    def rotation(self) -> Quaternion: ...
    @rotation.setter
    def rotation(self, value: Quaternion) -> Quaternion: ...
    @property
    def worldToLocalMatrix(self) -> Matrix4x4: ...
    def GetLocalPositionAndRotation(self, localPosition: clr.Reference[Vector3], localRotation: clr.Reference[Quaternion]) -> None: ...
    def GetPositionAndRotation(self, position: clr.Reference[Vector3], rotation: clr.Reference[Quaternion]) -> None: ...
    def SetLocalPositionAndRotation(self, localPosition: Vector3, localRotation: Quaternion) -> None: ...
    def SetPositionAndRotation(self, position: Vector3, rotation: Quaternion) -> None: ...


class TransformAccessArray(IDisposable):
    @typing.overload
    def __init__(self, capacity: int, desiredJobCount: int = ...) -> None: ...
    @typing.overload
    def __init__(self, transforms: Array_1[Transform], desiredJobCount: int = ...) -> None: ...
    @property
    def capacity(self) -> int: ...
    @capacity.setter
    def capacity(self, value: int) -> int: ...
    @property
    def isCreated(self) -> bool: ...
    @property
    def Item(self) -> Transform: ...
    @Item.setter
    def Item(self, value: Transform) -> Transform: ...
    @property
    def length(self) -> int: ...
    @staticmethod
    def Allocate(capacity: int, desiredJobCount: int, array: clr.Reference[TransformAccessArray]) -> None: ...
    def Dispose(self) -> None: ...
    def RemoveAtSwapBack(self, index: int) -> None: ...
    def SetTransforms(self, transforms: Array_1[Transform]) -> None: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, instanceId: int) -> None:...
        @typing.overload
        def __call__(self, transform: Transform) -> None:...


